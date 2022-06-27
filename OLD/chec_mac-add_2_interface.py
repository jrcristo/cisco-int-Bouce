import getpass
import re
from netmiko import ConnectHandler

print("==> Script to check on which port is the mac-add provided")
mac = input("Whats the mac address: ")
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
output = net_connect.send_command('sh mac add | inc' + " " + mac)

print("==> Filtering the output, only IP address allowed")
result = re.search(r'Gi[1-6]/[0-1]/\d+', output)  #re.search is just for the first entry
# result = re.finditer(r'10\.[0-2]{1,3}\S+', output)
print('==> The requested mac is behind the following interface: ', result.group())
