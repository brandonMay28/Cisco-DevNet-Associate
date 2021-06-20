from dnacentersdk import DNACenterAPI
from pprint import pprint

router = {
    "host": "sandboxdnac.cisco.com",
    "user": "devnetuser",
    "pass": "Cisco123!",
    "port": "443"
}

api = DNACenterAPI(username=router["user"], password=router["pass"],
 base_url=f'https://{router["host"]}:{router["port"]}', version='2.2.1')

foundDevice = False
dev_hostname = str(input("Hostname of Device: "))

devices = api.devices.get_device_list()

for device in devices["response"]:
    if device["hostname"] == dev_hostname:
        foundDevice = True
        dev_id = device["id"]    
    

if foundDevice == True:
    theDevice = api.devices.get_device_by_id(dev_id)
    dev = theDevice["response"]
    print(" ")
    pprint(dev["id"])
    pprint(dev["hostname"])
    pprint(dev["managementIpAddress"])
    pprint(dev["macAddress"])
    pprint(dev["family"])
    pprint(dev["reachabilityStatus"])
    pprint(dev["series"])
    pprint(dev["type"])
    print("=" * 70)
else:
    print(f"Could not find a device with the name {dev_hostname}")