from netmiko import ConnectHandler
import funtions_jose
import re

# getting time
date = funtions_jose.get_time_date()
print(date[1])

print('==> Script to execute commands on non-routable devices like TLs <==')

if __name__ == '__main__':

    # IP = str(input("==> Enter the FZ-Dist IP ADD<==: "))

    JC = {
        'device_type': 'cisco_ios',
        'ip': '10.125.70.129',
        'username': 'jcr8398',
        'password': 'STP cce2010',
    }

    net_connect = ConnectHandler(**JC)
    net_connect.enable()

    # getting hostname
    dev_name = net_connect.send_command('sh run' + " " + '| inc hostname')
    host = re.search(r'host\w+\s(.*)', dev_name)

    print('==> Using' + " " + host.group(1) + " " + 'as proxy')

    tl_ip = str(input("==> Enter Tech Locker IP<==: "))

    # sending ssh-command from FZ-Dist to TL
    cmd = 'ssh -l ccl' + " " + tl_ip
    copy_file = net_connect.send_command(cmd, expect_string=r'Password:')
    try:
        copy_file += net_connect.send_command('N@v!gaT!nG~', expect_string=r'#')
        # copy_file += net_connect.send_command(tftp, expect_string=r'Destination filename')
        # copy_file += net_connect.send_command('\n', expect_string=r'#')
    except:
        raise

    version = net_connect.send_command('sh ver')
    print(version)
