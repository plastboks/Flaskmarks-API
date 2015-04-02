#Output

### => Registering new user
```json
{
    "created": "Wed, 01 Apr 2015 18:32:09 -0000", 
    "email": "f816903 ... 4ae1e1@example.net", 
    "id": 9, 
    "username": null
}
```

### => Create new token
```json
{
    "expires": "Sat, 04 Apr 2015 21:40:30 -0000", 
    "key": "master", 
    "unhashed": "eyJh ... a_o"
}
```

### => Fetch profile
```json
{
    "created": "Wed, 01 Apr 2015 18:32:09 -0000", 
    "email": "f816903 ... 4ae1e1@example.net", 
    "id": 9, 
    "username": null
}
```

### => Setting username
```json
{
    "created": "Wed, 01 Apr 2015 18:32:09 -0000", 
    "email": "f816903 ... 4ae1e1@example.net", 
    "id": 9, 
    "username": "14c9f103-3390-4f32-b582-6c6319352f3f"
}
```

### => Create new mark
```json
{
    "clicks": 0, 
    "created": "Thu, 02 Apr 2015 09:40:30 -0000", 
    "id": 9, 
    "last_clicked": null, 
    "tags": [
        "tag1", 
        "tag2", 
        "tag3"
    ], 
    "title": "test", 
    "type": "bookmark", 
    "updated": null, 
    "url": "http://example.org"
}
```

### => Update mark
```json
{
    "clicks": 1, 
    "created": "Thu, 02 Apr 2015 09:40:30 -0000", 
    "id": 9, 
    "last_clicked": "Thu, 02 Apr 2015 09:40:30 -0000", 
    "tags": [
        "tag1", 
        "tag2", 
        "tag3"
    ], 
    "title": "updated title", 
    "type": "bookmark", 
    "updated": "Thu, 02 Apr 2015 09:40:30 -0000", 
    "url": "http://example.org"
}
```

### => Get all marks
```json
{
    "marks": [
        {
            "clicks": 1, 
            "created": "Thu, 02 Apr 2015 09:40:30 -0000", 
            "id": 9, 
            "last_clicked": "Thu, 02 Apr 2015 09:40:30 -0000", 
            "tags": [
                "tag1", 
                "tag2", 
                "tag3"
            ], 
            "title": "updated title", 
            "type": "bookmark", 
            "updated": "Thu, 02 Apr 2015 09:40:30 -0000", 
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
