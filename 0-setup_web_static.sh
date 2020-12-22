#!/usr/bin/env bash
# sets up your web servers for the deployment

mkdir /data/
mkdir /data/web_static/
mkdir /data/web_static/releases/
mkdir /data/web_static/shared/
mkdir /data/web_static/releases/test/
echo "Holberton school" | sudo tee /data/web_static/releases/test/
sudo chown -R ubuntu: /data/
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo sed -i "25 i\\\tlocation /hbnb_static{\n\t\talias /data/web_static/\
current/;\n\t}" /etc/nginx/sites-available/default
