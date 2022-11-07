from cli import configure, cli, pnp
import re


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


def get_serial():
    show_ver = cli('show version | inc System')
    sn = re.findall(r'Syst\S+\sSer\w+\sNum\S+\s+.\s(.*)', show_ver).group(1)
    print(sn)
    return sn


def main():

    JC = funtions_jose.get_credentials_and_interface()
    net_connect = ConnectHandler(**JC)
    net_connect.enable()

    print('###### STARTING ZTP SCRIPT ######')
    print('\n*** Obtaining serial number of device.. ***')
    serial = get_serial()
    print('*** Setting configuration file variable.. ***')
    config_file = "{}.cfg".format(serial)
    print('*** Config file: %s ***' % config_file)
    device_ios = getting_ios_version()
    device_model = getting_model()


if __name__ in "__main__":
    main()
