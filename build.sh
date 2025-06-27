#!/usr/bin/env bash

apt-get update

# Install Chromium and matching ChromeDriver
apt-get install -y chromium-browser chromium-chromedriver

# Symlink to standard paths (so Selenium can find them)
ln -sf /usr/bin/chromium-browser /usr/bin/google-chrome
ln -sf /usr/lib/chromium-browser/chromedriver /usr/bin/chromedriver
