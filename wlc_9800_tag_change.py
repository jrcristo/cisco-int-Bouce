from netmiko import ConnectHandler
import getpass
import re
import funtions_jose

print('==> script to check clients connected to an specific AP <==')

if __name__ == '__main__':

    ap_name = input("What's AP name: ")

    try:
        xic = re.match('^XIC', ap_name)
    #        yp = re.match('^YP', ap_name)
    #        gp = re.match('^GP', ap_name)
    #        rp = re.match('^RP', ap_name)
    #        mj = re.match('^MJ', ap_name)
    #        ap = re.match('^AP', ap_name)
    #        cb = re.match('^CB', ap_name)
    #        co = re.match('^CO', ap_name)
    #        di = re.match('^DI', ap_name)
    #        ep = re.match('^EP', ap_name)
    #        kp = re.match('^KP', ap_name)
    #        ip = re.match('^IP', ap_name)
    #        ru = re.match('^RU', ap_name)
    #        sa = re.match('^SA', ap_name)
    #        pev2 = re.match('^PEV', ap_name)

    except AttributeError:
        pass

    try:
        if xic.group():
            isIP = '10.126.140.125'
            print('==> Connecting to XiC=XiC WLC at' + " " + isIP)
            JC = funtions_jose.connect_wlc(isIP)
            net_connect = ConnectHandler(**JC)
            net_connect.enable()

            # calling function
            funtions_jose.set_wlc_policy_tag_9800(ap_name, net_connect)

            exit(0)

    except AttributeError:
        pass
