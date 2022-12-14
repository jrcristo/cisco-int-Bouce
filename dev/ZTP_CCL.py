from cli import configure, cli, pnp
import re
import json
import time

# Set Global variables to be used in later functions
tftp_server = '192.168.200.15'
ftp_server = '192.168.200.15'

### WS-C3650-48PD ###
WS365048PD = 'cat3k_caa-universalk9.16.06.02.SPA.bin'
WS365048PD_md5 = 'ebec919da12d0ac5a49886531b8b82cc'
WS365048PD_ver = '16.6.2'

### C9300-48T ###
C930048T = 'cat9k_iosxe.16.12.04.SPA.bin'
C930048T_md5 = '16e8583ca6184c54f9d9fccf4574fa6e'
C930048T_ver = '16.12.4'

### WS-C3850-48U ###
C385048U = 'cat3k_caa-universalk9.16.09.06.SPA.bin'
C385048U_md5 = '710e1bbaa07b0c8f593af3cab9b5c385'
C385048U_ver = '16.09.06'


def getting_ios_version():
    show_ver = cli('show version')
    version = re.search(r'SW\sVer\w+.*\s[\r\n]+([^\r\n]+)\s[\r\n]+([^\r\n]+)', show_ver).group(2)
    version_detail = re.search(r'\d\s\d+\s+\S+\s+(\S+)', version).group(1)
    print('=> IOS version = ' + version_detail)
    return version_detail


def getting_model():
    dev_model = cli('show version | inc Model')
    mod_detail = re.search(r'Mo\S+\s[N|n]um\S+\s+.\s(.*)', dev_model).group(1)
    print('=> Model = ' + mod_detail)
    return mod_detail


def saving_config():
    write = cli('wr mem')
    if 'OK' in write:
        print('=> Config was saved')
    else:
        print('=> Config was not saved')


def find_certs():
    certs = cli('show run | include crypto pki')
    if certs:
        certs_split = certs.splitlines()
        certs_split.remove('')
        for cert in certs_split:
            command = 'no %s' % (cert)
            configure(command)


def configure_replace(file, file_system='flash:/'):
    config_command = 'configure replace %s%s force' % (file_system, file)
    config_repl = cli(config_command)
    time.sleep(120)
    write_mem = cli('wr mem')
    if 'OK' in write_mem:
        print('=> Config was saved')
    else:
        print('=> Config was not saved')


def check_file_exists(file, file_system='flash:/'):
    dir_check = 'dir ' + file_system + " " + '| inc ' + file
    if len(dir_check):
        # print('=> IOS File is already in flash')
        return False
    else:
        print('=> IOS File is not in flash, starting copy process')
        return True


def deploy_eem_cleanup_script():
    install_command = 'install remove inactive'
    eem_commands = ['event manager applet cleanup',
                    'event none maxrun 600',
                    'action 1.0 cli command "enable"',
                    'action 2.0 cli command "%s" pattern "\[y\/n\]"' % install_command,
                    'action 2.1 cli command "y" pattern "proceed"',
                    'action 2.2 cli command "y"'
                    ]
    results = configure(eem_commands)
    print('*** Successfully configured cleanup EEM script on device! ***')


def deploy_eem_upgrade_script(image):
    install_command = 'install add file flash:' + image + ' activate commit'
    eem_commands = ['event manager applet upgrade',
                    'event none maxrun 600',
                    'action 1.0 cli command "enable"',
                    'action 2.0 cli command "%s" pattern "\[y\/n\/q\]"' % install_command,
                    'action 2.1 cli command "n" pattern "proceed"',
                    'action 2.2 cli command "y"'
                    ]
    results = configure(eem_commands)
    print('*** Successfully configured upgrade EEM script on device! ***')


def get_serial():
    show_ver = cli('show version | inc System')
    sn = re.search(r'Sys\S+\sS\S+\s\w+\s+.\s(.*)', show_ver).group(1)
    return sn


def file_transfer(ftp_server, file, file_system='flash:/'):
    transfer_file = 'copy ftp://anonymous:dfwedfe@' + ftp_server + '/' + file + " " + file_system
    print('Transferring %s to %s' % (file, file_system))
    # transfer_results = cli(transfer_file, expect_string=r'Destination filename')
    transfer_results = cli(transfer_file)
    if 'OK' in transfer_results:
        print('=> file successfully uploaded!!!!')
    else:
        print('=> file upload fail')


def tftp_file_transfer(tftp_server, file, file_system='flash:/'):
    transfer_file = 'copy tftp://' + tftp_server + '/' + file + " " + file_system
    print('Transferring %s to %s' % (file, file_system))
    transfer_results = cli(transfer_file)
    if 'OK' in transfer_results:
        print('=> tftp file successfully uploaded!!!!')
    else:
        print('=> tftp ile upload fail')


def check_ios_md5(file, md5, file_system='flash:/'):
    verify_md5 = 'verify /md5 ' + file_system + file + " " + md5
    md5_result = cli(verify_md5)
    print('Verifying MD5 for ' + file_system + file)
    if 'Verified' in md5_result:
        print('=> IOS file has been verified')
    else:
        print('=> IOS verification failed, process will not continue')
        exit(0)


def main():
    print('###### STARTING ZTP SCRIPT ######')
    print('\n*** Obtaining serial number of device.. ***')
    serial = get_serial()
    print('*** Setting configuration file variable.. ***')
    config_file = "{}.cfg".format(serial)
    print('*** Config file: %s ***' % config_file)
    device_ios = getting_ios_version()
    device_model = getting_model()

    if 'WS-C3650-48PD' in device_model:
        # print('Device model =', device_model)
        # validating IOS version
        if device_ios != WS365048PD_ver:
            print('=> IOS upgrade required')
            # checking IOS on flash
            if not check_file_exists(WS365048PD):
                file_transfer(ftp_server, WS365048PD)
            else:
                print('=> IOS file is already in flash')
            # validation MD5 in ios file
            check_ios_md5(WS365048PD, WS365048PD_md5)

            # upgrading IOS
            print('=> Starting upgrade')
            deploy_eem_upgrade_script(WS365048PD)
            print('*** Performing the upgrade - switch will reboot ***\n')
            cli('event manager run upgrade')
            time.sleep(600)

        else:
            print("=> IOS upgrade isn't required")

            # Cleanup any leftover installation files
            print('*** Deploying Cleanup EEM Script ***')
            deploy_eem_cleanup_script()
            print('*** Running Cleanup EEM Script ***')
            cli('event manager run cleanup')
            time.sleep(30)

            # moving config file into flash
            if not check_file_exists(config_file):
                print('=> Config File is already in flash')

            else:
                file_transfer(ftp_server, config_file)
                time.sleep(17)
                print('*** Removing any existing certs ***')
                find_certs()
                time.sleep(10)

            # replacing config and ssh GEN
            configure_replace(config_file)
            configure('crypto key generate rsa modulus 4096')

            # saving config
            saving_config()

    elif 'C9300-48T' in device_model:
        # print('Device model =', device_model)
        # validating IOS version
        if device_ios != C930048T_ver:
            print('=> IOS upgrade required')
            # checking IOS on flash
            if not check_file_exists(C930048T):
                file_transfer(ftp_server, C930048T)
            else:
                print('=> IOS file is already in flash')
            # validation MD5 in ios file
            check_ios_md5(C930048T, C930048T_md5)

            # upgrading IOS
            print('=> Starting upgrade')
            deploy_eem_upgrade_script(C930048T)
            print('*** Performing the upgrade - switch will reboot ***\n')
            cli('event manager run upgrade')
            time.sleep(600)

        else:
            print("=> IOS upgrade isn't required")

            # Cleanup any leftover installation files
            print('*** Deploying Cleanup EEM Script ***')
            deploy_eem_cleanup_script()
            print('*** Running Cleanup EEM Script ***')
            cli('event manager run cleanup')
            time.sleep(30)

            # moving config file into flash
            if check_file_exists(config_file):
                print('=> Config File is already in flash')

            else:
                tftp_file_transfer(ftp_server, config_file)
                time.sleep(17)
                print('*** Removing any existing certs ***')
                find_certs()
                time.sleep(10)

            # replacing config and ssh GEN
            configure_replace(config_file)
            configure('crypto key generate rsa modulus 4096')

            # saving config
            saving_config()

    elif 'WS-C3850-48U' in device_model:
        # print('Device model =', device_model)
        # validating IOS version
        if device_ios != C385048U_ver:
            print('=> IOS upgrade required')
            # checking IOS on flash
            if not check_file_exists(C385048U):
                file_transfer(ftp_server, C385048U)
            else:
                print('=> IOS file is already in flash')
            # validation MD5 in ios file
            check_ios_md5(C385048U, C385048U_md5)

            # upgrading IOS
            print('=> Starting upgrade')
            deploy_eem_upgrade_script(C385048U)
            print('*** Performing the upgrade - switch will reboot ***\n')
            cli('event manager run upgrade')
            time.sleep(600)

        else:
            print("=> IOS upgrade isn't required")

            # Cleanup any leftover installation files
            print('*** Deploying Cleanup EEM Script ***')
            deploy_eem_cleanup_script()
            print('*** Running Cleanup EEM Script ***')
            cli('event manager run cleanup')
            time.sleep(30)

            # moving config file into flash
            if check_file_exists(config_file):
                print('=> Config File is already in flash')

            else:
                tftp_file_transfer(ftp_server, config_file)
                time.sleep(17)
                print('*** Removing any existing certs ***')
                find_certs()
                time.sleep(10)

            # replacing config and ssh GEN
            configure_replace(config_file)
            configure('crypto key generate rsa modulus 4096')

            # saving config
            saving_config()


if __name__ in "__main__":
    main()
