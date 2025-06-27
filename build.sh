#!/usr/bin/env bash

apt-get update
apt-get install -y wget curl gnupg2 apt-transport-https unzip

# Download and install Google Chrome
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
apt install -y ./google-chrome-stable_current_amd64.deb

# Move Chrome binary to standard location
ln -s /usr/bin/google-chrome-stable /usr/bin/google-chrome
