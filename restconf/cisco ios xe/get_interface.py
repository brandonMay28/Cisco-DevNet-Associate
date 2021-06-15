import requests
import json
from pprint import pprint

interface_type_selected = False


while interface_type_selected == False:
    print("Interface Types Options are 1 for gig or 2 for loop")

    interface_type = str(input("Interface Type: "))

    if interface_type == "1":
        interface_type = "GigabitEthernet"
        interface_type_selected == True
        break
    elif interface_type == "2":
        interface_type = "Loopback"
        interface_type_selected == True
        break
    else:
        print("Not a valid option. Please enter correct option.")
        interface_type == ""


interface_num = str(input("Interface Number: "))
    

router = {
    "host": "sandbox-iosxe-latest-1.cisco.com",
    "user": "developer",
    "pass": "C1sco12345",
    "port": "443"
}

url = f"https://{router['host']}:{router['port']}/restconf/data/ietf-interfaces:interfaces/interface={interface_type}{interface_num}"

payload={}

headers = {
  'Accept': 'application/yang-data+json',
  'Content-Type': 'application/yang-data+json'
}

response = requests.request("GET", url, auth=(router["user"], router["pass"]), headers=headers, data=payload)

#print(response.text)

app_data = response.json()

pprint(app_data["ietf-interfaces:interface"]["name"])
pprint(app_data["ietf-interfaces:interface"]["description"])
pprint(app_data["ietf-interfaces:interface"]["enabled"])
if app_data["ietf-interfaces:interface"]["ietf-ip:ipv4"]:
    pprint(app_data["ietf-interfaces:interface"]["ietf-ip:ipv4"]["address"][0]["ip"])
else:
    print("No Ip Address")
