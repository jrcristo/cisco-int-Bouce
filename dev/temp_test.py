from netmiko import ConnectHandler
import getpass
import re
import funtions_jose

print('==> script to check if an AP is joined WLC <==')

if __name__ == '__main__':

    # connecting to device
    JC = funtions_jose.get_credentials_and_interface()
    net_connect = ConnectHandler(**JC)
    net_connect.enable()

    # getting hostname
    funtions_jose.get_hostname_only(net_connect)

    # getting stack-wise size
    funtions_jose.get_stackwise_size(net_connect)

