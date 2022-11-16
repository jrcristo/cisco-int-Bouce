from __future__ import print_function
import re
import requests
import json
from argparse import ArgumentParser

requests.packages.urllib3.disable_warnings()

base_uri = 'https://10.126.100.196/webacs/api/v4/'
user = 'xopsapi'
password = 'Xops@123'
# rest_path = '/data/InventoryDetails'
rest_path = 'data/AccessPoints?name=eq("Cabana_11")'
url = base_uri + rest_path

headers = {'Accept': 'application/json'}
response = requests.get(url, headers=headers, auth=(user, password), verify=False)
# print(response.text)
# print(response.status_code)98745
acdResp = json.loads(response.text)
# print(acdResp)

if acdResp['queryResponse']['@count'] == 1:
    print('=> Device Found it, getting details')

    # capturing device ID
    dev_id = acdResp['queryResponse']['entityId'][0]['$']
    # print('id =', dev_id)

    # showing device details
    # device = 'data/Devices/' + dev_id
    device = 'data/AccessPointDetails/' + dev_id
    url_dev = base_uri + device
    dev_details = requests.get(url_dev, headers=headers, auth=(user, password), verify=False)
    cdpData = json.loads(dev_details.text)
    cdpNeighList = cdpData['queryResponse']['entity'][0]['accessPointDetailsDTO']['cdpNeighbors']['cdpNeighbor']
    i = 0
    for neigh in cdpNeighList:
        i += 1
        # print("Neighbor: ", i)
        print("=> The last known CDP Neighbor name was:", neigh['neighborName'])
        print("=> The last known CDP Neighbor port was:", neigh['neighborPort'])
        print('=> The Last known IP neighbor address was:', neigh['neighborIpAddress']['address'])
        print('=> Switch type is:', neigh['platform'])

else:
    print('=> Device not found it, exiting')
    exit(0)
