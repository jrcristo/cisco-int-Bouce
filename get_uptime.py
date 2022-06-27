from netmiko import ConnectHandler
import funtions_jose
import re

JC = funtions_jose.get_credentials_and_interface()
net_connect = ConnectHandler(**JC)
net_connect.enable()


# output = net_connect.send_command('show ip int brief')
# print(output)
# config_commands = ['int' + " " + interface, 'swi acc vlan' + " " + VLAN, 'sh', 'no sh']
# output = net_connect.send_config_set(config_commands)
# print(output)

# validating if nexus
output = net_connect.send_command('sh ver | inc Nexus')
if output:
    print('==> Nexus Device Detected <==')
    nexus = net_connect.send_command('sh system uptime')
    # getting hostname
    nexus_hostname = net_connect.send_command('sh run | inc hostname')
    hostname = re.search(r'PCL.*', nexus_hostname)
    print(nexus, hostname.group())

else:
    print('==> IOS Device Detected <==')
    output = net_connect.send_command('sh ver | inc uptime|Uptime|Last')
    print(output)
