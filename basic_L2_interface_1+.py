from netmiko import ConnectHandler
import funtions_jose

# getting time
date = funtions_jose.get_time_date()
print(date[1])

print('==> Script to configure default L2 interface settings <==')

if __name__ == '__main__':

    yes_option = ['yes', 'y']
    no_option = ['no', 'n']

    inter = []
    inter = str(input("==> Enter the interface(s), more than one use ,space (Gi1/0/1, Gi3/0/17) <==: ")).lower()
    vlan_id = input('Whats the Vlan#: ')

    JC = funtions_jose.get_credentials_and_interface()
    net_connect = ConnectHandler(**JC)
    net_connect.enable()

    # checking if interface is UP
    funtions_jose.check_interface_status(inter, net_connect)

    # showing current config
    funtions_jose.show_running_config(inter, net_connect)

    # applying factory default to interface(s)
    factory_default = input("==> do you want to factory default the interface?, (Y) to continue (N) to cancel:").lower()
    if factory_default in yes_option:
        print("==> Sending default int command")
        funtions_jose.factory_default_interface(inter, net_connect)

    elif factory_default in no_option:
        print("No factory default interface command applied")
    else:
        print("No factory default interface command applied")

    validation = input("==> Check the current config, do yo want to push L2 config to the interface?, if oK, "
                       "(Y) to continue (N) to cancel:").lower()

    # configuring interface L2 settings
    print('==> Settings interface(s) parameters')

    if validation in yes_option:
        funtions_jose.default_l2_interface(inter, net_connect, vlan_id)

    elif validation in no_option:
        print("NO changes committed --adios--")

    else:
        print("No changes were made.\nExiting, --BYE--")

    # showing results after commands
    funtions_jose.show_results(inter, net_connect)

    # saving config
    funtions_jose.save_config(net_connect)



