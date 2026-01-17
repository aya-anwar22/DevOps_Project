#!/bin/bash
# تحديث السيرفر
sudo dnf update -y
# تثبيت Python + pip
sudo dnf install python3 python3-pip -y
# تثبيت MariaDB
bash scripts/install_mariadb.sh
# تثبيت virtualenv
pip3 install virtualenv
# تهيئة Flask environment
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
