# Pet app
## Pet app as a job interview. Done in python and django, django REST framework with mySQL and deployed on heroku.

## Description

Web Application for Users and Pets. Users and Pets API endpoints done with Django REST framework. 

## Installation
Tip:  Your folder structure should look like this:
    * petapp
    * v

where __petapp__ is folder where you clone repository, and __v__ your virtual enviroment.

Install the dependecies.

    $ source v/bin/activate
    $ cd petapp
    $ pip install -r requirements.txt
    $ python manage.py makemigrations
    $ python manage.py migrate


## Run server

    $ cd petapp/
    $ python manage.py runserver
