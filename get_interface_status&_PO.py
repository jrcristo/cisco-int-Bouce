from netmiko import ConnectHandler
import funtions_jose

print('==> Script to check interface Details(including POs) <==')

if __name__ == '__main__':

    inter = str(input("==> What's the Interface <==: ")).lower()

    JC = funtions_jose.get_credentials_and_interface()
    net_connect = ConnectHandler(**JC)
    net_connect.enable()

    # platform
    platform = net_connect.send_command('sh ver')
    # getting the time
    funtions_jose.get_device_date_time(net_connect)
    if 'Nexus' in platform:
        int_nxos_up = net_connect.send_command('sh int' + " " + inter + " " + '| inc Ethernet|port-channel')
        if 'up' in int_nxos_up:
            print('*---*-*---*-*---*-*---*-')
            print('=> Interface' + " " + inter + " " + 'is up, showing results')
            funtions_jose.check_interface_details_and_po(inter, net_connect)
        else:
            print('=> NXOS Interface is not UP')
    else:
        # getting interface details IOS
        if 'vl' in inter:
            vl_int_state = net_connect.send_command('sh int' + " " + inter + " " + '| inc Vl')
            if 'up' in vl_int_state:
                print('=> Interface' + " " + inter + " " + 'is up, showing results')
                funtions_jose.check_interface_details_and_po(inter, net_connect)
        else:
            is_up = net_connect.send_command('sh int' + " " + inter)
            if 'connected' in is_up:
                print('=> Interface' + " " + inter + " " + 'is up, showing results')
                funtions_jose.check_interface_details_and_po(inter, net_connect)
            else:
                print("=> IOS interface isn't UP")


