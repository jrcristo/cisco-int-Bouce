from netmiko import ConnectHandler
import funtions_jose
import getpass
import re

# getting time
date = funtions_jose.get_time_date()
print(date[1])

print('==> Script to check maximum clients connected by AP <==')

if __name__ == '__main__':
    yes_option = ['yes', 'y']
    no_option = ['no', 'n']

    # Connection to WLC
    JC = funtions_jose.get_credentials_and_interface()
    net_connect = ConnectHandler(**JC)
    net_connect.enable()

    # getting AP summary info
    # wlc = net_connect.send_command('sh ap summary load-info')
    # wlc = net_connect.send_command('sh ap summary load-info')
    output = net_connect.send_command('sh ver')

    # Filtering the results
    # ap_summary = re.findall(r'(^\w+-\d+-\w+-\w+\s+\d+.[a-fA-F0-9]+.[a-fA-F0-9]+\s+\d{1,2}\s+\d+)', output)

    print(output)
