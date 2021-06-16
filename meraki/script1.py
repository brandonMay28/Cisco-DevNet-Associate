import requests
import json

######################################## Get a list of oganizations ##################################
api_key = "dad1d34568f7c2d7709c96c3a6ffc4b73dd395be"
org_name = "DevNet Sandbox"
org_id = ""
networks = []

orgs_url = "https://api.meraki.com/api/v0/organizations"

payload={}
headers = {
  'X-Cisco-Meraki-API-Key': api_key
}

orgs_response = requests.request("GET", orgs_url, headers=headers, data=payload).json()

#print(json.dumps(orgs_response, indent=2, sort_keys=True))

######################################## Get specific oganization ##################################


for org in orgs_response:
    if org["name"] == org_name:
        org_id = org["id"]

org_url = f"https://api.meraki.com/api/v0/organizations/{org_id}"    

org_response = requests.request("GET", org_url, headers=headers, data=payload).json()

#print(json.dumps(org_response, indent=2, sort_keys=True))


######################################## Get oganization networks ##################################

nets_url = f"https://api.meraki.com/api/v0/organizations/{org_id}/networks"

nets_response = requests.request("GET",nets_url, headers=headers, data=payload).json()

#print(json.dumps(org_response, indent=2, sort_keys=True))
#print(json.dumps(nets_response, indent=2, sort_keys=True))

print(f"Organzation {org_response['name']} with an id of {org_response['id']} has the following networks below: ")
for net in nets_response:
    networks.append(net["name"])
print(networks)




