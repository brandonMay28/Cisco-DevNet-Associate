import requests
import json
from pprint import pp, pprint

from requests.sessions import PreparedRequest

router = {
    "host": "sandboxdnac.cisco.com",
    "user": "devnetuser",
    "pass": "Cisco123!",
    "port": "443"
}

auth_url = f"https://{router['host']}/dna/system/api/v1/auth/token"

payload={}

headers = {
  'Content-Type': 'application/json'
}

auth_response = requests.request("POST", auth_url, auth=(router["user"], router["pass"]), headers=headers, data=payload).json()

token = auth_response["Token"]

##################################################################################

url = f"https://{router['host']}/dna/intent/api/v1/client-health"

payload={}

headers = {
  'Content-Type': 'application/json',
  'x-auth-token': token
}

response = requests.request("GET", url, auth=(router["user"], router["pass"]), headers=headers, data=payload).json()

print(f"Client Count: {response['response'][0]['scoreDetail'][0]['clientCount']}")
print(" ")

scores = response['response'][0]['scoreDetail']

for score in scores:
  if score["scoreCategory"]["value"] == "WIRED":
    print("Wired Clients")
    print(f"CLient Count: {score['clientCount']}")
    print(f"Score Value: {score['scoreValue']}")
    print(f"Start Time: {score['starttime']} | End Time: {score['endtime']}")
    print(" ")
    if "scoreList" in score:
      for list in score["scoreList"]:
        print(f"   Value: {list['scoreCategory']['value']}")
        print(f"*" * 30)
      print("=" * 70)
  
  if score["scoreCategory"]["value"] == "WIRELESS":
    print("WIRELESS Clients")
    print(f"CLient Count: {score['clientCount']}")
    print(f"Score Value: {score['scoreValue']}")
    print(f"Start Time: {score['starttime']} | End Time: {score['endtime']}")
    print(" ")
    if "scoreList" in score:
      for list in score["scoreList"]:
        print(f"   Value: {list['scoreCategory']['value']}")
        print(f"*" * 30)
      print("=" * 70)
  
