#!/bin/python
#
# simple restful client tester for the API application.
#

import requests
import json
import uuid


base_url = 'http://localhost:5000/'
user_name = 'test'
user_email = str(uuid.uuid4()) + "@example.net"
user_pass = '1234'

# register new user
print('=> Registering new user')
register = requests.post(base_url + 'register',
                         params={'user': user_name,
                                 'email': user_email,
                                 'password': user_pass})
print(register.text)

# creating new token
print('=> Create new token')
token_request = requests.post(base_url + 'token',
                              auth=(user_email, user_pass),
                              params={'key': 'master'})
print(token_request.text)

# get token for newly registered user.
token = token_request.json().get('unhashed')

# get profile
print('=> Fetch profile')
profile_request = requests.get(base_url + 'profile',
                               auth=(token, 'unused'))
print(profile_request.text)

# set username
print('=> Setting username')
profile_username_request = requests.put(base_url + 'profile',
                                        auth=(token, 'unused'),
                                        params={'username': str(uuid.uuid4())})
print(profile_username_request.text)

# create mark
print('=> Create new mark')
mark_payload = {'type': 'bookmark',
                'title': 'test',
                'tags': 'tag1,tag2,tag3',
                'url': 'http://example.org'
                }
new_mark = requests.post(base_url + 'mark',
                         auth=(token, 'unused'),
                         params=mark_payload)
print(new_mark.text)

# get new mark id
mark_id = str(new_mark.json().get('id'))

# update mark
print('=> Update mark')
update_mark = requests.put(base_url + 'mark/' + mark_id,
                           auth=(token, 'unused'),
                           params={'title': 'updated title'})
print(update_mark.text)

# get all marks
print('=> Get all marks')
marks = requests.get(base_url + 'marks',
                     auth=(token, 'unused'))

print(marks.text)
