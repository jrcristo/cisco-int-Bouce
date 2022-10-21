from netmiko import ConnectHandler
import getpass
import re
import funtions_jose

print('==> script to check how many clients x SSID <==')

if __name__ == '__main__':

    yes_option = ['yes', 'y']
    no_option = ['no', 'n']

    # client_count = int(input("What's the threshold clients number per AP?: "))

    ship = input("What's the SHIP || Location code: ").upper()
    print("==> Checking one SHIP")

    try:
        ex = re.match('^EX', ship)
        xp = re.match('^XP', ship)
        yp = re.match('^YP', ship)
        gp = re.match('^GP', ship)
        rp = re.match('^RP', ship)
        mj = re.match('^MJ', ship)
        ap = re.match('^AP', ship)
        cb = re.match('^CB', ship)
        co = re.match('^CO', ship)
        di = re.match('^DI', ship)
        ep = re.match('^EP', ship)
        kp = re.match('^KP', ship)
        ip = re.match('^IP', ship)
        ru = re.match('^RU', ship)
        sa = re.match('^SA', ship)
        pev2 = re.match('^PEV', ship)
        test = re.match('^TEST', ship)

    except AttributeError:
        pass

    try:
        if ex.group():
            isIP = '10.125.71.225'
            print('==> Connecting to EX=ENCHANTED WLC at' + " " + isIP)
            JC = funtions_jose.connect_wlc(isIP)
            net_connect = ConnectHandler(**JC)
            net_connect.enable()

            # executing functions
            print('==> DISCOVERY WLC <==')
            wlan_id = funtions_jose.get_wlan_id_wlc(net_connect)
            funtions_jose.get_total_clients_ssid_9800(wlan_id, net_connect)

            exit(0)

    except AttributeError:
        pass

    try:
        if xp.group():
            isIP = '10.125.135.225'
            print('==> Connecting to XP=DISCOVERY WLC at' + " " + isIP)
            JC = funtions_jose.connect_wlc(isIP)
            net_connect = ConnectHandler(**JC)
            net_connect.enable()

            # executing functions
            print('==> DISCOVERY WLC <==')
            wlan_id = funtions_jose.get_wlan_id_wlc(net_connect)
            funtions_jose.get_total_clients_ssid_9800(wlan_id, net_connect)
            exit(0)

    except AttributeError:
        pass

    try:
        if yp.group():
            isIP = '10.125.7.225'
            print('==> Connecting to YP=SKY WLC at' + " " + isIP)
            JC = funtions_jose.connect_wlc(isIP)
            net_connect = ConnectHandler(**JC)
            net_connect.enable()

            # executing function
            print('==> SKY WLC <==')
            wlan_id = funtions_jose.get_wlan_id_wlc(net_connect)
            funtions_jose.get_total_clients_ssid_aireos(wlan_id, net_connect)
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

            # executing function
            wlan_id = funtions_jose.get_wlan_id_wlc(net_connect)
            funtions_jose.get_total_clients_ssid_aireos(wlan_id, net_connect)
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

            # executing function
            wlan_id = funtions_jose.get_wlan_id_wlc(net_connect)
            funtions_jose.get_total_clients_ssid_aireos(wlan_id, net_connect)
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

            # executing function
            wlan_id = funtions_jose.get_wlan_id_wlc(net_connect)
            funtions_jose.get_total_clients_ssid_aireos(wlan_id, net_connect)
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

            # executing function
            wlan_id = funtions_jose.get_wlan_id_wlc(net_connect)
            funtions_jose.get_total_clients_ssid_aireos(wlan_id, net_connect)
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

            # executing function
            wlan_id = funtions_jose.get_wlan_id_wlc(net_connect)
            funtions_jose.get_total_clients_ssid_aireos(wlan_id, net_connect)
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

            # executing function
            wlan_id = funtions_jose.get_wlan_id_wlc(net_connect)
            funtions_jose.get_total_clients_ssid_aireos(wlan_id, net_connect)
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

            # executing function
            wlan_id = funtions_jose.get_wlan_id_wlc(net_connect)
            funtions_jose.get_total_clients_ssid_aireos(wlan_id, net_connect)
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

            # executing function
            wlan_id = funtions_jose.get_wlan_id_wlc(net_connect)
            funtions_jose.get_total_clients_ssid_aireos(wlan_id, net_connect)
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

            # executing function
            wlan_id = funtions_jose.get_wlan_id_wlc(net_connect)
            funtions_jose.get_total_clients_ssid_aireos(wlan_id, net_connect)
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

            # executing function
            wlan_id = funtions_jose.get_wlan_id_wlc(net_connect)
            funtions_jose.get_total_clients_ssid_aireos(wlan_id, net_connect)
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

            # executing function
            wlan_id = funtions_jose.get_wlan_id_wlc(net_connect)
            funtions_jose.get_total_clients_ssid_aireos(wlan_id, net_connect)
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

            # executing function
            wlan_id = funtions_jose.get_wlan_id_wlc(net_connect)
            funtions_jose.get_total_clients_ssid_aireos(wlan_id, net_connect)
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

            # executing function
            wlan_id = funtions_jose.get_wlan_id_wlc(net_connect)
            funtions_jose.get_total_clients_ssid_aireos(wlan_id, net_connect)
            exit(0)

    except AttributeError:
        pass

    try:
        if test.group():
            isIP = '10.126.140.50'
            print('==> Connecting to XiC-Old-WLCat' + " " + isIP)
            JC = funtions_jose.connect_wlc(isIP)
            net_connect = ConnectHandler(**JC)
            net_connect.enable()

            # executing function
            wlan_id = funtions_jose.get_wlan_id_wlc(net_connect)
            funtions_jose.get_total_clients_ssid_aireos(wlan_id, net_connect)
            exit(0)

    except AttributeError:
        pass
