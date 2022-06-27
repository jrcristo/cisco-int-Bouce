import getpass

from netmiko import ConnectHandler

print("==> Script to show a mac-add behind a port")
interface = input("Whats the interface: ")
IP = input("Give me the switch IP: ")
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

print("==> sending shutdown command")
config_commands = ['int' + " " + interface.upper(), 'sh']
output = net_connect.send_config_set(config_commands)

if "sh" in output:
    print("Interface is in shutdown state\n")
else:
    print("shut command fail\n")

print("==> results after command")
output = net_connect.send_command('show run int' + " " + interface)
print(output)
