from netmiko import ConnectHandler, NetmikoAuthenticationException
import re
import funtions_jose
import logging

if __name__ == '__main__':

    # connecting to device
    ip = '10.125.6.1'
    JC = funtions_jose.if_credential_connection(ip)
    net_connect = ConnectHandler(**JC)
    net_connect.enable()

    logging.basicConfig(filename='test.log', level=logging.DEBUG)
    logger = logging.getLogger("my_log")
    logger.debug('This message should go to the log file')

    # getting details from host
    hostname_fz = net_connect.send_command('sh run | inc hostname')
    print('=> Hostname is:', re.search(r'host\w+\s(.*)', hostname_fz).group(1))

    # connecting to non-routable devices
    connect_cmd = 'ssh -l ccl 10.28.128.40'
    password = 'N@v!gaT!nG~\n'
    connect = net_connect.send_command(connect_cmd, expect_string=r'Password:', read_timeout=603)
    try:
        connect += net_connect.send_command(password, expect_string=r'#', read_timeout=603)
    except:
        raise

    hostname = net_connect.send_command('sh run | inc hostname')
    print(hostname)
