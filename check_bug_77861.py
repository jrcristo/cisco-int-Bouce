from netmiko import ConnectHandler, NetmikoAuthenticationException
import re
import funtions_jose

print('==> script to check cisco BUG 77861 <==')

if __name__ == '__main__':

    yes_option = ['yes', 'y']
    no_option = ['no', 'n']

    ship = input("What's the SHIP || Location code: ").upper()
    print("==> Checking one SHIP")

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
            with open("Inventory/Campus/IDF_EX_Campus.txt", 'r') as hostsfile:
                for line in hostsfile:
                    hostline = line.strip()
                    isIP = line
                    JC = funtions_jose.if_credential_connection(isIP)
                    net_connect = ConnectHandler(**JC)
                    net_connect.enable()

                    # checking model to match 93k
                    model = funtions_jose.getting_model(net_connect)
                    if 'C9300' in model:
                        # checking model to match 93k
                        model = funtions_jose.getting_model(net_connect)
                        if 'C9300' in model:
                            print('==> This is a cat93k device, continuing with the process <==')

                            # Getting device name
                            print('=> Hostname:', funtions_jose.get_hostname_only(net_connect))

                            # Printing the Model
                            print('=> Model:', model)

                            # getting code version
                            print('=> OS or Code:', funtions_jose.get_ios_nxos_version_model(net_connect)[1])

                            # looking for LocalSoft in sh ver
                            sh_ver = net_connect.send_command('sh ver | inc reload', read_timeout=603)
                            if 'LocalSoft' in sh_ver:
                                print('***> Bug error found it on show_version')
                            else:
                                print('=> No reference to the bug found it in show_version')

                            # checking the sack size
                            stack = net_connect.send_command('sh switch')
                            stack_size = re.findall(r'.*Ready', stack)
                            print('=> There are', len(stack_size), 'switches on the stack')

                            # checking the stack members for errors related to this BUG
                            for j in range(len(stack_size)):
                                tmp = j+1
                                uptime = net_connect.send_command('sh logging onboard switch ' + str(tmp) + " " + 'uptime deta', read_timeout=603)
                                if 'reason content is absent' in uptime:
                                    print('***> Bug found it on Blade #' + str(tmp))
                                else:
                                    print('=> No reference to the bug found it in uptime details by stack #' + str(tmp))

                            print('*---.---*.*---.---*.*---.---*.*---.---*')

                    else:
                        print('Not a cat93k, exiting')
                        exit(0)

    except AttributeError:
        pass

    try:
        if xp.group():
            # loop for all devices
            with open("Inventory/Campus/IDF_XP_Campus", 'r') as hostsfile:
                for line in hostsfile:
                    hostline = line.strip()
                    isIP = line
                    JC = funtions_jose.if_credential_connection(isIP)
                    net_connect = ConnectHandler(**JC)
                    net_connect.enable()

                    # checking model to match 93k
                    model = funtions_jose.getting_model(net_connect)
                    if 'C9300' in model:
                        # checking model to match 93k
                        model = funtions_jose.getting_model(net_connect)
                        if 'C9300' in model:
                            print('==> This is a cat93k device, continuing with the process <==')

                            # Getting device name
                            print('=> Hostname:', funtions_jose.get_hostname_only(net_connect), '=>', isIP.rstrip())

                            # Printing the Model
                            print('=> Model:', model)

                            # getting code version
                            print('=> OS or Code:', funtions_jose.get_ios_nxos_version_model(net_connect)[1])

                            # looking for LocalSoft in sh ver
                            sh_ver = net_connect.send_command('sh ver | inc reload', read_timeout=603)
                            if 'LocalSoft' in sh_ver:
                                print('***> Bug error found it on show_version')
                            else:
                                print('=> No reference to the bug found it in show_version')

                            # checking the sack size
                            stack = net_connect.send_command('sh switch')
                            stack_size = re.findall(r'.*Ready', stack)
                            print('=> There are', len(stack_size), 'switches on the stack')

                            # checking the stack members for errors related to this BUG
                            for j in range(len(stack_size)):
                                tmp = j + 1
                                uptime = net_connect.send_command(
                                    'sh logging onboard switch ' + str(tmp) + " " + 'uptime deta', read_timeout=603)
                                if 'reason content is absent' in uptime:
                                    print('***> Bug found it on Blade #' + str(tmp))
                                else:
                                    print('=> No reference to the bug found it in uptime details by stack #' + str(tmp))

                            print('*---.---*.*---.---*.*---.---*.*---.---*')

                    else:
                        print('Not a cat93k, exiting')
                        exit(0)

    except AttributeError:
        pass

    try:
        if gp.group():
            # loop for all devices
            with open("Inventory/Campus/IDF_GP_Campus.txt", 'r') as hostsfile:
                for line in hostsfile:
                    hostline = line.strip()
                    isIP = line
                    JC = funtions_jose.if_credential_connection(isIP)
                    net_connect = ConnectHandler(**JC)
                    net_connect.enable()

                    # checking model to match 93k
                    model = funtions_jose.getting_model(net_connect)
                    if 'C9300' in model:
                        # checking model to match 93k
                        model = funtions_jose.getting_model(net_connect)
                        if 'C9300' in model:
                            print('==> This is a cat93k device, continuing with the process <==')

                            # Getting local time
                            local_time = net_connect.send_command('sh clock', read_timeout=603)
                            print('=> Local Time:', local_time)

                            # Getting device name
                            print('=> Hostname:', funtions_jose.get_hostname_only(net_connect), '=>', isIP.rstrip())

                            # Printing the Model
                            print('=> Model:', model)

                            # getting code version
                            print('=> OS or Code:', funtions_jose.get_ios_nxos_version_model(net_connect)[1])

                            # Getting OS version or Code
                            sh_version_os = net_connect.send_command('sh ver | inc Vers', read_timeout=603)
                            os_version = re.search(r'XE\sSo\S+\s+\S+\s(.*)', sh_version_os)
                            print('=> The Code Version is:', os_version.group(1))

                            # looking for LocalSoft in sh ver
                            sh_ver = net_connect.send_command('sh ver | inc reload', read_timeout=603)
                            if 'LocalSoft' in sh_ver:
                                print('***> Bug error found it on show_version')
                            else:
                                print('=> No reference to the bug found it in show_version')

                            # checking the sack size
                            stack = net_connect.send_command('sh switch')
                            stack_size = re.findall(r'.*Ready', stack)
                            print('=> There are', len(stack_size), 'switches on the stack')

                            # checking the stack members for errors related to this BUG
                            for j in range(len(stack_size)):
                                tmp = j + 1
                                uptime = net_connect.send_command(
                                    'sh logging onboard switch ' + str(tmp) + " " + 'uptime deta', read_timeout=603)
                                if 'reason content is absent' in uptime:
                                    print('***> Bug found it on Blade #' + str(tmp))
                                else:
                                    print('=> No reference to the bug found it in uptime details by stack #' + str(
                                        tmp))

                            print('*---.---*.*---.---*.*---.---*.*---.---*')

                    else:
                        print('Not a cat93k, exiting')
                        exit(0)

    except (AttributeError, NetmikoAuthenticationException) as error:
        pass

    try:
        if mj.group():
            # loop for all devices
            with open("Inventory/Campus/IDF_MJ_Campus.txt", 'r') as hostsfile:
                for line in hostsfile:
                    hostline = line.strip()
                    isIP = line
                    JC = funtions_jose.if_credential_connection(isIP)
                    net_connect = ConnectHandler(**JC)
                    net_connect.enable()

                    # checking model to match 93k
                    model = funtions_jose.getting_model(net_connect)
                    if 'C9300' in model:
                        # checking model to match 93k
                        model = funtions_jose.getting_model(net_connect)
                        if 'C9300' in model:
                            print('==> This is a cat93k device, continuing with the process <==')

                            # Getting local time
                            local_time = net_connect.send_command('sh clock', read_timeout=603)
                            print('=> Local Time:', local_time)

                            # Getting device name
                            print('=> Hostname:', funtions_jose.get_hostname_only(net_connect), '=>', isIP.rstrip())

                            # Printing the Model
                            print('=> Model:', model)

                            # getting code version
                            print('=> OS or Code:', funtions_jose.get_ios_nxos_version_model(net_connect)[1])

                            # Getting OS version or Code
                            sh_version_os = net_connect.send_command('sh ver | inc Vers', read_timeout=603)
                            os_version = re.search(r'XE\sSo\S+\s+\S+\s(.*)', sh_version_os)
                            print('=> The Code Version is:', os_version.group(1))

                            # looking for LocalSoft in sh ver
                            sh_ver = net_connect.send_command('sh ver | inc reload', read_timeout=603)
                            if 'LocalSoft' in sh_ver:
                                print('***> Bug error found it on show_version')
                            else:
                                print('=> No reference to the bug found it in show_version')

                            # checking the sack size
                            stack = net_connect.send_command('sh switch')
                            stack_size = re.findall(r'.*Ready', stack)
                            print('=> There are', len(stack_size), 'switches on the stack')

                            # checking the stack members for errors related to this BUG
                            for j in range(len(stack_size)):
                                tmp = j + 1
                                uptime = net_connect.send_command(
                                    'sh logging onboard switch ' + str(tmp) + " " + 'uptime deta', read_timeout=603)
                                if 'reason content is absent' in uptime:
                                    print('***> Bug found it on Blade #' + str(tmp))
                                else:
                                    print('=> No reference to the bug found it in uptime details by stack #' + str(
                                        tmp))

                            print('*---.---*.*---.---*.*---.---*.*---.---*')

                    else:
                        # Getting the time
                        print('==> Local time & Date =', funtions_jose.get_time_date()[0], '=> Time =',
                              funtions_jose.get_time_date()[1])
                        # Getting device name
                        print('=> Hostname:', funtions_jose.get_hostname_only(net_connect))
                        print('=> Model:', funtions_jose.get_ios_nxos_version_model(net_connect)[0])
                        print('=> OS or Code:', funtions_jose.get_ios_nxos_version_model(net_connect)[1])
                        print('=> Not a cat93k, exiting')
                        print('*---.---*.*---.---*.*---.---*.*---.---*')

    except AttributeError:
        pass
