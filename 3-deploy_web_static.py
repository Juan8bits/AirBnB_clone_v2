#!/usr/bin/python3
# Script that do A FULL deployment based on previous task 1 and 2.
from fabric.api import env, local, put, run
from datetime import datetime


env.hosts = ['34.74.10.45', '54.235.19.10']
env.user = 'ubuntu'


def do_pack():
    """ Generates a .tgz archive from the contents of the web_static """
    try:
        dt = datetime.now().strftime("%Y%m%d%H%M%S")
        local('mkdir -p versions')
        local('tar -cvzf versions/web_static_{}.tgz web_static'.format(dt))

        return 'versions/web_static_{}.tgz'.format(dt)
    except:
        return None


def do_deploy(archive_path):
    """ Distributed an archive to servers """

    if not archive_path:
        return False

    try:

        file = archive_path.split('/')[-1]
        nm = file.split('.')[0]
        fn = '/data/web_static/releases/'

        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(fn, nm))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file, fn, nm))
        run('rm /tmp/{}'.format(file))
        run('rm -rf /data/web_static/current')
        run('ln -sf {}{}/ /data/web_static/current'.format(fn, nm))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(fn, nm))
        run('rm -rf {}{}/web_static'.format(fn, nm))

        return True

    except:
        return False


def deploy():
    """Full deployment"""

    zip = do_pack()
    if zip:
        return do_deploy(zip)
    return False
