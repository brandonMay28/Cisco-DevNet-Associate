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

sites = api.sites.get_site()

for site in sites["response"]:
    if "parentId" in site:
        parentId = site["parentId"]
        print(f"Country: {site['additionalInfo'][0]['attributes']['country']}")
        print(f"Address: {site['additionalInfo'][0]['attributes']['address']}")
        print(f"Name: {site['name']}")
        print("=" * 50)
        print(" ")