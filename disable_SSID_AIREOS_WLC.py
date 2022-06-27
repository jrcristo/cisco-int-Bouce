import re
from netmiko import ConnectHandler
import getpass


yes_option = ['yes', 'y']
no_option = ['no', 'n']

print('==> script to enable||disable Ocean SSID <==')

# PASS = input("What's the password: ")
PASS = getpass.getpass()

# Connection to WLC
with ConnectHandler(ip='10.5.160.10',
                    port=22,
                    username='ccl',
                    password=PASS,
                    device_type='cisco_wlc_ssh') as ch:
    # output = ch.send_command("show wlan summ")

    # asking for disable SSID
    disable = input("==> do you want Disable Ocean SSID?, (Y) to continue (N) to cancel:").lower()
    if disable in yes_option:
        print("==> turning off OCEAN SSID")
        output = ch.send_command("config wlan disable 1")
        summ = ch.send_command("show wlan summ")

        # filtering output
        wlan = re.search(r'\b([1])\b.*', summ)
        if 'Disabled' in wlan.group():
            print('==> SSID disabled successfully')
        else:
            print("==> couldn't disable the SSID")

    else:
        print("Ocean SSID was not disabled")

    # asking for enable SSID
    enable = input("==> do you want Enable Ocean SSID?, (Y) to continue (N) to cancel:").lower()
    if enable in yes_option:
        print("==> turning on OCEAN SSID")
        # output = ch.send_command("config wlc enable 1")
        output = ch.send_command('config wlan enable 1')
        summ = ch.send_command("show wlan summ")

        # filtering output
        wlan = re.search(r'\b([1])\b.*', summ)
        if 'Enabled' in wlan.group():
            print('==> SSID enabled successfully')
        else:
            print("==> couldn't enable the SSID")

    elif enable in no_option:
        print("Ocean SSID was not enabled")
    else:
        print("Ocean SSID was not enabled")



