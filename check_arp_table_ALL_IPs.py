import getpass
import re

from netmiko import ConnectHandler

print("==> Script to return all the arp process per vlan")
vlan_id = input("What's VLAN# ")
IP = input("Give me the device IP: ")
USERNAME = input("What's the username: ")
# PASS = input("What's the password: ")
# PASS = getpass.getpass()
PASS = getpass.getpass()

JC = {
    'device_type': 'cisco_ios',
    'ip': IP,
    'username': USERNAME,
    'password': PASS,
}

net_connect = ConnectHandler(**JC)
net_connect.enable()

# output = net_connect.send_command('show ip int brief')
# print(output)
# config_commands = ['int' + " " + interface, 'swi acc vlan' + " " + VLAN, 'sh', 'no sh']
# output = net_connect.send_config_set(config_commands)
# print(output)

output = net_connect.send_command('sh ip arp vlan' + " " + vlan_id)

# result = re.search(r'10\S+', output) ##re.search is just for the first entry
print("==> Filtering the output, only IP address allowed")
result = re.finditer(r'10\.[0-2]{1,3}\S+', output)
for match in result:
    print(match.group())


