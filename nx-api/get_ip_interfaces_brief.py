import requests
import json

username = "admin"
password = "Admin_1234!"

url = "https://sbx-nxos-mgmt.cisco.com:443/ins"

payload = json.dumps({
    "ins_api": {
    "version": "1.0",
    "type": "cli_show",
    "chunk": "0",
    "sid": "sid",
    "input": "show ip int brief",
    "output_format": "json"
  }
})
headers = {
  'Content-Type': 'application/json',
  }

response = requests.request("POST", url, auth=(username, password), headers=headers, data=payload).json()

app_data = response["ins_api"]["outputs"]["output"]["body"]["TABLE_intf"]["ROW_intf"]


for interfaces in app_data:
    print(json.dumps(interfaces["iod"], indent=2, sort_keys=True))
    print(json.dumps(interfaces["intf-name"], indent=2, sort_keys=True))
    print(json.dumps(interfaces["link-state"], indent=2, sort_keys=True))
    print(json.dumps(interfaces["prefix"], indent=2, sort_keys=True))
    print(json.dumps(interfaces["proto-state"], indent=2, sort_keys=True))
    print("=" * 30)
    print(" ")