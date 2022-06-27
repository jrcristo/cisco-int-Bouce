from netmiko import ConnectHandler
import funtions_jose

if __name__ == '__main__':
    print('==> Script show ARP process from and IP||MAC-ADD <==')
    mac = input("Whats the mac-add or IP: ")
    vlan_id = input("Whats vlan id: ")

    JC = funtions_jose.get_credentials_and_interface()
    net_connect = ConnectHandler(**JC)
    net_connect.enable()

    funtions_jose.check_arp_from_ip_or_mac(mac, net_connect, vlan_id)
