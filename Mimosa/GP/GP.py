from netmiko import ConnectHandler
import funtions_jose
from variables import *

print('==> script to check MJ Mimosa <==')

if __name__ == '__main__':

    yes_option = ['yes', 'y']
    no_option = ['no', 'n']

    # APs
    APS = ['c4b2.39e5.a742', '4ce1.7557.76ba', '286f.7fcf.641c']

    FZ1 = '10.122.198.1'
    FZ7 = '10.122.198.193'
    IDF_FZ1 = '10.122.198.9'
    IDF_FZ7 = '10.122.198.201'

    # Antennas
    stbd_fwd = '10.122.198.17'
    stbd_aft = '10.122.198.219'
    ps_fwd = '10.122.198.15'
    ps_aft = '10.122.198.220'

    up_ap = 0

    # Displaying info for AP
    print('=> Total #s of APs are =', len(APS))

    # Connecting to WLC
    isIP = '10.122.199.226'
    print('==> Connecting to GP=REGAL WLC at' + " " + isIP)
    JC = funtions_jose.connect_wlc(isIP)
    net_connect = ConnectHandler(**JC)
    net_connect.enable()

    for j in APS:
        try:
            if funtions_jose.get_wlc_mimosa_check(j, net_connect)[0]:
                name = funtions_jose.get_wlc_mimosa_check(j, net_connect)[0]
                print('==> AP', name, ' with mac-add ', j, ' is joined WLC')
                print('=> AP name =', name)
            if funtions_jose.get_wlc_mimosa_check(j, net_connect)[1]:
                ip = funtions_jose.get_wlc_mimosa_check(j, net_connect)[1]
                print('=> AP IP =', ip)
                up_ap = ip
            if funtions_jose.get_wlc_mimosa_check(j, net_connect)[2]:
                group = funtions_jose.get_wlc_mimosa_check(j, net_connect)[2]
                print('=> AP group =', group)
            print('*---*-*---*-*---*-*---*')

        except TypeError:
            pass

    # checking rtt time from FZ to shore ( AP Terminal)
    # print(up_ap)
    if up_ap:
        print('=> Checking RTT time from ship to shore')
        # Connecting to FZ SW
        JC = funtions_jose.if_credential_connection(FZ1)
        net_connect = ConnectHandler(**JC)
        net_connect.enable()

        test = net_connect.send_command('sh ver')
        ping = net_connect.send_command('ping ' + up_ap + " " + 'rep 2\n')
        ping = net_connect.send_command('ping ' + up_ap)
        # calling ping function
        funtions_jose.get_ping_info_rates(ping, up_ap, net_connect)
        print('*---*-*---*-*---*-*---*')

    # asking for antennas to check
    antenna = input(
        "==> copy and paste one of the following options:=> ps_fwd or ps_aft or stbd_fwd or stbd_aft: ").lower()
    if 'ps_fwd' in antenna:
        # connecting device
        JC = funtions_jose.if_credential_connection(IDF_FZ1)
        net_connect = ConnectHandler(**JC)
        net_connect.enable()

        print('=> Checking PortSide Forward Antenna')
        ping = net_connect.send_command('ping ' + ps_fwd + " " + 'rep 2\n')
        ping = net_connect.send_command('ping ' + ps_fwd)

        # calling ping function
        funtions_jose.get_ping_info_rates(ping, ps_fwd, net_connect)
        print('*---*-*---*-*---*-*---*')

        # Checking port
        interface = 'Gig5/0/48'
        funtions_jose.show_running_config(interface, net_connect)

    elif 'ps_aft' in antenna:
        # connecting device
        JC = funtions_jose.if_credential_connection(IDF_FZ7)
        net_connect = ConnectHandler(**JC)
        net_connect.enable()

        print('=> Checking PortSide AFT Antenna')
        ping = net_connect.send_command('ping ' + ps_aft + " " + 'rep 2\n')
        ping = net_connect.send_command('ping ' + ps_aft)

        # calling ping function
        funtions_jose.get_ping_info_rates(ping, ps_aft, net_connect)
        print('*---*-*---*-*---*-*---*')

        # Checking port
        interface = 'Gig3/0/48'
        funtions_jose.show_running_config(interface, net_connect)

    elif 'stbd_fwd' in antenna:
        # connecting device
        JC = funtions_jose.if_credential_connection(IDF_FZ1)
        net_connect = ConnectHandler(**JC)
        net_connect.enable()

        print('=> Checking Starboard FWD Antenna')
        ping = net_connect.send_command('ping ' + stbd_fwd + " " + 'rep 2\n')
        ping = net_connect.send_command('ping ' + stbd_fwd)

        # calling ping function
        funtions_jose.get_ping_info_rates(ping, stbd_fwd, net_connect)
        print('*---*-*---*-*---*-*---*')

        # Checking port
        interface = 'Gig5/0/47'
        funtions_jose.show_running_config(interface, net_connect)

    elif 'stbd_aft' in antenna:
        # connecting device
        JC = funtions_jose.if_credential_connection(IDF_FZ7)
        net_connect = ConnectHandler(**JC)
        net_connect.enable()

        print('=> Checking Starboard AFT Antenna')
        ping = net_connect.send_command('ping ' + stbd_aft + " " + 'rep 2\n')
        ping = net_connect.send_command('ping ' + stbd_aft)

        # calling ping function
        funtions_jose.get_ping_info_rates(ping, stbd_aft, net_connect)
        print('*---*-*---*-*---*-*---*')

        # Checking port
        interface = 'Gig3/0/47'
        funtions_jose.show_running_config(interface, net_connect)
