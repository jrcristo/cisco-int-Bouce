import netmiko
import getpass

from netmiko import ConnectHandler

bgp_route = input("Whats the BGP IP|Network: ")
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

print("==> showing command")
output = net_connect.send_command('sh ip bgp all summa | inc' + " " + bgp_route)
print('This is the output: \n', output)
