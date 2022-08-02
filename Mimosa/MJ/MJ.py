from netmiko import ConnectHandler
import funtions_jose
from variables import *

print('==> script to check MJ Mimosa <==')

if __name__ == '__main__':
    yes_option = ['yes', 'y']
    no_option = ['no', 'n']

    FZ3 = '10.124.153.65'
    FZ7 = '10.124.153.193'
    IDF_FZ3 = '10.124.153.74'
    IDF_FZ7 = '10.124.153.200'
    # Antennas
    stbd_fwd = '10.124.153.90'
    stbd_aft = '10.124.153.221'
    ps_fwd = '10.124.153.91'
    ps_aft = '10.124.153.220'

    # asking for antennas to check
    antenna = input(
        "==> copy and paste one of the following options:=> ps_fwd or ps_aft or stbd_fwd or stbd_aft: ").lower()
    if 'ps_fwd' in antenna:
        # connecting device
        JC = funtions_jose.if_credential_connection(IDF_FZ3)
        net_connect = ConnectHandler(**JC)
        net_connect.enable()

        print('=> Checking PortSide Forward')
        ping = net_connect.send_command('ping ' + ps_fwd + " " + 'rep 2\n')
        ping = net_connect.send_command('ping ' + ps_fwd)

        # calling ping function
        funtions_jose.get_ping_info_rates(ping, ps_fwd, net_connect)
        print('*---*-*---*-*---*-*---*')

        # Checking port
        interface = 'Gi2/0/42'
        funtions_jose.show_running_config(interface, net_connect)

    elif 'ps_aft' in antenna:
        # connecting device
        JC = funtions_jose.if_credential_connection(IDF_FZ7)
        net_connect = ConnectHandler(**JC)
        net_connect.enable()

        print('=> Checking PortSide AFT')
        ping = net_connect.send_command('ping ' + ps_aft + " " + 'rep 2\n')
        ping = net_connect.send_command('ping ' + ps_aft)

        # calling ping function
        funtions_jose.get_ping_info_rates(ping, ps_aft, net_connect)
        print('*---*-*---*-*---*-*---*')

        # Checking port
        interface = 'Gi2/0/48'
        funtions_jose.show_running_config(interface, net_connect)

    elif 'stbd_fwd' in antenna:
        # connecting device
        JC = funtions_jose.if_credential_connection(IDF_FZ3)
        net_connect = ConnectHandler(**JC)
        net_connect.enable()

        print('=> Checking Starboard FWD')
        ping = net_connect.send_command('ping ' + stbd_fwd + " " + 'rep 2\n')
        ping = net_connect.send_command('ping ' + stbd_fwd)

        # calling ping function
        funtions_jose.get_ping_info_rates(ping, stbd_fwd, net_connect)
        print('*---*-*---*-*---*-*---*')

        # Checking port
        interface = 'Gi2/0/41'
        funtions_jose.show_running_config(interface, net_connect)

    elif 'stbd_aft' in antenna:
        # connecting device
        JC = funtions_jose.if_credential_connection(IDF_FZ7)
        net_connect = ConnectHandler(**JC)
        net_connect.enable()

        print('=> Checking Starboard AFT')
        ping = net_connect.send_command('ping ' + stbd_aft + " " + 'rep 2\n')
        ping = net_connect.send_command('ping ' + stbd_aft)

        # calling ping function
        funtions_jose.get_ping_info_rates(ping, stbd_aft, net_connect)
        print('*---*-*---*-*---*-*---*')

        # Checking port
        interface = 'Gi2/0/47'
        funtions_jose.show_running_config(interface, net_connect)

