from netmiko import ConnectHandler
import funtions_jose
import re

# getting time
date = funtions_jose.get_time_date()
print(date[1])

print('==> script to check high interface utilization (rx && tx load) <==')

if __name__ == '__main__':

    yes_option = ['yes', 'y']
    no_option = ['no', 'n']

    JC = funtions_jose.get_credentials_and_interface()
    net_connect = ConnectHandler(**JC)
    net_connect.enable()

    # getting interfaces
    int_up = net_connect.send_command('sh int status | inc connected')

    # grabbing INT
    interfaces_non_po = re.findall(r'[TG]\w+.\d.\d+|Et\w+/\d+', int_up)
    interfaces_po = re.findall(r'\w+-c\w+|Po\d+', int_up)

    # print(len(interfaces_non_po))

    # printing
    print('=> Printing NON POs Interface')
    for j in interfaces_non_po:
        # getting reliability
        reliability = net_connect.send_command('sh int' + " " + j + " " + '| inc reliabil')
        desc = net_connect.send_command('sh int' + " " + j + " " + '| inc Descript')
        # getting Tx && Rx load
        tx_rx = re.search(r'tx\w+\s(\d+).\d+,\s\w+\s(\d+).\d+', reliability)
        # getting desc
        description = re.search(r'Des\w+.\s(\w.*)', desc)
        print('==> Interface ', j)
        try:
            if description.group(1):
                print('=> Description: =>', description.group(1))
        except AttributeError:
            print('=> Description: => none')
        total_TX = float(int(tx_rx.group(1)) * 100) / 255
        total_RX = float(int(tx_rx.group(2)) * 100) / 255
        print('=> TxLoad value is=', tx_rx.group(1), '=>', 'total int % of TX=', round(total_TX, 2), '%')
        print('=> RxLoad value is=', tx_rx.group(2), '=>', 'total int % of RX=', round(total_RX, 2), '%')

        if (int(tx_rx.group(1)) > 150 or int(tx_rx.group(2))) > 157:
            print('==> Int' + " " + j + " " + 'utilization is super higher, maybe L2 loop or something else')
            print('=> Showing int Config')
            inter = net_connect.send_command('sh int' + " " + j)
            print(inter)
            int_validation = input("==> do you want to shutdown interface?, (Y) to continue ("
                                   "N) to cancel:").lower()
            if int_validation in yes_option:
                print('==> sending shutdown command to ', j)
                config_commands = ['int' + " " + j, 'sh']
                output = net_connect.send_config_set(config_commands)
                # validating shutdown
                shut = net_connect.send_command('sh run int' + " " + j)
                if 'shutdown' in shut:
                    print('==> Interface was shutdown')
                    print('\n')
                else:
                    print('=> Interface was not shutdown')
            else:
                print('==> no shutdown command sent')

        print('*---*-*---*-*---*-*---*-*---*-*---*')
    print('=> Total number of interfaces is ', len(interfaces_non_po))
    print('\n')

    # printing POs
    print('=> Printing POs Interface')
    for c in interfaces_po:
        # print(c)
        reliability_po = net_connect.send_command('sh int' + " " + c + " " + '| inc reliabil')
        po_desc = net_connect.send_command('sh int' + " " + j + " " + '| inc Descript')
        # getting Tx && Rx load
        tx_rx_po = re.search(r'tx\w+\s(\d+).\d+,\s\w+\s(\d+).\d+', reliability_po)
        # getting desc
        po_description = re.search(r'Des\w+.\s(\w.*)', po_desc)
        print('==> Interface ', c)
        try:
            if po_description.group(1):
                print('=> Description: =>', po_description.group(1))
        except AttributeError:
            pass
        total_po_TX = float(int(tx_rx_po.group(1)) * 100) / 255
        total_po_RX = float(int(tx_rx_po.group(2)) * 100) / 255
        print('=> TxLoad = ', tx_rx_po.group(1), '=>', 'total int % of TX=', round(total_po_TX, 2), '%')
        print('=> RxLoad = ', tx_rx_po.group(2), '=>', 'total int % of RX=', round(total_po_RX, 2), '%')
        print('*---*-*---*-*---*-*---*-*---*-*---*')
    print('=> Total number of PO interfaces is ', len(interfaces_po))
