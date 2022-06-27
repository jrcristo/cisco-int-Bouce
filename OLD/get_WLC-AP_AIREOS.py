from netmiko import ConnectHandler
import getpass
import re

print('==> script to check if an AP is joined WLC <==')

ap_name = input("What's the AP name or mac-add: ")
yp = re.match('^YP', ap_name)
print('this is the result', yp.group())

# evaluating which ship
if yp.group():
    print('==> Using SKY WLC ip-add ')

else:
    print('no SKY')

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
    output = ch.send_command("show ap config general" + " " + ap_name)
#    print(ch.send_command("show ap config general" + " " + ap_name))

    if "invalid" in output:
        print("==> AP is not joined WLC, exiting\n")
        exit(0)

    else:
        print("==> AP is joined WLC, getting facts <==")

    # Filtering AP name
    ap = re.search(r'Cisco\sAP\sN.*', output)
    print(ap.group())

    # Filtering Country code
    c_code = re.search(r'AP\sCoun.*', output)
    print(c_code.group())

    # Filtering Regulatory Domain
    regulatory = re.search(r'AP\sReg.*', output)
    print(regulatory.group())

    # Filtering mac-add
    mac = re.search(r'MAC\sAddre.*', output)
    print(mac.group())

    # IP Address Configuration
    ip_dhcp = re.search(r'IP\sAdd\w+\s.*', output)
    print(ip_dhcp.group())

    # IP Address
    ip_add = re.search(r'IP\sAdd\w+(.){39}\s\d.*', output)
    print(ip_add.group())

    # IP netmask
    ip_net = re.search(r'IP\sNe.*', output)
    print(ip_net.group())

    # Gateway
    gateway = re.search(r'Gatew.*', output)
    print(gateway.group())

    # capwap
    capwap = re.search(r'CAPWAP\sP.*', output)
    print(capwap.group())

    # telnet
    telnet = re.search(r'Tel.*', output)
    print(telnet.group())

    # SSH
    ssh = re.search(r'Ssh.*', output)
    print(ssh.group())

    # NSI
    nsi = re.search(r'NSI.*', output)
    print(nsi.group())

    # ap location
    location = re.search(r'Ci\w+\sAP\sLo.*', output)
    print(location.group())

    # floor label
    floor = re.search(r'Ci\w+\sAP\sFl.*', output)
    print(floor.group())

    # group name
    group_name = re.search(r'Cis\w+\sAP\sG.*', output)
    print(group_name.group())

    # IP switch
    switch_pri = re.search(r'Primary\sC\w+\sS\w+\sI.*', output)
    print(switch_pri.group())

    # Tertiary
    tertiary = re.search(r'Tertiary\sCi\w+\sS\w+\sI.*', output)
    print(tertiary.group())

    # admin state
    admin_state = re.search(r'Administrative\s.*', output)
    print(admin_state.group())

    # mirror
    mirror = re.search(r'Mirror.*', output)
    print(mirror.group())

    # ap mode
    ap_mode = re.search(r'AP\sM\w+\s.*', output)
    print(ap_mode.group())

    # s/w version
    sw = re.search(r'S/W.*', output)
    print(sw.group())

    # boot
    boot = re.search(r'Boo.*', output)
    print(boot.group())

    # led state
    led = re.search(r'LED\sS.*', output)
    print(led.group())

    # power type
    power = re.search(r'Po\w+\sT.*', output)
    print(power.group())

    # ap model
    model = re.search(r'AP\sModel.*', output)
    print(model.group())

    # ap image
    ap_image = re.search(r'AP\sIma.*', output)
    print(ap_image.group())

    # ios version
    ios = re.search(r'IOS\sV\w+\S+.\d.*', output)
    print(ios.group())

    # ap serial #
    serial = re.search(r'AP\sSe.*', output)
    print(serial.group())

    # ap username
    ap_username = re.search(r'AP\sU\w+\sN.*', output)
    print(ap_username.group())

    # dot1x
    dot1 = re.search(r'AP\sDo\w+\sE.*', output)
    print(dot1.group())

    # uptime
    uptime = re.search(r'AP\sUp\s.*', output)
    print(uptime.group())

    # ap LWAP
    ap_lwap = re.search(r'AP\sLW.*', output)
    print(ap_lwap.group())

    # join date
    join = re.search(r'Join\sD.*', output)
    print(join.group())

    # join taken
    join_taken = re.search(r'Join\sTa.*', output)
    print(join_taken.group())

    # memory type
    memory = re.search(r'Mem\w+\sT.*', output)
    print(memory.group())

    # memory size
    memory_size = re.search(r'Mem\w+\sS.*', output)
    print(memory_size.group())

    # flash size
    flash = re.search(r'Fla\w+\sS.*', output)
    print(flash.group())

    # ethernet duplex
    eth_duplex = re.search(r'Ether\w+\sP\w+\sD.*', output)
    print(eth_duplex.group())

    # ethernet speed
    eth_speed = re.search(r'Ether\w+\sP\w+\sS.*', output)
    print(eth_speed.group())

    # mss adjust
    mss_adjust = re.search(r'AP\sT\w+\sM\w+\sA.*', output)
    print(mss_adjust.group())

    # mss size
    mss_size = re.search(r'AP\sT\w+\sM\w+\sS.*', output)
    print(mss_size.group())
