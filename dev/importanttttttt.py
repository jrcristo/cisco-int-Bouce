from netmiko import ConnectHandler
import funtions_jose
import re

JC = funtions_jose.get_credentials_and_interface()
net_connect = ConnectHandler(**JC)
net_connect.enable()


output = net_connect.send_command('sh ver')
# sn = re.search(r"System Serial Number\s+:\s+(\S+)", output).group(1)
sn = re.findall(r"System Serial Number\s+:\s+(\S+)", output)
print(sn)


'''
def main():
    print '###### STARTING ZTP SCRIPT ######'
    print '\n*** Obtaining serial number of device.. ***'
    serial = get_serial()
    print '*** Setting configuration file variable.. ***'
    config_file = "{}.cfg".format(serial)

    # searching for SN
    for i in sn:
        if
'''


