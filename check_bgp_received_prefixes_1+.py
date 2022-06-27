from netmiko import ConnectHandler
import funtions_jose

print('==> Script to check received routes from a BGP neighbor <==')

if __name__ == '__main__':

    yes_option = ['yes', 'y']
    no_option = ['no', 'n']

    JC = funtions_jose.get_credentials_and_interface()
    net_connect = ConnectHandler(**JC)
    net_connect.enable()

    # showing BGP neighbors
    funtions_jose.check_bgp_neighbors_all(net_connect)

    # asking for the neighbor IP
    bgp_nei = input('Whats neighbor IP? ')

    # showing advertised routes
    specific_route = input("==> do you want to search for a specific route?, (Y) to continue (N) to cancel:").lower()
    if specific_route in yes_option:
        bgp_route = input('Whats the specific route you want to check? ')
        print("==> Checking for " + " " + bgp_route)
        funtions_jose.check_bgp_received_routes(bgp_nei, bgp_route, net_connect)

    elif specific_route in no_option:
        bgp_route = False
        print("==> Showing all the received-routes from", bgp_nei)
        funtions_jose.check_bgp_received_routes(bgp_nei, bgp_route, net_connect)
    else:
        print("no actions")
