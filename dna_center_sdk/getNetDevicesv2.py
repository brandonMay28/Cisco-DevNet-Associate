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

devices = api.devices.get_device_list()

for device in devices.response:
    print(" ")
    pprint(device.id)
    pprint(device.hostname)
    pprint(device.managementIpAddress)
    pprint(device.macAddress)
    pprint(device.family)
    pprint(device.reachabilityStatus)
    pprint(device.series)
    pprint(device.type)
    print("=" * 70)