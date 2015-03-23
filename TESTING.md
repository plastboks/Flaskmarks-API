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

#Register

```bash
curl -X POST -v -d "user=test&email=post@example.net&password=1234" \
         http://localhost:5000/register

or

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

#Token

##Add

```bash
curl -X POST -v --basic -u "post@example.net:1234" \
         -d "key=apple" \
         http://localhost:5000/token
```
```json
{
    "expires": "Wed, 25 Mar 2015 06:22:02 -0000", 
    "key": "apple", 
    "value": "..."
}
```

##Get by key

```
curl -X GET -v --basic -u "post@example.net:1234" \
         http://localhost:5000/token/{:key}
```
```json
{
    "expires": null, 
    "key": "master", 
    "value": "..."
}
```

##All

```bash
curl -X GET -v --basic -u "post@example.net:1234" \
         http://localhost:5000/tokens
```
```json
{
    "pager": {
        "next_num": false, 
        "page": 1, 
        "pages": 1, 
        "prev_num": false, 
        "total": 1
    }, 
    "tokens": [
        {
            "expires": null, 
            "key": "master", 
            "value": "..."
        }
    ]
}

```

##Using token auth

```bash
curl -X GET -v --basic -u "tokenkey:unused" http://localhost:5000/marks
```


#Mark

##Add

```bash
curl -X POST -v --basic -u "post@example.net:1234" \
         -d "type=bookmark&title=test&tags=1,2,3&url=http://example.org" \
         http://localhost:5000/mark

or

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

##Get by id

```bash
curl -X GET -v --basic -u "post@example.net:1234" \
         http://localhost:5000/mark/{id}
```
```json
{
    "clicks": 0, 
    "created": "Sun, 22 Mar 2015 18:26:18 -0000", 
    "id": 1, 
    "last_clicked": null, 
    "tags": [
        "1", 
        "2", 
        "3"
    ], 
    "title": "test", 
    "type": "bookmark", 
    "updated": null, 
    "url": "http://example.org"
}
```

##Update

```bash
curl -X PUT -v --basic -u "post@example.net:1234" \
         -d "title=horse" \
         http://localhost:5000/mark/{:id}

or

curl -X PUT -v -H "Content-Type: application/json" \
         --basic -u "post@example23.net:1234" \
         -d '{"title":"horse"}' \
         http://localhost:5000/mark/{:id}
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


##Delete

```bash
not implemented
```

##All

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