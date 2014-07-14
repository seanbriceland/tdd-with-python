Provisioning a new site
=======================

## Required packages:

 * nginx
 * Python 3
 * Git
 * pip (pip3)
 * virtualenv

eg, on Ubuntu:
    
    sudo apt-get update
    sudo apt-get install nginx git python3 python3-pip
    sudo pip3 install virtualenv

## Nginx Virtual Host Config

 * see nginx.template.conf
 * replace SITENAME with, eg, staging.example-domain.com

## Upstart Job

 * see gunicorn-upstart.template.conf
 * replace SITENAME with, eg, staging.example-domain.com

## Folder Structure:

(Assume we have a nonroot user with sudo priveleges at /home/username)


/home/username

    └── sites

        └── SITENAME

            ├── database

            ├── source

            ├── static

            └── virtualenv
