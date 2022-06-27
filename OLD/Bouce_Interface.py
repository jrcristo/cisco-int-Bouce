from getpass import getpass
from netmiko import ConnectHandler
print('==> Script to bounce interfaces <==')
import funtions_jose

IP = input("Give me the switch IP: ")
USERNAME = input("What's the username: ")
PASS = getpass.getpass()

JC = {
    'device_type': 'cisco_ios',
    'ip': IP,
    'username': USERNAME,
    'password': PASS,
}

net_connect = ConnectHandler(**JC)
net_connect.enable()

print("==> show current config")
funtions_jose.show_running_config(funtions_jose.inter)

print("==> rebooting interface")
funtions_jose.bounce_interface(funtions_jose.inter)

print("==> Results after reboot")
funtions_jose.show_results(funtions_jose.inter)
