from netmiko import ConnectHandler
import funtions_jose

print('==> script to check DMVPN Ocean link <==')

if __name__ == '__main__':

    yes_option = ['yes', 'y']
    no_option = ['no', 'n']

    JC = funtions_jose.get_credentials_and_interface()
    net_connect = ConnectHandler(**JC)
    net_connect.enable()

    # showing dmvpn results
    funtions_jose.check_ocean_dmvpn(net_connect)
    print('\n')

    # showing bgp prefixes received from AWS
    received_adv = input("==> do you want to see the prefixes received from the AWS neighbor?, (Y) to continue ("
                         "N) to cancel:").lower()
    if received_adv in yes_option:
        bgp_peer = input("Whats the AWS neighbor: ")
        print('==> Getting prefixes from Neighbor from: ' + " " + bgp_peer)
        funtions_jose.check_bgp_ocean_received_routes(bgp_peer, net_connect)

    else:
        print('==> skipping prefixes output')

    # showing bgp prefixes advertised to AWS
    adv_prefixes = input("==> do you want to see the advertised prefixes to the neighbor?, (Y) to continue ("
                         "N) to cancel:").lower()
    if adv_prefixes in yes_option:
        bgp_peer0 = input("Whats the AWS neighbor: ")
        print('==> Getting prefixes sent to Neighbor: ' + " " + bgp_peer0)
        funtions_jose.check_bgp_ocean_sent_routes(bgp_peer0, net_connect)
    else:
        print('==> skipping adv prefixes output')

    # showing bgp table
    bgp_table = input("==> do you want to see the FULL BGP table?, (Y) to continue ("
                      "N) to cancel:").lower()
    if bgp_table in yes_option:
        print('==> Getting BGP table')
        funtions_jose.check_bgp_ocean_table(net_connect)
    else:
        print('==> skipping BGP table output')

    # showing bgp network details
    bgp_network_specific = input("==> do you want to see a specific BGP learned network?, (Y) to continue ("
                                 "N) to cancel:").lower()
    if bgp_network_specific in yes_option:
        bgp_net = input("Whats the specific network?: ")
        print('==> Getting route specific details')
        funtions_jose.check_bgp_ocean_network_specific(bgp_net, net_connect)
    else:
        print('==> Skipping BGP network details')

    # showing bgp nei details
    bgp_details = input("==> do you want to see BGP neighbor details?, (Y) to continue ("
                        "N) to cancel:").lower()
    if bgp_details in yes_option:
        bgp_peer1 = input("Whats the AWS neighbor: ")
        print('==> Getting BGP neighbor details from: ' + " " + bgp_peer1)
        funtions_jose.check_bgp_neighbor_ocean_details(bgp_peer1, net_connect)
    else:
        print('==> skipping neighbor details')
