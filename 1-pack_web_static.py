#!/usr/bin/python3
"""
Fabric script to generate a tgz archive
Execute: fab -f 1-pack_web_static.py do_pack
"""

from datetime import datetime
from fabric.api import local

def do_pack():
    """
    Generate a .tgz archive from the contents of the web_static folder.
    """
    # Create a timestamped archive name
    now = datetime.now()
    archive_name = "versions/web_static_{}.tgz".format(now.strftime("%Y%m%d%H%M%S"))
    
    # Ensure the versions directory exists
    local('mkdir -p versions')
    
    # Create the archive using tar
    result = local('tar -cvzf {} web_static'.format(archive_name))
    
    if result.succeeded:
        print("Packing web_static to {}".format(archive_name))
        return archive_name
    else:
        print("Failed to create archive")
        return None

