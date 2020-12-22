#!/usr/bin/python3
"""Generates a .tgz archive from the contents of the web_static
folder of your AirBnB Clone repo"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """Generates a tgz archive"""

    try:
        file_time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "web_static_{}.tgz".format(file_time)
        comm = "tar -cvzf versions/{} web_static".format(file_name)
        local("mkdir -p versions")
        return local(comm)
    except:
        return None
