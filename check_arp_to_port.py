from netmiko import ConnectHandler
import getpass
import re
import funtions_jose

print('==> script to check on which port is an specific mac-add <==')

if __name__ == '__main__':

    yes_option = ['yes', 'y']
    no_option = ['no', 'n']

    mac_acc = str(input("What's the device mac-add: "))

    JC = funtions_jose.get_credentials_and_interface()
    net_connect = ConnectHandler(**JC)
    net_connect.enable()

    funtions_jose.check_mac_add_on_port(mac_acc, net_connect)

