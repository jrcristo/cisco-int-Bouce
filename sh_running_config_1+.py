from netmiko import ConnectHandler
import funtions_jose

if __name__ == '__main__':
    print('==> Script to show running config on interface <==')
    inter = input("Whats the interface: ")

    JC = funtions_jose.get_credentials_and_interface()
    net_connect = ConnectHandler(**JC)
    net_connect.enable()

    # funtions_jose.show_running_config_single(inter, net_connect)
    funtions_jose.show_running_config(inter, net_connect)
