#!/usr/bin/env bash
# Sets up your web servers for the deployment of web_static
sudo apt-get -y update
sudo apt-get -y install nginx
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "Testing file" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i '/http {/a \\tserver { \n\t\tlocation /hbnb_static/ {\n\t\t\talias /data/web_static/current/;\n\t\t}\n\t}\n' /etc/nginx/nginx.conf
service nginx restart
