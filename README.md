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
* run: `sed -i s/REPLACE_ME/$(python -c "import uuid;print uuid.uuid4()")/g config/default.py`
* run: `pip install -r requirements.txt`.
* set: `export APP_CONFIG_FILE=$PWD/config/environment.py`
* run: `python run.py db init`
* run: `python run.py db migrate`
* run: `python run.py db upgrade`
* run: `python run.py runserver`

Docker
======
Now with a docker automated build. See [the registry](https://registry.hub.docker.com/u/plastboks/flaskmarks-api/) for details.
* change directory into `./docker`
* run: `build` (need superuser)
* run: `debug` or `daemon` (need superuser)

Upgrade
=======
* run: `python run.py db migrate`
* run: `python run.py db upgrade`

Package updates
===============
* run: `pip install --upgrade -r requirements.txt`

Routes
======
Current routes
* GET /register
* POST /mark
* {GET,PUT} /mark/id
* GET /marks
* GET /tags

Authentication
=============
Basic auth only.

Testing
=======
* run: `nosetests --with-coverage --cover-package=api --cover-erase`

CURLing
=======
Some crude CURL tests
* register:
```bash
curl -X POST -v -d "user=test&email=post@example.net&password=1234" \
         http://localhost:5000/register

curl -X POST -v -H "Content-Type: application/json" \
         -d '{"user":"test", "email":"post@example.net", "password":"1234"}' \
         http://localhost:5000/register
```
* tokens:
```bash
curl -X GET -v --basic -u "post@example.net:1234" \
         http://localhost:5000/tokens

curl -X GET -v --basic -u "post@example.net:1234" \
         https://localhost:5000/token/master
```
* new token:
```bash
curl -X POST -v --basic -u "post@example.net:1234" \
         -d "key=apple" \
         https://localhost:5000/token
```
* new mark:
```bash
curl -X POST -v --basic -u "post@example.net:1234" \
         -d "type=bookmark&title=test&tags=1,2,3&url=http://example.org" \
         http://localhost:5000/mark

curl -X POST -v -H "Content-Type: application/json" \
         --basic -u "post@example23.net:1234" \
         -d '{"type":"bookmark", "title":"test", "url":"http://example.net"}' \
         http://localhost:5000/mark 
```
* update mark:
```bash
curl -X PUT -v --basic -u "post@example.net:1234" \
         -d "title=horse" \
         http://localhost:5000/mark/3 

curl -X PUT -v -H "Content-Type: application/json" \
         --basic -u "post@example23.net:1234" \
         -d '{"title":"horse"}' \
         http://localhost:5000/mark/3
```
* delete:
```bash
not implemented
```
* all marks:
```bash
curl -X GET -v --basic -u "post@example.net:1234" http://localhost:5000/marks
```
* using token auth
```bash
curl -X GET -v --basic -u "tokenkey:unused" http://localhost:5000/marks
```


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
