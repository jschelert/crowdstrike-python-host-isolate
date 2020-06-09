import requests
from requests import post, auth, exceptions
import json

#Initial REST API CONNECTION
headers = {
    'accept': 'application/json',
    'Content-Type': 'application/x-www-form-urlencoded',
}

#OAUTH2 API Keys *SECRET*
data = {
  'client_id': 'xxxxxxxxx',
  'client_secret': 'xxxxxxxxx'
}

#Post to CS REST API 
response = requests.post('https://api.crowdstrike.com/oauth2/token', headers=headers, data=data)

#Parses OAuth Response from JSON to Dictionary / List 
x = response.text
y = json.loads(x)

# Defines VAR Y1 for Dictionary List on Access Token (SESSION KEY)
y1 = y["access_token"]

#Defintes VAR Y2 for Token Type for Sessions Key (Bearer)
y2 = y["token_type"]

#Concats two strings with space
y3 = ((y2) + ' ' + (y1))

hostisolate = '["xxxxxxx"]'

headers1 = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
    'authorization': y3
    }

params1 = (
    ("action_name", "contain"),
)


data2 = ('{"action_parameters": [ { "name": "string", "value": "string" } ],' + '"ids":' + hostisolate + '}')

print(data2)

response1 = requests.post('https://api.crowdstrike.com/devices/entities/devices-actions/v2', headers=headers1, params=params1, data=data2)

print(response1.text)
