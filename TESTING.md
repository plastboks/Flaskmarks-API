Routes
======
Current routes
* POST /register
* GET /token/key
* POST /token
* GET /tokens
* POST /mark
* {GET,PUT} /mark/id
* GET /marks
* GET /tags

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
