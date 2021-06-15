import requests
import json
from pprint import pprint

url = "https://sbx-nxos-mgmt.cisco.com/api/aaaLogin.json"

payload = json.dumps({
  "aaaUser": {
    "attributes": {
      "name": "admin",
      "pwd": "Admin_1234!"
    }
  }
})

headers = {
  'Content-Type': 'application/json',
}

auth_response = requests.request("POST", url, headers=headers, data=payload).json()

#pprint(response.text)
token = auth_response["imdata"][0]["aaaLogin"]["attributes"]["token"]

#pprint(token)
cookies = {}
cookies["APIC-cookie"] = token



url = "https://sbx-nxos-mgmt.cisco.com/api/node/mo/sys/bd.json?query-target=children&"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload, cookies=cookies).json()

pprint(json.dumps(response, indent=2, sort_keys=True))