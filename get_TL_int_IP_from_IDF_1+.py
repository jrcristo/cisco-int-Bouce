import re

from netmiko import ConnectHandler
import funtions_jose

if __name__ == '__main__':

    tl_name = input("Whats the TL name?: ")

    JC = funtions_jose.get_credentials_and_interface()
    net_connect = ConnectHandler(**JC)
    net_connect.enable()

    # getting cdp neighbor interface
    cdp = net_connect.send_command('sh cdp ne | sec' + " " + tl_name)

    if 'Total cdp entries displayed : 0' in cdp or not cdp:
        print("==> I couldn't find" + " " + tl_name + " " + 'is probable down')

    else:
        cdp_int = re.search(r'Gig\s\d+/\d/\d+', cdp)
        inter = cdp_int.group().replace(" ", "")

        # calling cdp function
        result = funtions_jose.get_cdp_neighbor(inter, net_connect)
        print('==> The neighbor interface is:', inter)
        print('==> TL neighbor IP is: ', result[0])



