import getpass
from netmiko import ConnectHandler

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

print("==> Checking current config before change on: " + " " + interface)
output = net_connect.send_command('sh run int' + " " + interface)
print(output)

print("==> checking mac-add learned on: " + " " + interface)
output = net_connect.send_command('sh mac add int' + " " + interface)
print(output)


factory_default = input("==> do you want to factory default the interface?, (Y) to continue (N) to cancel:").lower()
if factory_default in yes_option:
    print("==> Sending default int command")
    config_commands = ['default interface' + " " + interface]
    output = net_connect.send_config_set(config_commands)
    print(output)

    if "set to default configuration" in output:
        print("Factory default completed")
    else:
        print("not able to factory default the interface")

elif factory_default in no_option:
    print("No factory default interface applied")
else:
    print("No factory default interface applied")

print("result after config")
output = net_connect.send_command('sh run int' + " " + interface)
print(output)

print("Saving config")
output = net_connect.send_command('wr mem')
print(output)
