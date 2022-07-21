import re
from netmiko import ConnectHandler
import getpass

print('==> script to check wireless client associated with an AP <==')
ap_name = input("What's the AP name: ")
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
    print("==> Getting 5Ghz clients associates with", ap_name)
    output = ch.send_command("show client ap 802.11a" + " " + ap_name)
    # filtering output for 5Ghz
    five = re.finditer(r'([a-f]|[0-9]){2}.([a-f]|[0-9]){2}.([a-f]|[0-9]){2}.*', output)
    print('MAC Address        AP Id   Status         WLAN Id    Authenticated')
    for match in five:
        print(match.group())

    print('\n')

    # getting output for 2.4Ghz
    print("==> Getting 2.4Ghz clients associates with", ap_name)
    output1 = ch.send_command("show client ap 802.11b" + " " + ap_name)
    print('MAC Address        AP Id   Status         WLAN Id    Authenticated')
    # filtering output for 2.4Ghz
    two = re.finditer(r'([a-f]|[0-9]){2}.([a-f]|[0-9]){2}.([a-f]|[0-9]){2}.*', output1)
    for match in two:
        print(match.group())