#!/usr/bin/env bash

# Install dependencies
apt-get update
apt-get install -y wget gnupg2 apt-transport-https curl unzip

# Install Chrome
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
apt install -y ./google-chrome-stable_current_amd64.deb

# Confirm binary path
which google-chrome
