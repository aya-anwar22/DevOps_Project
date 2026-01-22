#!/bin/bash
sudo dnf update -y
sudo dnf install python3 python3-pip -y
bash scripts/install_mariadb.sh
pip3 install virtualenv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
