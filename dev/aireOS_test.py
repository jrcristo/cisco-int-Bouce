from netmiko import ConnectHandler
import getpass
import re
import funtions_jose

print('==> script to check clients connected to an specific AP <==')

if __name__ == '__main__':

    ap_name = input("What's the AP name: ")

    try:
        mj = re.match('^MJ', ap_name)
        xp = re.match('^XP', ap_name)

    except AttributeError:
        pass

    try:
        if mj.group():
            isIP = '10.124.154.225'
            print('==> Connecting to MJ=MAJESTIC WLC at' + " " + isIP)
            JC = funtions_jose.connect_wlc(isIP)
            net_connect = ConnectHandler(**JC)
            net_connect.enable()

            # getting data
            output = funtions_jose.get_wlc_airos_clients_connected_by_ap(ap_name, net_connect)
            exit(0)

    except AttributeError:
        pass
