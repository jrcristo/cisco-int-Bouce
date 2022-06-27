import netmiko
import getpass

from netmiko import ConnectHandler

bgp_route = input("Whats the EIGRP IP|Network: ")
IP = input("Give me the device IP: ")
USERNAME = input("What's the username: ")
# PASS = input("What's the password: ")
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

print("==> Showing command")
output = net_connect.send_command('sh ip eigrp vrf * neighbors | inc' + " " + bgp_route)
print('This is the output: \n', output)
