#!/usr/bin/python3
# Fabric script (based on the file 1-pack_web_static.py) that
# distributes an archive to your web servers, using the function do_deploy.
from fabric.api import run, put, env
from os.path import exists

env.user = 'ubuntu'
env.hosts = ['34.74.10.45', '54.235.19.10']


def do_deploy(archive_path):
    """ Do_deploy Function.
    archive_path will be pass as argument.
    """

    if exists(archive_path) is False:
        return False

    filename_wo_ext = archive_path[9:34]
    filename_w_ext = archive_path[9:]
    input_path = "/data/web_static/releases/{}/".format(filename_wo_ext)

    try:
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(input_path))
        run("sudo tar -zxvf /tmp/{} -C {}".format(filename_w_ext, input_path))
        run("sudo rm -rf /tmp/{}".format(filename_w_ext))
        run("sudo mv -n {}/web_static/* {}".format(input_path, input_path))
        run("sudo rm -rf {}/web_static".format(input_path))
        run("sudo rm /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(input_path))
        return True

    except Exception:
        return False
