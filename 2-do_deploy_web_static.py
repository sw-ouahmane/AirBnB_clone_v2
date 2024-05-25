#!/usr/bin/python3
"""web server distribution"""
from fabric.api import *
import os.path

env.user = 'ubuntu'
env.hosts = ["54.146.65.131", "18.208.120.199"]
env.key_filename = "~/.ssh/school"


def do_deploy(archive_path):
    """distributes an archive to your web servers
    """
    if os.path.exists(archive_path) is False:
        return False
    data_path = '/data/web_static/releases/'
    tmp = archive_path.split('.')[0]
    name = tmp.split('/')[1]
    dest = data_path + name

    try:
        put(archive_path, '/tmp')
        run('mkdir -p {}'.format(dest))
        run('tar -xzf /tmp/{}.tgz -C {}'.format(name, dest))
        run('rm -f /tmp/{}.tgz'.format(name))
        run('mv {}/web_static/* {}/'.format(dest, dest))
        run('rm -rf {}/web_static'.format(dest))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(dest))
        return True
    except Exception:
        return False
