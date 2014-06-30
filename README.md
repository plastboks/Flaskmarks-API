Flaskmarks-API
==============

Flaskmarks REST API

Description
===========
See Flaskmarks repository.

Install
=======
* Create and activate a python virtualenv.
* make a copy of config.py.example to config.py and edit accordingly.
* run: `pip install -r requirements.txt`.
* run: `python run.py db init`
* run: `python run.py db migrate`
* run: `python run.py db upgrade`
* run: `python run.py runserver`

Upgrade
=======
* run: `python run.py db migrate`
* run: `python run.py db upgrade`

Package updates
===============
* run: `pip install --upgrade -r requirements.txt`

Branches
========
There will at any given point be at least two branches in this repository. One
master (stable) branch, and one develop branch. The develop branch might contain
unfinished code and/or wonky solutions. I will strive to make sure that code 
merged into master is as stable as possible (given the small size of this application).

Useful Links
============
* [Flask RESTful](http://flask-restful.readthedocs.org/en/latest/)
