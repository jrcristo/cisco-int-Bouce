import netmiko
import getpass

from netmiko import ConnectHandler

IP = input("Give me The IP: ")
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
# config_commands = ['wr mem']
# output = net_connect.send_config_set(config_commands)
# print(output)

print("saving config")
output = net_connect.send_command('wr mem')
print(output)
