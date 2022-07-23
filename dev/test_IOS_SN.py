from netmiko import ConnectHandler
import funtions_jose
import re

# getting time
date = funtions_jose.get_time_date()
print(date[1])

if __name__ == '__main__':

    tftp_server = '10.228.35.168'
    ftp_server = '10.228.35.168'

    def getting_ios_version():
        show_ver = net_connect.send_command('show version')
        # show_ver = cli('show version')
        version = re.search(r'SW\sVer\w+.*\s[\r\n]+([^\r\n]+)\s[\r\n]+([^\r\n]+)', show_ver).group(2)
        version_detail = re.search(r'\d\s\d+\s+\S+\s+(\S+)', version).group(1)
        print('=> IOS version = ' + version_detail)
        return version_detail


    def getting_model():
        dev_model = net_connect.send_command('show version | inc Model')
        # dev_model = cli('show version | inc Model')
        mod_detail = re.search(r'Mo\S+\s[N|n]um\S+\s+.\s(.*)', dev_model).group(1)
        print('=> Model = ' + mod_detail)
        return mod_detail


    def get_serial():
        show_ver = net_connect.send_command('show version | inc System')
        # show_ver = cli('show version | inc System')
        sn = re.findall(r'Syst\S+\sSer\w+\sNum\S+\s+.\s(.*)', show_ver)
        # print(sn)
        return sn


    def file_transfer(ftp_server, file, file_system='flash:/'):
        transfer_file = 'copy ftp://anonymous:dfwedfe@' + ftp_server + '/' + file + " " + file_system
        print('Transferring %s to %s' % (file, file_system))
        # transfer_results = cli(transfer_file, expect_string=r'Destination filename')
        transfer_results = net_connect.send_command(transfer_file)
        # transfer_results = cli(transfer_file)
        if 'OK' in transfer_results:
            print('=> file successfully uploaded!!!!')
        else:
            print('=> file upload fail')


    JC = funtions_jose.get_credentials_and_interface()
    net_connect = ConnectHandler(**JC)
    net_connect.enable()

    print('###### STARTING ZTP SCRIPT ######')
    print('\n*** Obtaining serial number of device.. ***')
    serial = get_serial()
    # checking what's the SN.cfg on file
    for m in serial:
        print('=> Testing ', m)
        transfer_file = 'copy tftp://' + tftp_server + '/' + m+'.cfg' + " " + 'flash:/'
        transfer_results = net_connect.send_command(transfer_file, expect_string=r'Destination filename')
        transfer_results += net_connect.send_command('\n', expect_string=r'#')
        if 'OK' in transfer_results:
            print('=> File was copied to Flash!!!')
            new_ser = m
            break
        elif 'No such file or directory' in transfer_results:
            pass

    print('*** Setting configuration file variable.. ***')
    config_file = "{}.cfg".format(new_ser)
    print('*** Config file: %s ***' % config_file)
    device_ios = getting_ios_version()
    device_model = getting_model()


