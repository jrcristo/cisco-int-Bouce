from netmiko import ConnectHandler
import funtions_jose

print('==> Script to get PAN-OS system info <==')

if __name__ == '__main__':

    panos = funtions_jose.panos_credentials()
    net_connect = ConnectHandler(**panos)
    net_connect.enable()
'''
config_commands = [
    'show system info',
    # 'show system resources', # next command after this will hang
    'show high-availability all'
]
out = ""
for cmd in config_commands:
    print("Executing %s" % cmd)
    out += "-------------"
    out += net_connect.send_command(cmd)

print(out)
'''
# getting inf
funtions_jose.panos_show_system_info(net_connect)


net_connect.disconnect()
