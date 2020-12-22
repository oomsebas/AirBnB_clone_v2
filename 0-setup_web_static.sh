#!/usr/bin/env bash
# sets up your web servers for the deployment
sudo apt-get update
sudo apt_get install nginx
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "Holberton school" | sudo tee /data/web_static/releases/test/
sudo chown -R ubuntu: /data/
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo sed -i "25 i\\\tlocation /hbnb_static{\n\t\talias /data/web_static/current/;\n\t}" /etc/nginx/sites-available/default
sudo service nginx start
