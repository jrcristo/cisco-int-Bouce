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

    yes_option = ['yes', 'y']
    no_option = ['no', 'n']

    # connecting to the device(s)
    JC = funtions_jose.get_credentials_and_interface()
    net_connect = ConnectHandler(**JC)
    net_connect.enable()

    # Getting interface Details
    output = net_connect.send_command('show int' + " " + interface + " " + '| inc down|up|drops|CRC|media|collision'
                                                                       '|resets|MTU|Hardw')
    if "down" in output:
        print("==> Interface is down, process will not continue")

    else:
        print("==> Interface is up, process will continue")

        # Printing interface_UP
        if_up = re.search(r'^(Gi|Te|Vl).*', output)
        if_up_ = re.search(r'^(Gi|Te|Vl)\S+\s\w+\s\w+', if_up.group())
        line_up = re.search(r'line\sp.*', output)
        print(if_up_.group() + " " + line_up.group())

        # Getting Interface mac-add
        mac = re.search(r'([0-9]|[a-z]){4}\.\S+', output)
        print("The hardcoded interface mac-add is: ", mac.group())

        if "duplex" in output:
            # Speed Interface
            speed = re.search(r'(Full|Half)-\w+,\s\d+\w+/s', output)
            speed_filter = re.search(r'\d+.*', speed.group())
            print('The speed is: ', speed_filter.group())

            # Printing Duplex
            duplex = re.search(r'(Full|Half)-d\w+', output)
            print('The duplex is: ', duplex.group())

            # Collisions
            in_collisions = re.search(r'\d+\sco\w+', output)
            collisions_total = re.search(r'\d', in_collisions.group())
            print("Total of input collisions errors are: ", collisions_total.group())

        else:
            print('==> Probably this is a SVI interface <==')

        # Printing Drops
        drops = re.search(r'drops:\s.*', output)
        drops_total = re.search(r'\d+', drops.group())
        print("Total Drops on interface are: ", drops_total.group())

        # input_errors
        in_error = re.search(r'\d\sinput\s\w+', output)
        in_total_err = re.search(r'\d+', in_error.group())
        print("Total Input errors on Interface are: ", in_total_err.group())

        # CRC error
        in_crc = re.search(r'\d+\sCRC', output)
        crc_total = re.search(r'\d', in_crc.group())
        print("Total of input CRC errors are: ", crc_total.group())

        # interface rests
        int_reset = re.search(r'\d+\sinter\w+.*', output)
        reset_total = re.search(r'\d+', int_reset.group())
        print("Total of input interface reset errors are: ", reset_total.group())

        # Getting MTU interface value
        mtu = re.search(r'MTU\s\d+\s\w+', output)
        mtu_total = re.search(r'\d+\s\w+', mtu.group())
        print("MTU value is: ", mtu_total.group())

        # Getting BW
        bw = re.search(r'BW\s\d+\s\w+', output)
        bw_filter = re.search(r'\d+\s\w+', bw.group())
        print("The interface bandwidth is: ", bw_filter.group())

        # Getting Load
        load = re.search(r'DLY\s\d+\s\w+', output)
        load_filter = re.search(r'\d+\s\w+', load.group())
        print("The interface load is: ", load_filter.group())


