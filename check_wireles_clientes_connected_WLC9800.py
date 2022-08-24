from netmiko import ConnectHandler
import getpass
import re
import funtions_jose

print('==> script to check clients connected to an specific AP <==')

if __name__ == '__main__':

    ap_name = input("What's the AP name: ")

    try:
        ex = re.match('^EX', ap_name)
        xp = re.match('^XP', ap_name)
        xic = re.match('^XIC', ap_name)

    except AttributeError:
        pass

    try:
        if ex.group():
            isIP = '10.125.71.225'
            print('==> Connecting to EX=Enchanted WLC at' + " " + isIP)
            JC = funtions_jose.connect_wlc(isIP)
            net_connect = ConnectHandler(**JC)
            net_connect.enable()

            # getting data
            output = funtions_jose.get_wlc_9800_clients_connected_by_ap(ap_name, net_connect)
            exit(0)

    except AttributeError:
        pass

    try:
        if xp.group():
            isIP = '10.125.135.225'
            print('==> Connecting to XP=Discovery WLC at' + " " + isIP)
            JC = funtions_jose.connect_wlc(isIP)
            net_connect = ConnectHandler(**JC)
            net_connect.enable()

            # getting data
            output = funtions_jose.get_wlc_9800_clients_connected_by_ap(ap_name, net_connect)
            exit(0)

    except AttributeError:
        pass

    try:
        if xic.group():
            isIP = '10.126.140.125'
            print('==> Connecting to XIC WLC at' + " " + isIP)
            JC = funtions_jose.connect_wlc(isIP)
            net_connect = ConnectHandler(**JC)
            net_connect.enable()

            # getting data
            output = funtions_jose.get_wlc_9800_clients_connected_by_ap(ap_name, net_connect)
            exit(0)

    except AttributeError:
        pass

