from netmiko import ConnectHandler
import funtions_jose

print('==> script to check XP Mimosa <==')

if __name__ == '__main__':

    yes_option = ['yes', 'y']
    no_option = ['no', 'n']

    # FZ2 = '10.125.134.41'
    FZ7 = '10.125.134.200'

    # checking IDF7
    JC = funtions_jose.if_credential_connection(FZ7)
    net_connect = ConnectHandler(**JC)
    net_connect.enable()

    # ping the antenna
    print('==> Checking AFT_STBD')
    fwdPS_ping = net_connect.send_command('ping 10.125.134.221' + " " + 'rep 3')
    print('######################################')

    # validating PING
    if '!' in fwdPS_ping:
        print('=> AFT_STBD Mimosa is up and reachable')
    else:
        print('=> PING fail')

    ping = input("==> do you want to see ping results?, (Y) to continue ("
                 "N) to cancel:").lower()
    if ping in yes_option:
        print(fwdPS_ping)
    else:
        pass
    print('######################################')

    # checking config on port
    fwdPS_port = net_connect.send_command('sh run int Gi4/0/34')
    port = input("==> do you want to see interface config?, (Y) to continue ("
                 "N) to cancel:").lower()
    if port in yes_option:
        print('=> Getting port config')
        print(fwdPS_port)
    else:
        pass
    print('######################################')

    # checking mac-add on port
    fwd_mac = net_connect.send_command('sh mac add int Gi4/0/34')
    mac_add = input("==> do you want to see mac-add learned by Gi4/0/34?, (Y) to continue ("
                    "N) to cancel:").lower()
    if mac_add in yes_option:
        print('=> Getting mac-add learned on Gi4/0/34')
        print(fwd_mac)
    else:
        pass
