import re
from netmiko import ConnectHandler
import getpass

print('==> script to check wireless client properties <==')
mac_add = input("What's client mac-add: ")
IP = input("Give me the device IP: ")
USERNAME = input("What's the username: ")
# PASS = input("What's the password: ")
PASS = getpass.getpass()

# Connection to WLC
with ConnectHandler(ip=IP,
                    port=22,
                    username=USERNAME,
                    password=PASS,
                    device_type='cisco_wlc_ssh') as ch:
    # output = ch.send_command("show wlan summ")

    # getting output for 5Ghz
    print("==> Getting client properties from WLC for:", mac_add)
    output = ch.send_command("show client detail" + " " + mac_add)

    if "Invalid" in output:
        print("==> Device is not connected to the network, exiting\n")
        exit(0)

    else:
        print("==> Device is joined WLC, getting facts <==")
        # print(output)

        # getting client-mac-add
        client_mac = re.search(r'Client\sMAC.*', output)
        print(client_mac.group())

        # getting client hostname
        client_hostname = re.search(r'\bClient\sUsername\b.*', output)
        print(client_hostname.group())

        # getting client webauth
        client_webauth = re.search(r'Client\sWe.*', output)
        print(client_webauth.group())

        # getting hostname
        hostname = re.search(r'Host\w+.*', output)
        print(hostname.group())

        # getting device type
        device_type = re.search(r'Dev\w+\sT.*', output)
        print(device_type.group())

        # getting AP mac-add
        ap_mac = re.search(r'AP\sMAC.*', output)
        print(ap_mac.group())

        # getting AP name
        ap_name = re.search(r'AP\sNa\w+.*', output)
        print(ap_name.group())

        # getting client state
        client_state = re.search(r'Clie\w+\sState.*', output)
        print(client_state.group())

        # getting wireless ID
        wireless_id = re.search(r'Wirel\w+\sLAN\sI.*', output)
        print(wireless_id.group())

        # getting wireless SSID
        wireless_ssid = re.search(r'Wirel\w+\sLAN\sNe.*', output)
        print(wireless_ssid.group())

        # getting connected for
        connecting_for = re.search(r'Connect\w+\sFo.*', output)
        print(connecting_for.group())

        # getting bssid
        bssid = re.search(r'BSSI\w.*', output)
        print(bssid.group())

        # getting channel
        channel = re.search(r'Channel.*\d{1,3}', output)
        print(channel.group())

        # getting IP-add
        ipv4 = re.search(r'IP\sAdd\w+........................................10.*', output)
        print(ipv4.group())

        # getting netmask
        netmask = re.search(r'Netma\w+.*', output)
        print(netmask.group())

        # getting gateway
        gateway = re.search(r'Gate.*', output)
        print(gateway.group())

        # getting auth algorithm
        auth_algorithm = re.search(r'Authen\w+\sAl.*', output)
        print(auth_algorithm.group())

        # getting QoS
        qos_level = re.search(r'Qo\w\sL.*', output)
        print(qos_level.group())

        # getting supported rated
        rates = re.search(r'Suppo\w+\sR.*', output)
        print(rates.group())

        # getting vlan
        vlan = re.search(r'Acc\w+\sV.*', output)
        print(vlan.group())

        # getting DNS details
        dns_details = re.search(r'DNS\sSe\w+\sd.*', output)
        print(dns_details.group())

        # getting dns server IP
        dns_server = re.search(r'.*\bDNS\sse.*\b', output)
        print(dns_server.group())

        # getting nas_identifier
        nas_id = re.search(r'Nas\sI.*', output)
        print(nas_id.group())

        # getting Clients statistics
        client_stats = re.search(r'Cli\w+\sStatis.*', output)
        print(client_stats.group())

        # number of bytes rcvd
        number_of_bytes_rcvd = re.search(r'.*\bNumb\w+\sof\sB\w+\sRece.*\b', output)
        print(number_of_bytes_rcvd.group())

        # number of bytes sent
        number_of_bytes_sent = re.search(r'.*\bNumber\sof\sBytes\sSent\b\.......................\s.*', output)
        print(number_of_bytes_sent.group())

        # total of Number of Bytes Sent
        total_number_of_bytes_rcvd = re.search(r'.*\bTot\w+\sNu\w+\sof\sBy\w+\sSe\w+\b.*', output)
        print(total_number_of_bytes_rcvd.group())

        # Total Number of Bytes Recv
        total_number_of_bytes_sent = re.search(r'.*\bTot\w+\sNu\w+\sof\sB\w+\sR\w+\b.*', output)
        print(total_number_of_bytes_sent.group())

        # getting packets received
        packets_rcvd = re.search(r'.*\bNum\w+\sof\sPa\w+\sR.*\b', output)
        print(packets_rcvd.group())

        # getting packet sent
        packets_sent = re.search(r'.*\bNum\w+\sof\sPa\w+\sS.*\b', output)
        print(packets_sent.group())

        # getting numbers of data retries
        retries = re.search(r'.*\bNum\w+\sof\sDa\w+\sRe.*\b', output)
        print(retries.group())

        # getting RSSI and
        rssi = re.search(r'.*\bRadio\sSi.*\b', output)
        print(rssi.group())

        # getting signal-to-noise ratio
        ratio = re.search(r'.*\bSign\w+\st.*\b', output)
        print(ratio.group())

        # getting dhcp server
        '''
        dhcp = re.findall(r'DHCP.*\r[\r\n]+([^\r\n]+)', output)
        print(dhcp)
        
        for i in dhcp:
            print(i)
        '''
