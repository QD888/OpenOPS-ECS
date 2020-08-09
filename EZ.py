# OpenOPS - ECS Object Storage, Dell EMC ECS Object Storage Monitor
# ECS: ECS U400, Dell EMC Object storage
# ECS Version: 3.4.0.3
# Programe: Python 3.8
# Stage: prototype
# Author: QD888
# Tested: 9th Aug. 2020


# Import libraries
import requests
from requests.auth import HTTPBasicAuth
import json
import urllib
from urllib.parse import urlencode
from urllib.parse import quote
import http.cookies

# Set up endpoint and authentication credentials
endpoint = 'https://IP address:4443'


# Prepare authentication, create a session
username = 'username'
password = 'password'
auth = HTTPBasicAuth(username, password)

api = '/login'
url = endpoint + api
headers = {
    'Accept': "application/json",
    'Content-Type': "application/json",
    'Accept-Language': 'en-US',
}
response = requests.get(url, headers=headers, auth=auth, verify=False)
print(response.headers)

# Get authentication token
token = response.headers['x-sds-auth-token']
print(token)



# Get response with token, example: Alerts
api = '/vdc/alerts/latest'
url = endpoint + api
headers = {
    'Accept': "application/json",
    'Content-Type': "application/json",
    'Accept-Language': 'en-US',
	'X-SDS-AUTH-TOKEN': token
}
resAlerts = requests.get(url, headers=headers, verify=False)
print(resAlerts.text)


# Get response, Example: Capacity
api = '/object/capacity'
url = endpoint + api
resCap = requests.get(url, headers=headers, verify=False)
print(resCap.text)


# Get response, Example: NFS exports summary
api = '/object/nfs/exports'
url = endpoint + api
resNFS = requests.get(url, headers=headers, verify=False)
print(resNFS.text)


# Get response, Example: namespaces
api = '/object/namespaces'
url = endpoint + api
resNspace = requests.get(url, headers=headers, verify=False)
print(resNspace.text)


# Get response, example: users
api = '/object/users'
url = endpoint + api
resUsers = requests.get(url, headers=headers, verify=False)
print(resUsers.text)

