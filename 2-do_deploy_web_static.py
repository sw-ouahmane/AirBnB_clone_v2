#!/usr/bin/python3
"""
Fabric script based on the file 1-pack_web_static.py that distributes an
archive to the web servers
"""

from fabric.api import put, run, env, local
from os.path import exists

env.hosts = ['54.237.43.101', '52.86.186.82']

def do_pack():
    """
    Generate a .tgz archive from the contents of the web_static folder.
    """
    now = datetime.now()
    archive_name = "versions/web_static_{}.tgz".format(now.strftime("%Y%m%d%H%M%S"))

    # Ensure the versions directory exists
    local('mkdir -p versions')

    # Create the archive using tar
    result = local('tar -cvzf {} web_static'.format(archive_name))

    if result.succeeded:
        return archive_name
    else:
        return None

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        print(f"Archive path {archive_path} does not exist.")
        return False

    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"

        print(f"Uploading {archive_path} to /tmp/ on each server...")
        put(archive_path, '/tmp/')

        print(f"Creating directory {path}{no_ext}/ on each server...")
        run('mkdir -p {}{}/'.format(path, no_ext))

        print(f"Unpacking the archive into {path}{no_ext}/ on each server...")
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))

        print(f"Deleting the archive from /tmp/ on each server...")
        run('rm /tmp/{}'.format(file_n))

        print(f"Moving contents from {path}{no_ext}/web_static/ to {path}{no_ext}/ on each server...")
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))

        print(f"Deleting the web_static directory from {path}{no_ext}/ on each server...")
        run('rm -rf {}{}/web_static'.format(path, no_ext))

        print(f"Removing the current symbolic link on each server...")
        run('rm -rf /data/web_static/current')

        print(f"Creating a new symbolic link to {path}{no_ext}/ on each server...")
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))

        print("New version deployed!")
        return True

    except Exception as e:
        print(f"An error occurred: {e}")
        return False

