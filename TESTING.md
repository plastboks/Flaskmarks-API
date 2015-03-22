#Routes
Current routes
* POST /register
* GET /token/key
* POST /token
* GET /tokens
* POST /mark
* {GET,PUT} /mark/id
* GET /marks
* GET /tags

#CURLing
Some crude CURL tests

##Register

```bash
curl -X POST -v -d "user=test&email=post@example.net&password=1234" \
         http://localhost:5000/register

curl -X POST -v -H "Content-Type: application/json" \
         -d '{"user":"test", "email":"post@example.net", "password":"1234"}' \
         http://localhost:5000/register
```
```json
{
    "apikeys": [
        [
            "master", 
            "..."
        ]
    ], 
    "created": "Sun, 22 Mar 2015 18:11:04 -0000", 
    "email": "test@example.net", 
    "id": 1
}
```

##Tokens

```bash
curl -X GET -v --basic -u "post@example.net:1234" \
         http://localhost:5000/tokens

curl -X GET -v --basic -u "post@example.net:1234" \
         https://localhost:5000/token/master
```

##New token

```bash
curl -X POST -v --basic -u "post@example.net:1234" \
         -d "key=apple" \
         https://localhost:5000/token
```

##New mark

```bash
curl -X POST -v --basic -u "post@example.net:1234" \
         -d "type=bookmark&title=test&tags=1,2,3&url=http://example.org" \
         http://localhost:5000/mark

curl -X POST -v -H "Content-Type: application/json" \
         --basic -u "post@example23.net:1234" \
         -d '{"type":"bookmark", "title":"test", "url":"http://example.net"}' \
         http://localhost:5000/mark 
```
```json
{
    "clicks": 0, 
    "created": "Sun, 22 Mar 2015 18:11:06 -0000", 
    "id": 18, 
    "last_clicked": null, 
    "tags": [
        "tag1", 
        "tag2", 
        "tag3"
    ], 
    "title": "updated title", 
    "type": "bookmark", 
    "updated": null, 
    "url": "http://example.org"
}
```

##Update mark

```bash
curl -X PUT -v --basic -u "post@example.net:1234" \
         -d "title=horse" \
         http://localhost:5000/mark/3 

curl -X PUT -v -H "Content-Type: application/json" \
         --basic -u "post@example23.net:1234" \
         -d '{"title":"horse"}' \
         http://localhost:5000/mark/3
```

##Delete mark

```bash
not implemented
```

##All marks

```bash
curl -X GET -v --basic -u "post@example.net:1234" http://localhost:5000/marks
```
```json
{
    "marks": [
        {
            "clicks": 0, 
            "created": "Sun, 22 Mar 2015 18:11:06 -0000", 
            "id": 18, 
            "last_clicked": null, 
            "tags": [
                "tag1", 
                "tag2", 
                "tag3"
            ], 
            "title": "updated title", 
            "type": "bookmark", 
            "updated": null, 
            "url": "http://example.org"
        }
    ], 
    "pager": {
        "next_num": false, 
        "page": 1, 
        "pages": 1, 
        "prev_num": false, 
        "total": 1
    }
}
```

##Using token auth
```bash
curl -X GET -v --basic -u "tokenkey:unused" http://localhost:5000/marks
```
