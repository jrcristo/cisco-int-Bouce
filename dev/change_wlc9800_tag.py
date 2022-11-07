import netmiko
import re
import getpass

from netmiko import ConnectHandler

vlan_id = input("Whats vlan#: ")
interface = input("Whats the interface: ")
IP = input("Give me the device IP: ")
USERNAME = input("What's the username: ")
# PASS = input("What's the password: ")
PASS = getpass.getpass()
yes_option = ['yes', 'y']
no_option = ['no', 'n']

JC = {
    'device_type': 'cisco_ios',
    'ip': '10.126.140.125',
    'username': 'ccl',
    'password': 'N@v!gaT!nG~',
}
net_connect = ConnectHandler(**JC)
net_connect.enable()

print("==> getting AP mac-add")
ap_name = 'XIC2.0-3rd-Floor-VoD'
output = net_connect.send_command("sh ap name " + ap_name + " " + 'config general')
tag_policy = re.search(r'Policy\sT\w+\sNa\w+\s+.\s(.*)', output).group(1)
mac = re.search(r'MAC\sAdd\w+\s+.\s(\d\S+|\w\S+)', output).group(1)

if 'XIC' in tag_policy:
    print('=> already on the right TAG, no changes committed')

else:
    print('mac-add=>', mac)
    # Changing TAG-Policy
    config_commands = ['config t', 'ap' + " " + mac, 'policy-tag XIC']
    output = net_connect.send_config_set(config_commands)
    if 'Associating policy-tag will cause associated AP to reconnect' in output:
        print('Command executed successfully')
