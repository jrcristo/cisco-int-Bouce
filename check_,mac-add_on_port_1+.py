from netmiko import ConnectHandler
import funtions_jose

print('==> Script to check the port of a mac-address <==')

if __name__ == '__main__':
    #    mac = []
    mac = input('Whats the mac-add?: ')

    JC = funtions_jose.get_credentials_and_interface()
    net_connect = ConnectHandler(**JC)
    net_connect.enable()

    # checking the mac
    funtions_jose.check_mac_add_interface_dst(mac, net_connect)
