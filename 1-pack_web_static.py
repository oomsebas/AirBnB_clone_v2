#!/usr/bin/python3
"""create a tgz file """

from fabric.api import local
from datetime import datetime


def do_pack():
        """Generates a tgz archive"""
        try:
            local("mkdir -p versions")
            file_time = datetime.now().strftime("%Y%m%d%H%M%S")
            file_name = "web_static_{}.tgz".format(file_time)
            comm = "tar -cvzf versions/{} web_static".format(file_name)
            return local(comm)
        except:
            return None
