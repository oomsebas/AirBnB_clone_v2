#!/usr/bin/python3
""" script distributes an archive to your web servers"""
from fabric.api import local, run, put, env
from datetime import datetime
from os import path


env.hosts = ['35.237.144.175', '35.237.121.43']


def deploy():
        """script that creates and distributes an archive to web servers """

        path_tar = do_pack()
        if path_tar:
                return do_deploy(path_tar)
        return False


def do_pack():
        """Generates a tgz archive"""

        try:
            file_time = datetime.now().strftime("%Y%m%d%H%M%S")
            file_name = "web_static_{}.tgz".format(file_time)
            comm = "tar -cvzf versions/{} web_static".format(file_name)
            local("mkdir -p versions")
            local(comm)
            return "versions/" + file_name
        except:
            return None


def do_deploy(archive_path):
    """copy an archive to the web servers"""

    if path.exists(archive_path) is True:
        try:
            path_ls = archive_path.split("/")
            file_name = path_ls[-1]
            path_name = "/data/web_static/releases/" + file_name.split(".")[0]
            ufile = put(local_path=archive_path, remote_path='/tmp/')
            run('mkdir -p {}/'.format(path_name))
            run('tar -xzf /tmp/{} -C {}/'.format(file_name, path_name))
            run('rm /tmp/{}'.format(file_name))
            run('mv {}/web_static/* {}/'.format(path_name, path_name))
            run('rm -rf {}/web_static'.format(path_name))
            run('rm -rf /data/web_static/current')
            run('ln -s {}/ /data/web_static/current'.format(path_name))
            print('New Version Deployed!')
            return True
        except:
            return False
    return False
