import requests
import json

router = {
    "host": "sandboxapicdc.cisco.com",
    "user": "admin",
    "pass": "ciscopsdt",
    "port": "443"
}

url = f"https://{router['host']}/api/aaaLogin.json"

payload = json.dumps({
  "aaaUser": {
    "attributes": {
      "name": "admin",
      "pwd": "ciscopsdt"
    }
  }
})
headers = {
  'Content-Type': 'application/json'  
}

response = requests.request("POST", url, auth=(router["user"], router["pass"]), headers=headers, data=payload).json()

token = response["imdata"][0]["aaaLogin"]["attributes"]["token"]

print(token)
