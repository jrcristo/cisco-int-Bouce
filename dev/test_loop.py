from netmiko import ConnectHandler
import getpass
import os
import re

# location = '/home/venkat/Documents/SDN_bckup_Cfg/'
location = '/home/jose/'
# host = input("Enter Hostname: ")
username = input("Enter Username: ")
password = getpass.getpass()
user_cmd = input("Enter command: ")

with open("Hosts.txt", 'r') as hostsfile:
    for line in hostsfile:
        hostline = line.strip()
        cisco = {
            'device_type': 'cisco_ios',
            'host': hostline,
            'username': username,
            'password': password,
            'secret': 'admin',
        }
        net_connect = ConnectHandler(**cisco)
        net_connect.enable()
        output = net_connect.send_command(user_cmd)
        output_hostname = net_connect.send_command('sh ver')
        hostname = re.search(r'^PCL\w+.\w+.\w+', output_hostname)
        print(hostname)
        print(output)
        print('*---*---*---*---*---*')

'''     outputfile = os.path.join(location, hostline +".txt")
        with open(outputfile, 'w') as result:
            x = result.write(output)
            print(x)
'''