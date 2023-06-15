# Modexa-Biotech-Django-Test
This repository contains django RestApi test code  organized by Modexa Biotech

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Commands](#commands)
* [App endpoints](#app-endpoints)
* [API Documentation](#api-documentation)


## General info
Modexa-Biotech-Django-Test

## Technologies
* Python
* Django
* Django Rest Framework
* SQlite3

### Setup
## Installation on Linux and Mac OS or windows
* Clone project from the develop branch
```
git clone https://github.com/lilcoded7/Modexa-Biotech-Django-Test.git
```

* To create a normal virtualenv (example .venv) and activate it (see Code below).

  ```
  virtualenv --python=python3.10.6 .venv
  
  . .venv/bin/activate

  (.venv) $ pip install -r requirements.txt

  (.venv) $ python manage.py makemigrations

  (.venv) $ python manage.py migrate

  (.venv) $ python manage.py createsuperuser 

  (.venv) $ python manage.py runserver
  ```
 * Or 
 
 * run pipenv shell to activate the virtual environment
  ```
 pipenv shell 
 ```
 
  (.pipenv) $ pip install -r requirements.txt

  (.pipenv) $ python manage.py makemigrations

  (.pipenv) $ python manage.py migrate

  (.pipenv) $ python manage.py createsuperuser 

  (.pipenv) $ python manage.py runserver
 
 
* Copy the IP address provided once your server has completed building the site. (It will say something like >> Serving at http://0.0.0.0:8000).
* Open the address in the browser


## App Endpoints

* create Patient whiles authenticated 
http://127.0.0.1:8000/api/v1/

* update, delete, retrieve, Paitent details 
http://127.0.0.1:8000/api/v1/crude/

## API Documentation
```
http://127.0.0.1:8000/doc
```
