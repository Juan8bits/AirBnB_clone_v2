#!/usr/bin/python3
# Script that generates a .tgz archive from the contents of the
# web_static folder of your AirBnB Clone repo, using the function do_pack.
from fabric.api import local
from datetime import datetime


def do_pack():
    """Packs a local web_static folder to .tgz format for deployment"""

    local("mkdir -p versions")
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    rest = local('tar -cvzf versions/web_static_{}.tgz web_static'
                 .format(time))
    if rest.failed:
        return None
    return rest
