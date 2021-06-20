import requests
import json
from pprint import pp, pprint

router = {
    "host": "sandboxdnac.cisco.com",
    "user": "devnetuser",
    "pass": "Cisco123!",
    "port": "443"
}

auth_url = f"https://{router['host']}/dna/system/api/v1/auth/token"

payload={}

headers = {
  'Content-Type': 'application/json'
}

auth_response = requests.request("POST", auth_url, auth=(router["user"], router["pass"]), headers=headers, data=payload).json()

token = auth_response["Token"]

##################################################################################

url = f"https://{router['host']}/dna/intent/api/v1/network-device"

payload={}

headers = {
  'Content-Type': 'application/json',
  'x-auth-token': token
}

response = requests.request("GET", url, auth=(router["user"], router["pass"]), headers=headers, data=payload).json()

for device in  response["response"]:
    print(" ")
    print(f"Hostname: {device['hostname']} | Series: {device['series']}")
    print(f"Device Type: {device['type']} | Mac: {device['macAddress']}")
    print(f"Role: {device['role']} | Reachability Status: {device['reachabilityStatus']}")
    print(f"Last Updated Time: {device['lastUpdateTime']} | Last Updated: {device['lastUpdated']}")
    print(f"Serial Number: {device['serialNumber']} | Collection Status: {device['collectionStatus']}")
    print(f"Management Ip Address: {device['managementIpAddress']} | Family: {device['family']}")
    print("=" * 100)
