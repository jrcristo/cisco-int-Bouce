from netmiko import ConnectHandler

import funtions_jose

print('==> Script to check the DST network (SHIP || OFFICE) <==')

if __name__ == '__main__':
    ip_addr = input('Whats the DST IP?: ')

    if '10.24' in ip_addr or '10.25' in ip_addr or '10.28' in ip_addr or '10.30' in ip_addr:
        print('=> IP provided is used locally, no routing available. exiting')
        exit(0)

    print('=> Running the test from XIC')
    isIP = '10.126.140.3'
    JC = funtions_jose.if_credential_connection(isIP)
    net_connect = ConnectHandler(**JC)
    net_connect.enable()

    # running the tracert from XIC-Core
    tracert = net_connect.send_command('traceroute ' + ip_addr + " " + 'num pro 1 source vlan 610 ttl 1 12 timeout 2',
                                       read_timeout=703)

    if '172.30.124.34' in tracert or '172.30.124.35' in tracert or '172.30.120.34.34' in tracert or '172.30.120.34.35' in tracert:
        print(ip_addr, '=> Belongs to Grand.')
    elif '172.30.124.20' in tracert or '172.30.124.21' in tracert or '172.30.120.20' in tracert or '172.30.120.21' in tracert:
        print(ip_addr, '=> Belongs to Caribbean.')
    elif '172.30.124.22' in tracert or '172.30.124.23' in tracert or '172.30.120.22' in tracert or '172.30.120.23' in tracert:
        print(ip_addr, '=> Belongs to Coral.')
    elif '172.30.124.28' in tracert or '172.30.124.29' in tracert or '172.30.120.28' in tracert or '172.30.120.29' in tracert:
        print(ip_addr, '=> Belongs to Diamond.')
    elif '172.30.124.30' in tracert or '172.30.124.31' in tracert or '172.30.120.30' in tracert or '172.30.120.31' in tracert:
        print(ip_addr, '=> Belongs to Emerald.')
    elif '172.30.124.214' in tracert or '172.30.124.215' in tracert or '172.30.120.214' in tracert or '172.30.120.215' in tracert:
        print(ip_addr, '=> Belongs to Enchanted.')
    elif '172.30.124.82' in tracert or '172.30.124.83' in tracert or '172.30.120.42' in tracert or '172.30.120.43' in tracert:
        print(ip_addr, '=> Belongs to Regal.')
    elif '72.30.229.48' in tracert:
        print(ip_addr, '=> Belongs to iLab/Italy.')
    elif '172.30.124.36' in tracert or '172.30.124.37' in tracert or '172.30.120.6' in tracert or '172.30.120.37' in tracert:
        print(ip_addr, '=> Belongs to Island.')
    elif '172.30.124.24' in tracert or '172.30.124.25' in tracert or '172.30.120.24' in tracert or '172.30.120.25' in tracert:
        print(ip_addr, '=> Belongs to Crown.')
    elif '172.30.124.56' in tracert or '172.30.124.57' in tracert or '172.30.120.56' in tracert or '172.30.120.57' in tracert:
        print(ip_addr, '=> Belongs to Majestic.')
    elif '172.30.124.70' in tracert:
        print(ip_addr, '=> Belongs to PEv2.')
    elif '172.30.12.63' in tracert:
        print(ip_addr, '=> Belongs to PEv21 (4g Cisco Router).')
    elif '172.30.124.71' in tracert:
        print(ip_addr, '=> Belongs to Princess Cays.')
    elif '172.30.124.44' in tracert or '172.30.124.45' in tracert or '172.30.120.44' in tracert or '172.30.120.45' in tracert:
        print(ip_addr, '=> Belongs to Royal.')
    elif '172.30.124.46' in tracert or '172.30.124.47' in tracert or '172.30.120.46' in tracert or '172.30.120.47' in tracert:
        print(ip_addr, '=> Belongs to Ruby.')
    elif '172.30.124.48' in tracert or '172.30.124.49' in tracert or '172.30.120.48' in tracert or '172.30.120.49' in tracert:
        print(ip_addr, '=> Belongs to Sapphire.')
    elif '172.30.124.216' in tracert or '172.30.124.217' in tracert or '172.30.120.216' in tracert or '172.30.120.217' in tracert:
        print(ip_addr, '=> Belongs to Discovery.')
    elif '172.30.124.58' in tracert or '172.30.124.59' in tracert or '172.30.120.58' in tracert or '172.30.120.59' in tracert:
        print(ip_addr, '=> Belongs to Sky.')
    elif '172.30.124.111' in tracert:
        print(ip_addr, '=> Belongs to XIC-2.5.')
    elif '172.30.124.75' in tracert or '172.30.124.76' in tracert:
        print(ip_addr, '=> Belongs to XS.')
    elif '10.16' in tracert:
        print(ip_addr, '=> Belongs to AWS.')
    elif '172.30.124.12' not in tracert:
        print(ip_addr, '=> Belongs to XIC.')

    else:
        print("=> I couldn't find it")
