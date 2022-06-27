import getpass
import re

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

print("==> Current config on interface")
output = net_connect.send_command('sh run int' + " " + interface)
print(output)

print("==> checking mac-add learned on: " + " " + interface)
output = net_connect.send_command('sh mac add int' + " " + interface)
print(output)

factory_default = input("==> do you want to factory default the interface?, (Y) to continue (N) to cancel:").lower()
if factory_default in yes_option:
    config_commands = ['default interface' + " " + interface]
    output = net_connect.send_config_set(config_commands)

    if "set to default configuration" in output:
        print("Factory default completed")
    else:
        print("not able to factory default the interface")

elif factory_default in no_option:
    print("No factory default interface applied")
else:
    print("No factory default interface applied")

validation = input("==> Check the current config on interface, if oK, (Y) to continue (N) to cancel:").lower()

# validate input, check current config and Y to continue
if validation in yes_option:
    config_commands = ['int' + " " + interface, 'desc [RDR] MED-READER', 'spanning-tree portfast',
                       'spanning-tree bpduguard en', 'sw mod acc', 'no macro auto proc', 'sw acc vlan 1310',
                       'power inline static max 30000']
    output = net_connect.send_config_set(config_commands)
    print(output)

    print('==> Bouncing the interface\n')
    config_commands = ['int' + " " + interface, 'sh', 'no shu']
    output = net_connect.send_config_set(config_commands)

    if "no sh" in output:
        print("Interface was Rebooted\n")
    else:
        print("int wasn't rebooted\n")

    print("==> Result after config")
    output1 = net_connect.send_command('show run int' + " " + interface)
    print(output1)

    print("==> saving config")
    output2 = net_connect.send_command('wr mem')
    print(output2)

elif validation in no_option:
    print("NO changes committed --adios--")

else:
    print("No changes were made.\nExiting, --BYE--")
