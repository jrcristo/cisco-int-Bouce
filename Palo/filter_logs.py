from netmiko import ConnectHandler
import funtions_jose

# getting time
date = funtions_jose.get_time_date()
print(date[1], '\n')

print('==> Script filter logs from PAN-OS <==')


if __name__ == '__main__':

    src_ip = input("What's src_ip: ")

    panos = funtions_jose.panos_credentials()
    net_connect = ConnectHandler(**panos)
    net_connect.enable()

    # getting the logs
    funtions_jose.panos_filter_logs(src_ip, net_connect)
