from netmiko import ConnectHandler
import re
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

    # getting all the tunnels IP
    tunnels_ip = re.findall(r'172\.30\.124\.\d{1,3}|172\.30\.120\.\d{1,3}|10\.16\.\d{1,3}\.\d{1,3}', tracert)
    # for match in tunnels_ip:
    #    print(match)

    # XiC Networks
    if not tunnels_ip:
        print(ip_addr, '=> Belongs to XIC.')
    elif tunnels_ip:
        for j in tunnels_ip:
            if j == '172.30.124.34' or j == '172.30.124.35' or j == '172.30.120.34.34' or j == '172.30.120.35':
                print(ip_addr, '=> Belongs to Grand.')
            elif j == '172.30.124.20' or j == '172.30.124.21' or j == '172.30.120.20' or j == '172.30.120.21':
                print(ip_addr, '=> Belongs to Caribbean.')
            elif j == '172.30.124.22' or j == '172.30.124.23' or j == '172.30.120.22' or j == '172.30.120.23':
                print(ip_addr, '=> Belongs to Coral.')
            elif j == '172.30.124.28' or j == '172.30.124.29' or j == '172.30.120.28' or j == '172.30.120.29':
                print(ip_addr, '=> Belongs to Diamond.')
            elif j == '172.30.124.30' or j == '172.30.124.31' or j == '172.30.120.30' or j == '172.30.120.31':
                print(ip_addr, '=> Belongs to Emerald.')
            elif j == '172.30.124.214' or j == '172.30.124.215' or j == '172.30.120.214' or j == '172.30.120.215':
                print(ip_addr, '=> Belongs to Enchanted.')
            elif j == '172.30.124.82' or j == '172.30.124.83' or j == '172.30.120.42' or j == '172.30.120.43':
                print(ip_addr, '=> Belongs to Regal.')
            elif j == '172.30.229.48':
                print(ip_addr, '=> Belongs to iLab/Italy.')
            elif j == '172.30.124.36' or j == '172.30.124.37' or j == '172.30.120.6' or j == '172.30.120.37':
                print(ip_addr, '=> Belongs to Island.')
            elif j == '172.30.124.24' or j == '172.30.124.25' or j == '172.30.120.24' or j == '172.30.120.25':
                print(ip_addr, '=> Belongs to Crown.')
            elif j == '172.30.124.56' or j == '172.30.124.57' or j == '172.30.120.56' or j == '172.30.120.57':
                print(ip_addr, '=> Belongs to Majestic.')
            elif j == '172.30.124.70':
                print(ip_addr, '=> Belongs to PEv2.')
            elif j == '172.30.12.63':
                print(ip_addr, '=> Belongs to PEv21 (4g Cisco Router).')
            elif j == '172.30.124.71':
                print(ip_addr, '=> Belongs to Princess Cays.')
            elif j == '172.30.124.44' or j == '172.30.124.45' or j == '172.30.120.44' or j == '172.30.120.45':
                print(ip_addr, '=> Belongs to Royal.')
            elif j == '172.30.124.46' or j == '172.30.124.47' or j == '172.30.120.46' or j == '172.30.120.47':
                print(ip_addr, '=> Belongs to Ruby.')
            elif j == '172.30.124.48' or j == '172.30.124.49' or j == '172.30.120.48' or j == '172.30.120.49':
                print(ip_addr, '=> Belongs to Sapphire.')
            elif j == '172.30.124.216' or j == '172.30.124.217' or j == '172.30.120.216' or j == '172.30.120.217':
                print(ip_addr, '=> Belongs to Discovery.')
            elif j == '172.30.124.58' or j == '172.30.124.59' or j == '172.30.120.58' or j == '172.30.120.59':
                print(ip_addr, '=> Belongs to Sky.')
            elif j == '172.30.124.111':
                print(ip_addr, '=> Belongs to XIC-2.5.')
            elif j == '172.30.124.75' or j == '172.30.124.76':
                print(ip_addr, '=> Belongs to XS.')
            elif '10.16' in j:
                print(ip_addr, '=> Belongs to AWS.')
    else:
        print('=> Network not found')






