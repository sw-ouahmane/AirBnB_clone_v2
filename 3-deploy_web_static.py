#!/usr/bin/python3
"""Generates a Compress (tgz) update - uncompress and create simbolic link"""

from fabric.api import put, run, env, local
from datetime import datetime
from os.path import exists


env.user = 'ubuntu'
env.hosts = ['54.237.43.101', '100.25.156.252']


def do_pack():
    """Function to compress files"""
    local("mkdir -p versions")
    str_date = datetime.now().strftime('%Y%m%d%H%M%S')
    result = local("tar -czvf versions/web_static_" +
                   str_date + ".tgz web_static")
    if result.failed:
        return None
    return "versions/web_static_" + str_date + ".tgz"


def do_deploy(archive_path):
    """
        Distributes an archive to your web servers
    """
    if not exists(archive_path):
        return False

    _path = archive_path.split("/")
    path_no_ext = _path[1].split(".")[0]

    try:
        put(archive_path, "/tmp")
        run("sudo mkdir -p /data/web_static/releases/" + path_no_ext + "/")
        run("sudo tar -xzf /tmp/" + path_no_ext + ".tgz" +
            " -C /data/web_static/releases/" + path_no_ext + "/")
        run("sudo rm /tmp/" + path_no_ext + ".tgz")
        run("sudo mv /data/web_static/releases/" + path_no_ext +
            "/web_static/* /data/web_static/releases/" + path_no_ext + "/")
        run("sudo rm -rf /data/web_static/releases/" +
            path_no_ext + "/web_static")
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s /data/web_static/releases/" + path_no_ext +
            "/ /data/web_static/current")
        return True

    except Exception:
        return False


def deploy():
    """compress and deploy a tar file to a web server"""
    return_pack = do_pack()
    if return_pack is None:
        return False
    return do_deploy(return_pack)






