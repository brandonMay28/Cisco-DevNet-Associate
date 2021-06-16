import requests
import json
from pprint import pprint

router = {
    "host": "sandboxapicdc.cisco.com",
    "user": "admin",
    "pass": "ciscopsdt",
    "port": "443"
}


######################### LOGIN

auth_url = f"https://{router['host']}/api/aaaLogin.json"

auth_payload = json.dumps({
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

auth_response = requests.request("POST", auth_url, auth=(router["user"], router["pass"]), headers=headers, data=auth_payload).json()

token = auth_response["imdata"][0]["aaaLogin"]["attributes"]["token"]

cookies = {}
cookies["APIC-cookie"] = token


######################################## 

tens_url = f"https://{router['host']}/api/node/class/fvTenant.json"

payload={}

headers = {}

tenants = requests.request("GET", tens_url, headers=headers, cookies=cookies, data=payload).json()


for tenant in tenants["imdata"]: 
    if tenant["fvTenant"]["attributes"]["name"] == "mgmt":   
        ten_name = tenant["fvTenant"]["attributes"]["name"]
    
############################################################# Update Tenant Description

url = f"https://{router['host']}/api/node/mo/uni/tn-{ten_name}.json"

new_desc = str(input("Enter Description: "))

body = json.dumps({
  "imdata": [
    {
      "fvTenant": {
        "attributes": {
          "descr": new_desc
        }
      }
    }
  ]
})

response = requests.request("POST", url, headers=headers, cookies=cookies, data=body)

tenants = requests.request("GET", tens_url, headers=headers, cookies=cookies, data=payload).json()


for tenant in tenants["imdata"]: 
    if tenant["fvTenant"]["attributes"]["name"] == ten_name:   
        print(tenant["fvTenant"]["attributes"]["name"])
        print(tenant["fvTenant"]["attributes"]["descr"])
