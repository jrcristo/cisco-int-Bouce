from netmiko import ConnectHandler

panos = {
    'device_type': 'paloalto_panos',
    'ip': '10.120.142.231',
    'username': 'Read_Only',
    'password': 'S$@!L!nG!12',
}

config_commands = [
    'show system info',
    # 'show system resources', # next command after this will hang
    'show system services',
    # 'show system software status', # next command after this will hang
    'show system state'
]
net_connect = ConnectHandler(**panos)
out = ""
for cmd in config_commands:
    print("Executing %s" % cmd)
    out += "-------------"
    out += net_connect.send_command(cmd)

print(out)

net_connect.disconnect()
