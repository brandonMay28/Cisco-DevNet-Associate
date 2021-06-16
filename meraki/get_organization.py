import requests
import json

api_key = 'dad1d34568f7c2d7709c96c3a6ffc4b73dd395be'
org_id = "549236"

url = f"https://api.meraki.com/api/v0/organizations/{org_id}"

payload={}
headers = {
  'Accept': '*/*',
  'X-Cisco-Meraki-API-Key': api_key
}

response = requests.request("GET", url, headers=headers, data=payload).json()

print(json.dumps(response, indent=2, sort_keys=True))
