from netmiko import ConnectHandler
import funtions_jose

print('==> Script to check BGP neighbors status <==')

if __name__ == '__main__':

    bgp_route = input("Whats the BGP IP|Network: ")

    JC = funtions_jose.get_credentials_and_interface()
    net_connect = ConnectHandler(**JC)
    net_connect.enable()

    # calling function
    funtions_jose.check_bgp_network(bgp_route, net_connect)




