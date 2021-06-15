import requests
import json

router = {
    "host": "sandbox-iosxe-latest-1.cisco.com",
    "user": "developer",
    "pass": "C1sco12345",
    "port": "443"
}

url = f"https://{router['host']}:{router['port']}/restconf/data/ietf-interfaces:interfaces"

payload={}

headers = {
  'Accept': 'application/yang-data+json',
  'Content-Type': 'application/yang-data+json'
}

response = requests.request("GET", url, auth=(router["user"], router["pass"]), headers=headers, data=payload)

print(response.text)
