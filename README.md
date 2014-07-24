Flaskmarks-API
==============
Flaskmarks RESTful API. This Flaskmarks API is meant to be the backend to flaskmarks in the future... As a consequence the Flaskmarks repository have no planned feature implementations and will most likely migrate over to a web client for this API.

Description
===========
See Flaskmarks repository.

Install
=======
* Create and activate a python virtualenv.
* make a copy of config/default.py.example to config/default.py and edit accordingly.
* make a copy of config/environment.py.example to config/environment.py and edit accordingly.
* run: `pip install -r requirements.txt`.
* run: `python run.py db init`
* run: `python run.py db migrate`
* run: `python run.py db upgrade`
* set: `export APP_CONFIG_FILE=$PWD/config/environment.py`
* run: `python run.py runserver`

Upgrade
=======
* run: `python run.py db migrate`
* run: `python run.py db upgrade`

Package updates
===============
* run: `pip install --upgrade -r requirements.txt`


Testing
=======
* run: `nosetests --with-coverage --cover-package=api --cover-erase`

Branches
========
There will at any given point be at least two branches in this repository. One
master (stable) branch, and one develop branch. The develop branch might contain
unfinished code and/or wonky solutions. I will strive to make sure that code 
merged into master is as stable as possible (given the small size of this application).

Code
====
The validators.py file in api/core was forked from [django](https://github.com/django/django) and modified to fit my needs.

Useful Links
============
* [Flask RESTful](http://flask-restful.readthedocs.org/en/latest/)
