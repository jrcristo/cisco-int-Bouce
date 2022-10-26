from netmiko import ConnectHandler
import re
import funtions_jose


print('==> script to check Potential for disaster <==')

if __name__ == '__main__':

    EX_IDF = r'c:\Dell\IDF_EX_Campus.txt'

    yes_option = ['yes', 'y']
    no_option = ['no', 'n']

    all_device = input("==> do you want to check one device or all(ship), (Y) to ONE (N) to all:").lower()
    if all_device in yes_option:

        switch = input("What's IDF switch IP?: ")

        # connecting to the device
        JC = funtions_jose.if_credential_connection(switch)
        net_connect = ConnectHandler(**JC)
        net_connect.enable()

        # getting CDP neighbor
        cdp = net_connect.send_command('sh cdp ne', read_timeout=603)

        # filtering TL
        tl_s = re.findall(r'WS-C3560C', cdp)

        # Filtering Phones
        phone = re.findall(r'Mitel', cdp)

        # Filtering APs
        ap_s = re.findall(r'C9120AXI|C9130AXI|AP380', cdp)

        # Filtering Readers
        readers = re.findall(r'Linux', cdp)

        # Printing
        print('*...*.*...*.*...*.*...*')
        # Getting the time
        print('==> Local time & Date =', funtions_jose.get_time_date()[0], '=> Time =',
              funtions_jose.get_time_date()[1])
        # Getting device name
        print('=> Hostname:', funtions_jose.get_hostname_only(net_connect))
        # Printing the Model and OS
        print('=> Model:', funtions_jose.get_ios_nxos_version_model(net_connect)[0])
        print('=> OS or Code:', funtions_jose.get_ios_nxos_version_model(net_connect)[1])
        # checking the sack size
        stack = net_connect.send_command('sh switch')
        stack_size = re.findall(r'.*Ready', stack)
        print('=> There are', len(stack_size), 'switches on the stack')
        # print total of cabin affected
        print('=> Total of potentially Cabins affected', len(tl_s) * 2)
        # print total of phones
        print('=> Total of potentially Phones affected', len(phone))
        # print total APs
        print('=> Total of potentially APs affected', len(ap_s))
        # print total readers
        print('=> Total of potentially Readers affected', len(readers))

    elif all_device in no_option:
        ship = input("What's the SHIP || Location code: ").upper()
        print("==> Checking all the IDFs")

        try:
            ex = re.match('^EX', ship)
            xp = re.match('^XP', ship)
            yp = re.match('^YP', ship)
            gp = re.match('^GP', ship)
            rp = re.match('^RP', ship)
            mj = re.match('^MJ', ship)
            ap = re.match('^AP', ship)
            cb = re.match('^CB', ship)
            co = re.match('^CO', ship)
            di = re.match('^DI', ship)
            ep = re.match('^EP', ship)
            kp = re.match('^KP', ship)
            ip = re.match('^IP', ship)
            ru = re.match('^RU', ship)
            sa = re.match('^SA', ship)
            pev2 = re.match('^PEV', ship)
            test = re.match('^TEST', ship)

        except AttributeError:
            pass

        try:
            if ex.group():
                # loop for all devices
                with open("IDF_EX_Campus.txt", 'r') as hostsfile:
                    for line in hostsfile:
                        hostline = line.strip()
                        isIP = line
                        JC = funtions_jose.if_credential_connection(isIP)
                        net_connect = ConnectHandler(**JC)
                        net_connect.enable()

                        # calling function
                        funtions_jose.get_potential_for_disaster(net_connect)

        except AttributeError:
            pass

        try:
            if xp.group():
                # loop for all devices
                with open("IDF_XP_Campus", 'r') as hostsfile:
                    for line in hostsfile:
                        hostline = line.strip()
                        isIP = line
                        JC = funtions_jose.if_credential_connection(isIP)
                        net_connect = ConnectHandler(**JC)
                        net_connect.enable()

                        # calling function
                        funtions_jose.get_potential_for_disaster(net_connect)

        except AttributeError:
            pass

        try:
            if yp.group():
                # loop for all devices
                with open("IDF_YP_Campus.txt", 'r') as hostsfile:
                    for line in hostsfile:
                        hostline = line.strip()
                        isIP = line
                        JC = funtions_jose.if_credential_connection(isIP)
                        net_connect = ConnectHandler(**JC)
                        net_connect.enable()

                        # calling function
                        funtions_jose.get_potential_for_disaster(net_connect)

        except AttributeError:
            pass

        try:
            if gp.group():
                # loop for all devices
                with open("IDF_GP_Campus.txt", 'r') as hostsfile:
                    for line in hostsfile:
                        hostline = line.strip()
                        isIP = line
                        JC = funtions_jose.if_credential_connection(isIP)
                        net_connect = ConnectHandler(**JC)
                        net_connect.enable()

                        # calling function
                        funtions_jose.get_potential_for_disaster(net_connect)

        except AttributeError:
            pass

        try:
            if rp.group():
                # loop for all devices
                with open("IDF_RP_Campus.txt", 'r') as hostsfile:
                    for line in hostsfile:
                        hostline = line.strip()
                        isIP = line
                        JC = funtions_jose.if_credential_connection(isIP)
                        net_connect = ConnectHandler(**JC)
                        net_connect.enable()

                        # calling function
                        funtions_jose.get_potential_for_disaster(net_connect)

        except AttributeError:
            pass

        try:
            if mj.group():
                # loop for all devices
                with open("IDF_MJ_Campus.txt", 'r') as hostsfile:
                    for line in hostsfile:
                        hostline = line.strip()
                        isIP = line
                        JC = funtions_jose.if_credential_connection(isIP)
                        net_connect = ConnectHandler(**JC)
                        net_connect.enable()

                        # calling function
                        funtions_jose.get_potential_for_disaster(net_connect)

        except AttributeError:
            pass

        try:
            if ap.group():
                # loop for all devices
                with open("IDF_AP_Campus.txt", 'r') as hostsfile:
                    for line in hostsfile:
                        hostline = line.strip()
                        isIP = line
                        JC = funtions_jose.if_credential_connection(isIP)
                        net_connect = ConnectHandler(**JC)
                        net_connect.enable()

                        # calling function
                        funtions_jose.get_potential_for_disaster(net_connect)

        except AttributeError:
            pass

        try:
            if cb.group():
                # loop for all devices
                with open("IDF_CB_Campus.txt", 'r') as hostsfile:
                    for line in hostsfile:
                        hostline = line.strip()
                        isIP = line
                        JC = funtions_jose.if_credential_connection(isIP)
                        net_connect = ConnectHandler(**JC)
                        net_connect.enable()

                        # calling function
                        funtions_jose.get_potential_for_disaster(net_connect)
                exit(0)

        except AttributeError:
            pass

        try:
            if co.group():
                # loop for all devices
                with open("IDF_CO_Campus.txt", 'r') as hostsfile:
                    for line in hostsfile:
                        hostline = line.strip()
                        isIP = line
                        JC = funtions_jose.if_credential_connection(isIP)
                        net_connect = ConnectHandler(**JC)
                        net_connect.enable()

                        # calling function
                        funtions_jose.get_potential_for_disaster(net_connect)

        except AttributeError:
            pass

        try:
            if di.group():
                # loop for all devices
                with open("IDF_DI_Campus.txt", 'r') as hostsfile:
                    for line in hostsfile:
                        hostline = line.strip()
                        isIP = line
                        JC = funtions_jose.if_credential_connection(isIP)
                        net_connect = ConnectHandler(**JC)
                        net_connect.enable()

                        # calling function
                        funtions_jose.get_potential_for_disaster(net_connect)

        except AttributeError:
            pass

        try:
            if ep.group():
                # loop for all devices
                with open("IDF_EP_Campus.txt", 'r') as hostsfile:
                    for line in hostsfile:
                        hostline = line.strip()
                        isIP = line
                        JC = funtions_jose.if_credential_connection(isIP)
                        net_connect = ConnectHandler(**JC)
                        net_connect.enable()

                        # calling function
                        funtions_jose.get_potential_for_disaster(net_connect)

        except AttributeError:
            pass

        try:
            if kp.group():
                # loop for all devices
                with open("IDF_KP_Campus.txt", 'r') as hostsfile:
                    for line in hostsfile:
                        hostline = line.strip()
                        isIP = line
                        JC = funtions_jose.if_credential_connection(isIP)
                        net_connect = ConnectHandler(**JC)
                        net_connect.enable()

                        # calling function
                        funtions_jose.get_potential_for_disaster(net_connect)
                exit(0)

        except AttributeError:
            pass

        try:
            if ip.group():
                # loop for all devices
                with open("IDF_IP_Campus.txt", 'r') as hostsfile:
                    for line in hostsfile:
                        hostline = line.strip()
                        isIP = line
                        JC = funtions_jose.if_credential_connection(isIP)
                        net_connect = ConnectHandler(**JC)
                        net_connect.enable()

                        # calling function
                        funtions_jose.get_potential_for_disaster(net_connect)
                exit(0)

        except AttributeError:
            pass

        try:
            if ru.group():
                # loop for all devices
                with open("IDF_RU_Campus.txt", 'r') as hostsfile:
                    for line in hostsfile:
                        hostline = line.strip()
                        isIP = line
                        JC = funtions_jose.if_credential_connection(isIP)
                        net_connect = ConnectHandler(**JC)
                        net_connect.enable()

                        # calling function
                        funtions_jose.get_potential_for_disaster(net_connect)
                exit(0)

        except AttributeError:
            pass

        try:
            if sa.group():
                # loop for all devices
                with open("IDF_SA_Campus.txt", 'r') as hostsfile:
                    for line in hostsfile:
                        hostline = line.strip()
                        isIP = line
                        JC = funtions_jose.if_credential_connection(isIP)
                        net_connect = ConnectHandler(**JC)
                        net_connect.enable()

                        # calling function
                        funtions_jose.get_potential_for_disaster(net_connect)
                exit(0)

        except AttributeError:
            pass







