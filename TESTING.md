#Routes
Current routes
* [/register](#register) - {POST}
* [/profile](#profile) - {GET, PUT}
* [/token/{:key}](#token) - {GET, POST}
* [/mark/{:id}](#mark) - {GET, POST, PUT, DELETE}
* [/marks/{?:page}](#marks) - {GET}
* [/tags/{?:page}](#tags) - {GET}

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
    "created": "Sun, 22 Mar 2015 18:11:04 -0000",
    "email": "test@example.net",
    "id": 1,
    "username": null
}
```


#Profile

##GET - Profile
```bash
curl -X GET -v --basic -u "post@example.net:1234" \
         http://localhost:5000/profile
```
```json
{
    "created": "Sun, 22 Mar 2015 18:11:04 -0000",
    "email": "test@example.net", 
    "id": 10, 
    "username": null
}
```

##PUT - Profile
```bash
curl -X PUT -v --basic -u "post@example.net:1234" \
         -d "username=horse" \
         http://localhost:5000/profile

or

curl -X PUT -v -H "Content-Type: application/json" \
         --basic -u "post@example23.net:1234" \
         -d '{"username":"horse"}' \
         http://localhost:5000/profile
```
```json
{
    "created": "Sun, 22 Mar 2015 18:11:04 -0000",
    "email": "test@example.net",
    "id": 10,
    "username": "horse"
}
```

#Token

##POST - Token

```bash
curl -X POST -v --basic -u "post@example.net:1234" \
         -d "key=apple" \
         http://localhost:5000/token
```
```json
{
    "expires": "Wed, 25 Mar 2015 06:22:02 -0000",
    "key": "apple",
    "unhashed": "..."
}
```

##Using token auth

```bash
curl -X GET -v --basic -u "tokenkey:unused" http://localhost:5000/marks
```


#Mark

##POST - Mark

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

##GET - Mark

```bash
curl -X GET -v --basic -u "post@example.net:1234" \
         http://localhost:5000/mark/{:id}
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

##PUT - Mark

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

##DELETE - Mark

```bash
curl -X DELETE -v --basic -u "post@example.net:1234" \
         http://localhost:5000/mark/{:id}
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

#Marks

```bash
curl -X GET -v --basic -u "post@example.net:1234" \
         http://localhost:5000/marks{?:page}
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

##Marks - Search

```bash
curl -X GET -v --basic -u "post@example.net:1234" \
         http://localhost:5000/marks/?q=abc&type=bookmark&tag=tag1&sort=clicks

or

curl -X GET --basic -u "post@example.net" \
         -H "Content-type: application/json" \
         -d '{"q": "abc", "type": "bookmark", "tag": "tag1", "sort": "clicks"}' \
         http://localhost:5000/marks
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
            "title": "abc",
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

#Tags

```bash
curl -X GET -v --basic -u "post@example.net:1234" \
        http://localhost:5000/tags/{?:page}
```
```json
{
    "pager": {
        "next_num": false,
        "page": 1,
        "pages": 1,
        "prev_num": false,
        "total": 3
    },
    "tags": [
        {
            "id": 1,
            "title": "tag1"
        },
        {
            "id": 2,
            "title": "tag2"
        },
        {
            "id": 3,
            "title": "tag3"
        }
    ]
}
```
