#!/usr/bin/env bash
# This script sets up your web servers for the deployment of web_static.
if ! which nginx /dev/null 2>&1;
then
    apt-get -y update
    apt-get -y upgrade
    apt-get -y install nginx
fi
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
ln -f -s /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i '56 i \\n\tlocation \/hbnb_static {\n\t\talias /data/web_static/current/;\n\t\tindex index.html;\n\t}' /etc/nginx/sites-available/default
service nginx restart
