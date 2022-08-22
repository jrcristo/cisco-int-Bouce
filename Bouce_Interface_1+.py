
from netmiko import ConnectHandler
import funtions_jose

print('==> Script to bounce interfaces <==')

if __name__ == '__main__':

    yes_option = ['yes', 'y']
    no_option = ['no', 'n']

    inter = []
    inter = str(input("==> Enter the interface(s), more than one use ,space (Gi1/0/1, Gi5/0/7) <==: "))

    JC = funtions_jose.get_credentials_and_interface()
    net_connect = ConnectHandler(**JC)
    net_connect.enable()

    # check interface status
    funtions_jose.check_interface_status(inter, net_connect)

    # showing current config
    funtions_jose.show_running_config(inter, net_connect)

    # executing interface bounce
    reboot = input("==> do you want to reboot the interface(s)?, (Y) to continue (N) to cancel:").lower()
    if reboot in yes_option:
        print("==> Sending reboot int command")
        funtions_jose.bounce_interface(inter, net_connect)

    elif reboot in no_option:
        print("exiting")
    else:
        print("exiting")
