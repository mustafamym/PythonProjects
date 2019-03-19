# Requirements

# REST framework requires the following:

Python (2.7, 3.4, 3.5, 3.6, 3.7)

# create virtualenv

$virtualenv env

$source env/Scripts/activate[windows]

$source env/bin/activate[[linux/mac]

## how to deactive virtualenv

$deactivate

# Getting started with Django 

## Install Django

$ pip install django

## Run the Django migrations to set up your models:

$ python manage.py makemigrations

$ python manage.py makemigrations polls

$ python manage.py migrate

## Start a local web server:

python manage.py runserver

## In your web browser, enter this address:

http://localhost:8000

## Stop a local web server:

press Ctrl+C to stop the local web server.