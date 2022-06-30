import getpass
import re
import funtions_jose
import time
from netmiko import ConnectHandler

# getting time
date = funtions_jose.get_time_date()
print(date[1])

print('==> Script to collect error details x interface <==')

if __name__ == '__main__':

    interface = input("Whats the interface: ")

    # connecting to the device(s)
    JC = funtions_jose.get_credentials_and_interface()
    net_connect = ConnectHandler(**JC)
    net_connect.enable()

    # Getting interface Details
    output = net_connect.send_command('show int' + " " + interface + " " + '| inc down|up|drops|CRC|media|collision'
                                                                           '|resets|MTU|Hardw')

    # interface status
    if 'down' in output:
        print('===> Interface' + " " + interface + " " + 'is DOWN <===')
    else:
        print('===> Interface' + " " + interface + " " + 'is UP <===')

    # getting MTU
    mtu = re.search(r'MTU\s(\d+)\sby\w+.\s\w+\s(\d+\s\w+.s\w+).\sD\w+\s(\d+\s\w+)', output)
    print('MTU Value is = ', mtu.group(1))

    # Getting Interface mac-add
    mac = re.search(r'([0-9]|[a-z]){4}\.\S+', output)
    print("The hardcoded interface mac-add is:", mac.group())
    print('Bandwidth is =', mtu.group(2))
    print('Delays is =', mtu.group(3))

    if 'Full-duplex' in output:
        # Speed Interface
        speed = re.search(r'Full-\w+.\s(\d+\w+.\w+)', output)
        print('The speed is:', speed.group(1))

        # getting duplex
        duplex = re.search(r'.*\bduplex\b', output)
        print('The duplex is:', duplex.group())

    else:
        pass

    # output errors, Collisions and reset
    collisions = re.search(r'(\d+)\sout\w+\ser\w+,\s(\d+)\sco\w+.\s(\d+)', output)
    print('Total output error =', collisions.group(1))
    print("Total of output collisions errors =", collisions.group(2))
    print('Total output interface reset =', collisions.group(3))

    # Printing Drops
    drops = re.search(r'\boutput\sdrops.\s(\d+)\b', output)
    print("Total Drops on interface =", drops.group(1))

    # Input Errors and CRC
    input_errors = re.search(r'(\d+)\sinput\serr\w+.\s(\d+)', output)
    print('Total Input Error =', input_errors.group(1))
    print('Total Input CRC errors =', input_errors.group(2))



