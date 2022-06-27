from netmiko import ConnectHandler
import funtions_jose
import re

# getting time
date = funtions_jose.get_time_date()
print(date[1])

print('==> script to check total TCN occurrences on all VLANS <==')

if __name__ == '__main__':

    JC = funtions_jose.get_credentials_and_interface()
    net_connect = ConnectHandler(**JC)
    net_connect.enable()

    # checking if Nexus or IOS
    device_os = net_connect.send_command('sh ver | inc Nexus')

    if 'Nexus' in device_os:
        print('==> Nexus Device detected')
        nx_os = net_connect.send_command('show spanning-tree detail | in exec|changes|from')
        print(nx_os)

    else:
        print('==> IOS Device Detected')
        # getting TCP TCN results
        int_up = net_connect.send_command('show spanning-tree detail | in ieee|from|occur|is exec')
        print(int_up)
        exit(0)

