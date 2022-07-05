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

# calling the function
funtions_jose.get_hostname(net_connect)
