import requests
import json
from pprint import pprint

router = {
    "host": "sbx-nxos-mgmt.cisco.com",
    "port": "443",
    "user": "admin",
    "pass": "Admin_1234!"
}

url = f"https://{router['host']}:{router['port']}/ins"

headers = {
    "Content-Type": "application/json"
}

payload = json.dumps({
  "ins_api": {
    "version": "1.0",
    "type": "cli_show",
    "chunk": "0",
    "sid": "sid",
    "input": "show int Loop99",
    "output_format": "json"
  }
})

response = requests.request("POST", url, auth=(router["user"], router["pass"]), headers=headers, data=payload).json()

#print(response)

################################# Logging Into The API REST #############################################

auth_url = f"https://{router['host']}:{router['port']}/api/aaaLogin.json"

auth_payload = json.dumps({
  "aaaUser": {
    "attributes": {
      "name": router["user"],
      "pwd": router["pass"]
    }
  }
})

auth_headers = {
  'Content-Type': 'application/json',
}

auth_response = requests.request("POST", auth_url, headers=auth_headers, timeout=5, data=auth_payload).json()

token = auth_response["imdata"][0]["aaaLogin"]["attributes"]["token"]

cookies = {}
cookies["APIC-cookie"] = token

interface_state = response["ins_api"]["outputs"]["output"]["body"]["TABLE_interface"]["ROW_interface"]["state"]
interface_name = response["ins_api"]["outputs"]["output"]["body"]["TABLE_interface"]["ROW_interface"]["interface"]
interface_des = response["ins_api"]["outputs"]["output"]["body"]["TABLE_interface"]["ROW_interface"]["desc"]

previous_desc = interface_des

print(interface_name)
print(interface_state)
print(interface_des)

new_desc = f"{interface_des}  || Updated with NX-API"

body = {     
    "l3LbRtdIf": {
        "attributes": {                   
            "descr": new_desc                   
        }
    }
}
    

if interface_state == "up":
    new_url = f"https://{router['host']}/api/node/mo/sys/intf/lb-[lo99].json"
    post_res = requests.request("POST", new_url, data=json.dumps(body), headers=headers, cookies=cookies).json()

    print(post_res)

