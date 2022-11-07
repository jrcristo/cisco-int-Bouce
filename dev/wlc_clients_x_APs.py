from netmiko import ConnectHandler
import getpass
import re
import funtions_jose

print('==> script to check clients connected to an specific AP <==')

if __name__ == '__main__':

    ap_name = input("What's site/ship: ").upper()

    # connecting to WLC

    try:
        yp = re.match('^YP', ap_name)
        gp = re.match('^GP', ap_name)
        rp = re.match('^RP', ap_name)
        mj = re.match('^MJ', ap_name)
        ap = re.match('^AP', ap_name)
        cb = re.match('^CB', ap_name)
        co = re.match('^CO', ap_name)
        di = re.match('^DI', ap_name)
        ep = re.match('^EP', ap_name)
        kp = re.match('^KP', ap_name)
        ip = re.match('^IP', ap_name)
        ru = re.match('^RU', ap_name)
        sa = re.match('^SA', ap_name)
        pev2 = re.match('^PEV', ap_name)

    except AttributeError:
        pass

    try:
        if yp.group():
            isIP = '10.125.7.225'
            print('==> Connecting to YP=SKY WLC at' + " " + isIP)
            JC = funtions_jose.connect_wlc(isIP)
            net_connect = ConnectHandler(**JC)
            net_connect.enable()

            # calling function
            funtions_jose.get_wlc_clients_ap(net_connect)
            exit(0)

    except AttributeError:
        pass

    try:
        if pev2.group():
            isIP = '10.5.144.10'
            print('==> Connecting to PEv2=PortEverglades-T2 WLC at' + " " + isIP)
            JC = funtions_jose.connect_wlc(isIP)
            net_connect = ConnectHandler(**JC)
            net_connect.enable()

            # calling function
            funtions_jose.get_wlc_clients_ap(net_connect)

            exit(0)

    except AttributeError:
        pass
