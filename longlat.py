#!/usr/bin/python3

import json
import os
import requests
import sys

def halt(reason, code):
  print(reason, file=sys.stderr)
  sys.exit(code)

access_key = os.environ.get("ACCESS_KEY")

try:
  ip_address = sys.argv[1]
except IndexError:
  halt("IP address to lookup not supplied", 1)

if access_key == None or access_key == "undef":
  halt("Environment variable 'ACCESS_KEY' is not defined", 2)

api_base = "https://api.ipstack.com/"

session = requests.session()
# would be nice to check ip address resembles an ipv4 ip address here.
response = session.get(api_base + ip_address + '?access_key=' + access_key)

payload = response.json()

try: 
  if 'success' in payload and payload['success'] == False:
    halt('Error (' +
      str(payload['error']['code']) +') ' +
      payload['error']['type'] + ': ' +
      payload['error']['info'],3)
finally:
  False

if 'latitude' in payload:
  lat = payload['latitude']
else:
  halt("Latitude missing in API repsonse",3)
if 'longitude' in payload:
  long = payload['longitude']
else:
  halt("Longitude missing in API repsonse",3)

halt('Latitude:'+ str(payload['latitude']) + ' Longitude:' + str(payload['longitude']), 0)
