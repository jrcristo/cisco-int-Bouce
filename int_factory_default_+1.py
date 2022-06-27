import getpass
from netmiko import ConnectHandler

inter = []

inter = str(input("==> Enter the interface(s), more than one use ,space (Gi1/0/1, Gi3/0/33) <==: "))
IP = input("Give me the switch IP: ")
USERNAME = input("What's the username: ")
# PASS = input("What's the password: ")
PASS = getpass.getpass()
yes_option = ['yes', 'y']
no_option = ['no', 'n']

JC = {
    'device_type': 'cisco_ios',
    'ip': IP,
    'username': USERNAME,
    'password': PASS,
    #    'fast_cli': False,
}

net_connect = ConnectHandler(**JC)
net_connect.enable()

inter_split = inter.split()
# convert list to an integer
# inter_split = ''.join([str(item) for item in inter])


def factory_default_interface(lists):
    if '-' in inter:
        print('==> Selecting multiples interface with "-" command')
        config_commands = ['default int range' + " " + inter.lower()]
        result = net_connect.send_config_set(config_commands)
        print(result)

    elif len(inter_split) == 1:
        print("==> Using one interface")
        config_commands0 = ['default int' + " " + inter.lower()]
        #       print(config_commands)
        output0 = net_connect.send_config_set(config_commands0)

        if "set to default configuration" in output0:
            print("Factory default completed")
        else:
            print("not able to factory default the interface")

    elif len(inter_split) > 1:
        print('==> Using not continuous interface range command')
        config_commands1 = ['default int range' + " " + inter.lower()]
        not_contiguous = net_connect.send_config_set(config_commands1)
        print(not_contiguous)

    else:
        print('Wrong Interface selection')
        exit(0)

    return


if '-' in inter:
    print("Can't show the running config if you use range int [Gi|Te]x/x/x ")

elif len(inter_split) >= 1:
    for j in range(len(inter_split)):
        iface = inter_split[j].rstrip(',')
        print("==> Checking current config before change on: " + " " + iface)
        output = net_connect.send_command('sh run int' + " " + iface)
        print(output, '\n')

        print('==> Checking mac-address learned on the ports before change: ', inter_split[j])
        output1 = net_connect.send_command('sh mac add int' + " " + iface)
        print(output1, '\n')

else:
    pass

factory_default = input("==> do you want to factory default the interface?, (Y) to continue (N) to cancel:").lower()
if factory_default in yes_option:
    print("==> Sending default int command")
    factory_default_interface(inter)

elif factory_default in no_option:
    print("No factory default interface command applied")
else:
    print("No factory default interface command applied")

# showing config results
if len(inter_split) >= 1:
    for j in range(len(inter_split)):
        iface = inter_split[j].rstrip(',')
        print("==> Results after config")
        output = net_connect.send_command('sh run int' + " " + iface)
        print(output, '\n')
else:
    pass

print("==> Saving config")
output = net_connect.send_command('wr mem')
print(output)
