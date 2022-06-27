import getpass

from netmiko import ConnectHandler

VLAN = input("Whats the Vlan: ")
interface = input("Whats the interface: ")
IP = input("Give me the device IP: ")
USERNAME = input("What's the username: ")
# PASS = input("What's the password: ")
PASS = getpass.getpass()
yes_option = ['yes', 'y']
no_option = ['no', 'n']

JC = {
    'device_type': 'cisco_ios',
    'ip': IP,
    'username': USERNAME,
    'password': PASS,
}

net_connect = ConnectHandler(**JC)
net_connect.enable()

print("==> checking current config on: " + " " + interface)
output = net_connect.send_command('show run int' + " " + interface)
print(output)

print("==> checking mac-add learned on: " + " " + interface)
output = net_connect.send_command('sh mac add int' + " " + interface)
print(output)

applying_change = input("==> do you want to apply this VLAN change?, (Y) to continue (N) to cancel:").lower()
if applying_change in yes_option:

    print("applying changes")
    config_commands = ['int' + " " + interface, 'swi acc vlan' + " " + VLAN, 'sh', 'no sh']
    output = net_connect.send_config_set(config_commands)
    print(output)

elif applying_change in no_option:
    print("No vlan change applied")
else:
    print("No changes applied")

print("==> results after config")
output = net_connect.send_command('show run int' + " " + interface)
print(output)

print("==> saving config")
output = net_connect.send_command('wr mem')
print(output)
