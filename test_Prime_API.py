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

headr = {'Accept': 'application/json'}
response = requests.request('GET', url, auth=(user, password), verify=False)
# print(response.text)
# print(response.status_code)

if 'count="1"' in response.text:
    print('=> Device Found it, getting details')

    # capturing device ID
    dev_id = re.search(r'(\w+).\/entityId', response.text).group(1)
    print('id =', dev_id)

    # showing device details
    # device = 'data/Devices/' + dev_id
    device = 'data/AccessPointDetails/' + dev_id
    url_dev = base_uri + device
    dev_details = requests.request('GET', url_dev, auth=(user, password), verify=False)
    json_data = json.load(dev_details.text)
    print("This is response data: ", json_data)
    print(dev_details.text)


else:
    print('=> Device not found it, exiting')
    exit(0)
