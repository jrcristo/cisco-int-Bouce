from netmiko import ConnectHandler
import funtions_jose

print('==> Script to check non_routable devices <==')

if __name__ == '__main__':

    JC = funtions_jose.get_credentials_and_interface()
    net_connect = ConnectHandler(**JC)
    net_connect.enable()

    tl = input("==> Whats the TL IP?:").lower()

    # trying to connect TLs using FZ as a proxy

    output = net_connect.send_command('sh ver')
    print(output)
