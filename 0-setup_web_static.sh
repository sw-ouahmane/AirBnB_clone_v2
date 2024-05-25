#!/usr/bin/env bash
# set up index.html

sudo apt-get update -y
sudo apt-get install nginx -y
ufw allow 'Nginx HTTP'
sudo mkdir -p "/data/web_static/releases/test/"
sudo mkdir -p  "/data/web_static/shared/"
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
rm -f /data/web_static/current
ln -s /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data
sudo sed -i '/listen 80 default_server/a location /hbnb_static/ { alias /data/web_static/current/;}' /etc/nginx/sites-available/default
sudo service nginx restart
