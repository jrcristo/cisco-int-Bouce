from netmiko import ConnectHandler
import funtions_jose

# getting time
date = funtions_jose.get_time_date()
print(date[1])

print('==> Script to check power draw details <==')

if __name__ == '__main__':

    inter = []
    inter = str(input("==> Enter the interface <==: "))

    JC = funtions_jose.get_credentials_and_interface()
    net_connect = ConnectHandler(**JC)
    net_connect.enable()

    # calling the function
    funtions_jose.check_power_inline_details(inter, net_connect)


