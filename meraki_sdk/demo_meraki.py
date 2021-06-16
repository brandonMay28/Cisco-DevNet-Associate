from os import name
import meraki
import json
from pprint import pprint

api_key = "dad1d34568f7c2d7709c96c3a6ffc4b73dd395be"

dashboard = meraki.DashboardAPI(api_key)

organizations = dashboard.organizations.getOrganizations()

for org in organizations:
    if org["name"] == "DevNet Sandbox":
        org_id = org["id"]

networks = dashboard.organizations.getOrganizationNetworks(org_id)

for net in networks:
    if net["name"] == "DevNet Sandbox ALWAYS ON":
        net_name = net["name"]
        net_id = net["id"]

net_devices = dashboard.networks.getNetworkDevices(net_id)

for device in net_devices:
    print(" ")
    pprint(device["networkId"])
    if "name" in device:
        pprint(device["name"])
    if "address" in device:
        if device["address"]:            
            pprint(device["address"])
    if "serial" in device:
        if device["serial"]:            
            pprint(device["serial"])
    if "mac" in device:
        if device["mac"]:            
            pprint(device["mac"])
    
    print("=" * 40)
