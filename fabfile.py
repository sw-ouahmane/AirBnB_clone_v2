#!/usr/bin/python3
"""mysql server distribution must be 5.7.x"""
from fabric.api import env, run, sudo

import os.path

env.user = 'ubuntu'
env.hosts = ["54.146.65.131", "18.208.120.199"]
env.key_filename = "~/.ssh/school"

def setup_mysql_user():
    """Set up MySQL user and permissions."""


	# Use the MySQL root password if set, otherwise adjust accordingly
	mysql_root_password = 'root' 

	# Create the MySQL user
	command_create_user = "mysql -uroot -p{password} -e \"CREATE USER 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';\"".format(password=mysql_root_password)
	sudo(command_create_user)

	# Grant REPLICATION CLIENT permission
	command_grant_perm = "mysql -uroot -p{password} -e \"GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';\"".format(password=mysql_root_password)
	sudo(command_grant_perm)

	# Show the grants for holberton_user
	command_show_grants = "mysql -uholberton_user -pprojectcorrection280hbtn -e \"SHOW GRANTS FOR 'holberton_user'@'localhost'\""
	run(command_show_grants)

		
def install_mysql():
	"""install mysql server
	"""
	try:
		# Remove any existing MySQL packages
		# sudo('apt-get remove --purge mysql-server mysql-client mysql-common -y')
		# sudo('apt-get autoremove -y')
		# sudo('apt-get autoclean')
		# sudo('rm -rf /etc/mysql /var/lib/mysql')
		# sudo('deluser mysql')
		# sudo('rm -rf /var/log/mysql*')

		# # Update package information
		# sudo('apt-get update')

		# # Add the MySQL APT repository for 5.7.25

		# run('wget https://dev.mysql.com/get/mysql-apt-config_0.8.12-1_all.deb')
		# sudo('dpkg -i mysql-apt-config_0.8.12-1_all.deb')

		# # During the installation of the above, a configuration screen appears. 
		# # This needs to be handled manually to select MySQL 5.7.
		# # Assuming you have handled this manually and selected MySQL 5.7...

		# # Update package information again
		# sudo('apt-get update')

		# # Install MySQL server
		# sudo('DEBIAN_FRONTEND=noninteractive apt-get install -y mysql-server')

		# # You can add the MySQL root password setting and `mysql_secure_installation` automation if desired, but this requires some additional steps and tools like 'expect'.

		# # Start and enable MySQL
		# sudo('systemctl start mysql')
		# sudo('systemctl enable mysql')
		# run('mysql --version')
		return True
	except Exception:
		print("Error")
		print("Error: {}".format(e))
		return False
