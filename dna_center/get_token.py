import requests
import json

router = {
    "host": "sandboxdnac.cisco.com",
    "user": "devnetuser",
    "pass": "Cisco123!",
    "port": "443"
}

url = f"https://{router['host']}/dna/system/api/v1/auth/token"

payload={}

headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, auth=(router["user"], router["pass"]), headers=headers, data=payload).json()

token = response["Token"]

print(token)
