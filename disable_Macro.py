import netmiko
import getpass

from netmiko import ConnectHandler

interface = input("Whats the interface: ")
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

print("==> sending command")
config_commands = ['int' + " " + interface, 'no macro auto proc']
output = net_connect.send_config_set(config_commands)
print(output)

print("==> results after change")
output = net_connect.send_command('show run int' + " " + interface)
print(output)

print("==> saving config")
output = net_connect.send_command('wr mem')
print(output)