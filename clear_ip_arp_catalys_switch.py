from netmiko import ConnectHandler
import getpass
import re
import funtions_jose

print('==> script clear IP arp <==')

if __name__ == '__main__':

    # vlan = input("What's the vlan: ")

    # connecting to the device
    JC = funtions_jose.get_credentials_and_interface()
    net_connect = ConnectHandler(**JC)
    net_connect.enable()

    # executing the loop
    i = 2
    while i <= 254:
        ip_arp_clean = net_connect.send_command("clear ip arp 10.5.144." + str(i))
        print('Executing =>', "clear ip arp 10.5.144." + str(i))
        i += 1



