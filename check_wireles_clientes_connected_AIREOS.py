from netmiko import ConnectHandler
import getpass
import re
import funtions_jose

print('==> script to check wireless client associated with an AP <==')

if __name__ == '__main__':

    yes_option = ['yes', 'y']
    no_option = ['no', 'n']

    ap_name = input("What's the AP name: ")

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

            # sending commands to WLC
            ap_details = input("==> do you want to check the AP details?, (Y) to continue (N) to cancel:").lower()
            if ap_details in yes_option:
                print("==> Getting AP details")
                funtions_jose.wlc_clients_associated_ap_details(ap_name, net_connect)

            else:
                pass
            print('*---*-*---*-*---*-*---*-*---*')
            funtions_jose.wlc_clients_associated(ap_name, net_connect)

            print('*---*-*---*-*---*-*---*-*---*')
            # asking for client details
            client_detail = input("==> do you want to check client details?, (Y) to continue (N) to cancel:").lower()
            if client_detail in yes_option:
                mac_addr = str(input("==> please, copy and paste the mac-add <==: ")).lower()
                print("==> Getting Client details")
                funtions_jose.wlc_aireos_client_details(mac_addr, net_connect)
            else:
                pass
            exit(0)

    except AttributeError:
        pass

    try:
        if gp.group():
            isIP = '10.122.199.226'
            print('==> Connecting to GP=REGAL WLC at' + " " + isIP)
            JC = funtions_jose.connect_wlc(isIP)
            net_connect = ConnectHandler(**JC)
            net_connect.enable()

            # sending commands to WLC
            ap_details = input("==> do you want to check the AP details?, (Y) to continue (N) to cancel:").lower()
            if ap_details in yes_option:
                print("==> Getting AP details")
                funtions_jose.wlc_clients_associated_ap_details(ap_name, net_connect)

            else:
                pass
            print('*---*-*---*-*---*-*---*-*---*')
            funtions_jose.wlc_clients_associated(ap_name, net_connect)

            print('*---*-*---*-*---*-*---*-*---*')
            # asking for client details
            client_detail = input("==> do you want to check client details?, (Y) to continue (N) to cancel:").lower()
            if client_detail in yes_option:
                mac_addr = str(input("==> please, copy and paste the mac-add <==: ")).lower()
                print("==> Getting Client details")
                funtions_jose.wlc_aireos_client_details(mac_addr, net_connect)
            else:
                pass
            exit(0)

    except AttributeError:
        pass

    try:
        if rp.group():
            isIP = '10.123.7.225'
            print('==> Connecting to RP=ROYAL WLC at' + " " + isIP)
            JC = funtions_jose.connect_wlc(isIP)
            net_connect = ConnectHandler(**JC)
            net_connect.enable()

            # sending commands to WLC
            ap_details = input("==> do you want to check the AP details?, (Y) to continue (N) to cancel:").lower()
            if ap_details in yes_option:
                print("==> Getting AP details")
                funtions_jose.wlc_clients_associated_ap_details(ap_name, net_connect)

            else:
                pass
            print('*---*-*---*-*---*-*---*-*---*')
            funtions_jose.wlc_clients_associated(ap_name, net_connect)

            print('*---*-*---*-*---*-*---*-*---*')
            # asking for client details
            client_detail = input("==> do you want to check client details?, (Y) to continue (N) to cancel:").lower()
            if client_detail in yes_option:
                mac_addr = str(input("==> please, copy and paste the mac-add <==: ")).lower()
                print("==> Getting Client details")
                funtions_jose.wlc_aireos_client_details(mac_addr, net_connect)
            else:
                pass
            exit(0)

    except AttributeError:
        pass

    try:
        if mj.group():
            isIP = '10.124.154.225'
            print('==> Connecting to MJ=MAJESTIC WLC at' + " " + isIP)
            JC = funtions_jose.connect_wlc(isIP)
            net_connect = ConnectHandler(**JC)
            net_connect.enable()

            # sending commands to WLC
            ap_details = input("==> do you want to check the AP details?, (Y) to continue (N) to cancel:").lower()
            if ap_details in yes_option:
                print("==> Getting AP details")
                funtions_jose.wlc_clients_associated_ap_details(ap_name, net_connect)

            else:
                pass
            print('*---*-*---*-*---*-*---*-*---*')
            funtions_jose.wlc_clients_associated(ap_name, net_connect)

            print('*---*-*---*-*---*-*---*-*---*')
            # asking for client details
            client_detail = input("==> do you want to check client details?, (Y) to continue (N) to cancel:").lower()
            if client_detail in yes_option:
                mac_addr = str(input("==> please, copy and paste the mac-add <==: ")).lower()
                print("==> Getting Client details")
                funtions_jose.wlc_aireos_client_details(mac_addr, net_connect)
            else:
                pass
            exit(0)

    except AttributeError:
        pass

    try:
        if ap.group():
            isIP = '10.121.199.225'
            print('==> Connecting to AP=GRAND WLC at' + " " + isIP)
            JC = funtions_jose.connect_wlc(isIP)
            net_connect = ConnectHandler(**JC)
            net_connect.enable()

            # sending commands to WLC
            ap_details = input("==> do you want to check the AP details?, (Y) to continue (N) to cancel:").lower()
            if ap_details in yes_option:
                print("==> Getting AP details")
                funtions_jose.wlc_clients_associated_ap_details(ap_name, net_connect)

            else:
                pass
            print('*---*-*---*-*---*-*---*-*---*')
            funtions_jose.wlc_clients_associated(ap_name, net_connect)

            print('*---*-*---*-*---*-*---*-*---*')
            # asking for client details
            client_detail = input("==> do you want to check client details?, (Y) to continue (N) to cancel:").lower()
            if client_detail in yes_option:
                mac_addr = str(input("==> please, copy and paste the mac-add <==: ")).lower()
                print("==> Getting Client details")
                funtions_jose.wlc_aireos_client_details(mac_addr, net_connect)
            else:
                pass
            exit(0)

    except AttributeError:
        pass

    try:
        if cb.group():
            isIP = '10.120.7.225'
            print('==> Connecting to CB=CARIBBEAN WLC at' + " " + isIP)
            JC = funtions_jose.connect_wlc(isIP)
            net_connect = ConnectHandler(**JC)
            net_connect.enable()

            # sending commands to WLC
            ap_details = input("==> do you want to check the AP details?, (Y) to continue (N) to cancel:").lower()
            if ap_details in yes_option:
                print("==> Getting AP details")
                funtions_jose.wlc_clients_associated_ap_details(ap_name, net_connect)

            else:
                pass
            print('*---*-*---*-*---*-*---*-*---*')
            funtions_jose.wlc_clients_associated(ap_name, net_connect)

            print('*---*-*---*-*---*-*---*-*---*')
            # asking for client details
            client_detail = input("==> do you want to check client details?, (Y) to continue (N) to cancel:").lower()
            if client_detail in yes_option:
                mac_addr = str(input("==> please, copy and paste the mac-add <==: ")).lower()
                print("==> Getting Client details")
                funtions_jose.wlc_aireos_client_details(mac_addr, net_connect)
            else:
                pass
            exit(0)

    except AttributeError:
        pass

    try:
        if co.group():
            isIP = '10.120.71.225'
            print('==> Connecting to CO=CORAL WLC at' + " " + isIP)
            JC = funtions_jose.connect_wlc(isIP)
            net_connect = ConnectHandler(**JC)
            net_connect.enable()

            # sending commands to WLC
            ap_details = input("==> do you want to check the AP details?, (Y) to continue (N) to cancel:").lower()
            if ap_details in yes_option:
                print("==> Getting AP details")
                funtions_jose.wlc_clients_associated_ap_details(ap_name, net_connect)

            else:
                pass
            print('*---*-*---*-*---*-*---*-*---*')
            funtions_jose.wlc_clients_associated(ap_name, net_connect)

            print('*---*-*---*-*---*-*---*-*---*')
            # asking for client details
            client_detail = input("==> do you want to check client details?, (Y) to continue (N) to cancel:").lower()
            if client_detail in yes_option:
                mac_addr = str(input("==> please, copy and paste the mac-add <==: ")).lower()
                print("==> Getting Client details")
                funtions_jose.wlc_aireos_client_details(mac_addr, net_connect)
            else:
                pass
            exit(0)

    except AttributeError:
        pass

    try:
        if di.group():
            isIP = '10.121.7.225'
            print('==> Connecting to DI=DIAMOND WLC at' + " " + isIP)
            JC = funtions_jose.connect_wlc(isIP)
            net_connect = ConnectHandler(**JC)
            net_connect.enable()

            # sending commands to WLC
            ap_details = input("==> do you want to check the AP details?, (Y) to continue (N) to cancel:").lower()
            if ap_details in yes_option:
                print("==> Getting AP details")
                funtions_jose.wlc_clients_associated_ap_details(ap_name, net_connect)

            else:
                pass
            print('*---*-*---*-*---*-*---*-*---*')
            funtions_jose.wlc_clients_associated(ap_name, net_connect)

            print('*---*-*---*-*---*-*---*-*---*')
            # asking for client details
            client_detail = input("==> do you want to check client details?, (Y) to continue (N) to cancel:").lower()
            if client_detail in yes_option:
                mac_addr = str(input("==> please, copy and paste the mac-add <==: ")).lower()
                print("==> Getting Client details")
                funtions_jose.wlc_aireos_client_details(mac_addr, net_connect)
            else:
                pass
            exit(0)

    except AttributeError:
        pass

    try:
        if ep.group():
            isIP = '10.121.71.225'
            print('==> Connecting to EP=EMERALD WLC at' + " " + isIP)
            JC = funtions_jose.connect_wlc(isIP)
            net_connect = ConnectHandler(**JC)
            net_connect.enable()

            # sending commands to WLC
            ap_details = input("==> do you want to check the AP details?, (Y) to continue (N) to cancel:").lower()
            if ap_details in yes_option:
                print("==> Getting AP details")
                funtions_jose.wlc_clients_associated_ap_details(ap_name, net_connect)

            else:
                pass
            print('*---*-*---*-*---*-*---*-*---*')
            funtions_jose.wlc_clients_associated(ap_name, net_connect)

            print('*---*-*---*-*---*-*---*-*---*')
            # asking for client details
            client_detail = input("==> do you want to check client details?, (Y) to continue (N) to cancel:").lower()
            if client_detail in yes_option:
                mac_addr = str(input("==> please, copy and paste the mac-add <==: ")).lower()
                print("==> Getting Client details")
                funtions_jose.wlc_aireos_client_details(mac_addr, net_connect)
            else:
                pass
            exit(0)

    except AttributeError:
        pass

    try:
        if kp.group():
            isIP = '10.120.135.225'
            print('==> Connecting to KP=CROWN WLC at' + " " + isIP)
            JC = funtions_jose.connect_wlc(isIP)
            net_connect = ConnectHandler(**JC)
            net_connect.enable()

            # sending commands to WLC
            ap_details = input("==> do you want to check the AP details?, (Y) to continue (N) to cancel:").lower()
            if ap_details in yes_option:
                print("==> Getting AP details")
                funtions_jose.wlc_clients_associated_ap_details(ap_name, net_connect)

            else:
                pass
            print('*---*-*---*-*---*-*---*-*---*')
            funtions_jose.wlc_clients_associated(ap_name, net_connect)

            print('*---*-*---*-*---*-*---*-*---*')
            # asking for client details
            client_detail = input("==> do you want to check client details?, (Y) to continue (N) to cancel:").lower()
            if client_detail in yes_option:
                mac_addr = str(input("==> please, copy and paste the mac-add <==: ")).lower()
                print("==> Getting Client details")
                funtions_jose.wlc_aireos_client_details(mac_addr, net_connect)
            else:
                pass
            exit(0)

    except AttributeError:
        pass

    try:
        if ip.group():
            isIP = '10.122.7.225'
            print('==> Connecting to IP=ISLAND WLC at' + " " + isIP)
            JC = funtions_jose.connect_wlc(isIP)
            net_connect = ConnectHandler(**JC)
            net_connect.enable()

            # sending commands to WLC
            ap_details = input("==> do you want to check the AP details?, (Y) to continue (N) to cancel:").lower()
            if ap_details in yes_option:
                print("==> Getting AP details")
                funtions_jose.wlc_clients_associated_ap_details(ap_name, net_connect)

            else:
                pass
            print('*---*-*---*-*---*-*---*-*---*')
            funtions_jose.wlc_clients_associated(ap_name, net_connect)

            print('*---*-*---*-*---*-*---*-*---*')
            # asking for client details
            client_detail = input("==> do you want to check client details?, (Y) to continue (N) to cancel:").lower()
            if client_detail in yes_option:
                mac_addr = str(input("==> please, copy and paste the mac-add <==: ")).lower()
                print("==> Getting Client details")
                funtions_jose.wlc_aireos_client_details(mac_addr, net_connect)
            else:
                pass
            exit(0)

    except AttributeError:
        pass

    try:
        if ru.group():
            isIP = '10.123.71.225'
            print('==> Connecting to RU=RUBY WLC at' + " " + isIP)
            JC = funtions_jose.connect_wlc(isIP)
            net_connect = ConnectHandler(**JC)
            net_connect.enable()

            # sending commands to WLC
            ap_details = input("==> do you want to check the AP details?, (Y) to continue (N) to cancel:").lower()
            if ap_details in yes_option:
                print("==> Getting AP details")
                funtions_jose.wlc_clients_associated_ap_details(ap_name, net_connect)

            else:
                pass
            print('*---*-*---*-*---*-*---*-*---*')
            funtions_jose.wlc_clients_associated(ap_name, net_connect)

            print('*---*-*---*-*---*-*---*-*---*')
            # asking for client details
            client_detail = input("==> do you want to check client details?, (Y) to continue (N) to cancel:").lower()
            if client_detail in yes_option:
                mac_addr = str(input("==> please, copy and paste the mac-add <==: ")).lower()
                print("==> Getting Client details")
                funtions_jose.wlc_aireos_client_details(mac_addr, net_connect)
            else:
                pass
            exit(0)

    except AttributeError:
        pass

    try:
        if sa.group():
            isIP = '10.123.135.225'
            print('==> Connecting to SA=SAPPHIRE WLC at' + " " + isIP)
            JC = funtions_jose.connect_wlc(isIP)
            net_connect = ConnectHandler(**JC)
            net_connect.enable()

            # sending commands to WLC
            ap_details = input("==> do you want to check the AP details?, (Y) to continue (N) to cancel:").lower()
            if ap_details in yes_option:
                print("==> Getting AP details")
                funtions_jose.wlc_clients_associated_ap_details(ap_name, net_connect)

            else:
                pass
            print('*---*-*---*-*---*-*---*-*---*')
            funtions_jose.wlc_clients_associated(ap_name, net_connect)

            print('*---*-*---*-*---*-*---*-*---*')
            # asking for client details
            client_detail = input("==> do you want to check client details?, (Y) to continue (N) to cancel:").lower()
            if client_detail in yes_option:
                mac_addr = str(input("==> please, copy and paste the mac-add <==: ")).lower()
                print("==> Getting Client details")
                funtions_jose.wlc_aireos_client_details(mac_addr, net_connect)
            else:
                pass
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

            # sending commands to WLC
            ap_details = input("==> do you want to check the AP details?, (Y) to continue (N) to cancel:").lower()
            if ap_details in yes_option:
                print("==> Getting AP details")
                funtions_jose.wlc_clients_associated_ap_details(ap_name, net_connect)

            else:
                pass
            print('*---*-*---*-*---*-*---*-*---*')
            funtions_jose.wlc_clients_associated(ap_name, net_connect)

            print('*---*-*---*-*---*-*---*-*---*')
            # asking for client details
            client_detail = input("==> do you want to check client details?, (Y) to continue (N) to cancel:").lower()
            if client_detail in yes_option:
                mac_addr = str(input("==> please, copy and paste the mac-add <==: ")).lower()
                print("==> Getting Client details")
                funtions_jose.wlc_aireos_client_details(mac_addr, net_connect)
            else:
                pass
            exit(0)

    except AttributeError:
        pass

    print('=> Using statically WLC connector')
    wlc_ip = str(input("==> What's the WLC IP) <==: ")).lower()
    ap = str(input("==> What's the AP name) <==: ")).lower()
    JC = funtions_jose.connect_wlc(wlc_ip)
    net_connect = ConnectHandler(**JC)
    net_connect.enable()

    # connecting WLC
    funtions_jose.get_wlc_ap_facts(ap, net_connect)

    print('exiting')


    # else:

    #    IP = input("Give me the device IP: ")
    #    USERNAME = input("What's the username: ")
    # PASS = input("What's the password: ")
    #    PASS = getpass.getpass()

    '''

    JC = funtions_jose.connect_wlc(isIP=False)
    net_connect = ConnectHandler(**JC)
    net_connect.enable()

    # connecting WLC
    print('global')
    output = funtions_jose.get_wlc_ap_facts(ap_name, net_connect)
    '''
