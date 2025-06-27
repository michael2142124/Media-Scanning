#!/usr/bin/env bash

# Update and install dependencies
apt-get update
apt-get install -y wget gnupg2 apt-transport-https curl unzip

# Install Google Chrome (headless)
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
apt install -y ./google-chrome-stable_current_amd64.deb
