from netmiko import ConnectHandler
import funtions_jose

print('==> script to check MJ Mimosa <==')

if __name__ == '__main__':

    yes_option = ['yes', 'y']
    no_option = ['no', 'n']

    FZ3 = '10.124.153.74'
    FZ7 = '10.124.153.200'

    # checking IDF3
    JC = funtions_jose.if_credential_connection(FZ3)
    net_connect = ConnectHandler(**JC)
    net_connect.enable()

    # ping the antenna
    print('==> Checking FWD-PortSide')
    fwdPS_ping = net_connect.send_command('ping 10.124.153.91' + " " + 'rep 3\n')

    # validating PING
    if '!' in fwdPS_ping:
        print('=> FWD-PortSide Mimosa is up and reachable')
    else:
        print('=> PING fail')

    ping = input("==> do you want to see ping results?, (Y) to continue ("
                 "N) to cancel:").lower()
    if ping in yes_option:
        print(fwdPS_ping)
    else:
        pass

    print('\n')

    # checking config on port
    fwdPS_port = net_connect.send_command('sh run int Gi2/0/42')
    port = input("==> do you want to see interface config?, (Y) to continue ("
                 "N) to cancel:").lower()
    if port in yes_option:
        print('=> Getting port config')
        print(fwdPS_port, '\n')
    else:
        pass

    # checking mac-add on port
    fwd_mac = net_connect.send_command('sh mac add int Gi2/0/42')
    mac_add = input("==> do you want to see mac-add learned by Gi2/0/42?, (Y) to continue ("
                    "N) to cancel:").lower()
    if mac_add in yes_option:
        print('=> Getting mac-add learned on Gi2/0/42')
        print(fwd_mac)
    else:
        pass
