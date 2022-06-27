from netmiko import ConnectHandler
import getpass
import re
import funtions_jose

print('==> script to check AP cdp neighbor <==')

if __name__ == '__main__':
    ap_name = input("What's the AP name: ")
    # IP = input("Give me the device IP: ")
    # USERNAME = input("What's the username: ")
    # PASS = input("What's the password: ")
    # PASS = getpass.getpass()

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

            # connecting WLC
            output = funtions_jose.check_ap_cdp_neighbor(ap_name, net_connect)
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

            # connecting WLC
            output = funtions_jose.check_ap_cdp_neighbor(ap_name, net_connect)
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

            # connecting WLC
            output = funtions_jose.check_ap_cdp_neighbor(ap_name, net_connect)
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

            # connecting WLC
            output = funtions_jose.check_ap_cdp_neighbor(ap_name, net_connect)
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

            # connecting WLC
            output = funtions_jose.check_ap_cdp_neighbor(ap_name, net_connect)
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

            # connecting WLC
            output = funtions_jose.check_ap_cdp_neighbor(ap_name, net_connect)
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

            # connecting WLC
            output = funtions_jose.check_ap_cdp_neighbor(ap_name, net_connect)
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

            # connecting WLC
            output = funtions_jose.check_ap_cdp_neighbor(ap_name, net_connect)
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

            # connecting WLC
            output = funtions_jose.check_ap_cdp_neighbor(ap_name, net_connect)
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

            # connecting WLC
            output = funtions_jose.check_ap_cdp_neighbor(ap_name, net_connect)
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

            # connecting WLC
            output = funtions_jose.check_ap_cdp_neighbor(ap_name, net_connect)
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

            # connecting WLC
            output = funtions_jose.check_ap_cdp_neighbor(ap_name, net_connect)
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

            # connecting WLC
            output = funtions_jose.check_ap_cdp_neighbor(ap_name, net_connect)
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

            # connecting WLC
            output = funtions_jose.check_ap_cdp_neighbor(ap_name, net_connect)
            exit(0)

    except AttributeError:
        pass

    else:
        print('exiting')

'''
    # connecting to WLC
    with ConnectHandler(ip=IP,
                        port=22,
                        username=USERNAME,
                        password=PASS,
                        device_type='cisco_wlc_ssh') as ch:

        # getting results
        print("==> Getting CDP neighbor for: ", ap_name)
        output = ch.send_command("show ap cdp neighbors ap-name" + " " + ap_name)
        print('\n')

        if output:
            # filtering CDP switch name
            cdp = re.search(r'(PCL\w+.\d{3}-\w+)|(PCL\w+.\w+)', output)
            # getting nei IP add
            nei_ip_add = re.search(r'IP\sadd.*', output)
            nei_ip = re.search(r'\d.*', nei_ip_add.group())

            # Filtering nei interface
            interface = re.search(r'(Gi.*)|(Te.*)', output)

            # printing results:
            print('The AP cdp neighbor is: ', cdp.group())
            print('The neighbor IP is: ', nei_ip.group())
            print('The neighbor interface is: ', interface.group())

        else:
            print("I couldn't find any neighbor")
'''






