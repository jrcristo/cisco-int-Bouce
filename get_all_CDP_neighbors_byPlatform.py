from netmiko import ConnectHandler
import funtions_jose
import time
import re

# getting time
date = funtions_jose.get_time_date()
print(date[1])

print('==> Script to check all the neighbors by platform <==')

if __name__ == '__main__':

    yes_option = ['yes', 'y']
    no_option = ['no', 'n']

    # connecting to the device(s)
    JC = funtions_jose.get_credentials_and_interface()
    net_connect = ConnectHandler(**JC)
    net_connect.enable()

    # showing platforms:
    cdp = net_connect.send_command('sh cdp ne | inc Gig')
    platform_regex = re.findall(r'(Mitel|C91\w+|Linux|WS-\w+|AIR-AP\w+)', cdp)
    new_platform_list = []

    # filtering items not repeated
    for i in platform_regex:
        if i not in new_platform_list:
            new_platform_list.append(i)

    # printing the platforms
    print('==> Showing platforms found on device <==')
    print(new_platform_list, '\n')

    # filtering by platform
    user_platform = input("Please, copy and paste the one you want to filter from the above output: ")
    result = net_connect.send_command('sh cdp ne | inc' + " " + user_platform)
    nei_int = re.findall(r'(\s+Gig\s\d+/\d/\d+)', result)

    if 'WS-C3560C' in user_platform:
        print('==> Showing TLs platform information <==')
    elif 'AIR-AP' in user_platform:
        print('==> Showing APs platform information <==')
    elif 'C91' in user_platform:
        print('==> Showing 91x APs platform information <==')

    elif 'Linux' or 'Mitel' in user_platform:
        print('==> Showing NON CDP platform information <==')
        lldp = net_connect.send_command('sh run | inc lldp')
        if not lldp:
            lldp_check = input("==> LLDP is not enable, do you want to enable it?, (Y) to continue (N) to cancel:").lower()
            if lldp_check in yes_option:
                config_commands = ['lldp run']
                result = net_connect.send_config_set(config_commands)
                # checking if lldp is running
                lldp_run = net_connect.send_command('sh run | inc lldp')
                if 'lldp run' in lldp_run:
                    print('==> LLDP has been enabled')
                    print('=> getting LLDP info')
                    # put some delays (lldp needs some time after being enabled)
                    print('=> Waiting 11s for LLDP to be ready <==')
                    time.sleep(11)
                    # removing leading spaces
                    # k = []
                    for i in nei_int:
                        j = i.lstrip()
                        # k.append(j)
                        # print(j)
                        # getting cdp info
                        lldp_function = funtions_jose.get_lldp_neighbor(j, net_connect)
                        print('The lldp neighbor chassis id is: ', lldp_function[0])
                        print('The lldp neighbor system name is: ', lldp_function[2])
                        print('The lldp neighbor IP is: ', lldp_function[1])
                        print('The lldp neighbor interface is: ', j)
                        print(lldp_function[3])
                        print('*--------*-*--------*-*--------*-*--------*')
                    print('=> Total LLDP neighbors = ', len(nei_int))


                else:
                    print("=> Couldn't enable LLDP <==")
            else:
                print("=> LLDP won't be enabled <==")
        else:
            print('==> LLDP was already enabled <==')
            print('=> getting LLDP info <=')
            # removing leading spaces
            # k = []
            for i in nei_int:
                j = i.lstrip()
                # k.append(j)
                # print(j)
                # getting cdp info
                lldp_func = funtions_jose.get_lldp_neighbor(j, net_connect)
                print('The lldp neighbor chassis id is: ', lldp_func[0])
                print('The lldp neighbor system name is: ', lldp_func[2])
                print('The lldp neighbor IP is: ', lldp_func[1])
                print('The lldp neighbor interface is: ', j)
                print(lldp_func[3])
                print('*--------*-*--------*-*--------*-*--------*')
            print('=> Total LLDP neighbors = ', len(nei_int))

        # removing LLDP from SW
        print('==> Removing LLDP capabilities from the switch <==')
        config_commands = ['no lldp run']
        result = net_connect.send_config_set(config_commands)
        lldp_last = net_connect.send_command('sh run | inc lldp')
        if not lldp_last:
            print('==> LLDP has been disabled <==')
        exit(0)
    else:
        pass

    print('\n')

    # CDP
    # removing leading spaces
    # k = []
    for i in nei_int:
        j = i.lstrip()
        # k.append(j)
        # print(j)
        # getting cdp info
        cdp = funtions_jose.get_cdp_neighbor(j, net_connect)
        print('The cdp neighbor name is: ', cdp[1])
        print('The cdp neighbor IP is: ', cdp[0])
        print('The cdp neighbor platform is: ', cdp[2])
        print('The cdp neighbor interface is: ', j)
        print('*--------*-*--------*-*--------*-*--------*')

    print('=> Total CDP neighbors = ', len(nei_int))





