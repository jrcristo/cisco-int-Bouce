import time
from netmiko import ConnectHandler
import funtions_jose
import re

print('==> Script to enable && || disable packet capture <==')

# getting time
date = funtions_jose.get_time_date()
print(date[1])

if __name__ == '__main__':

    yes_option = ['yes', 'y']
    no_option = ['no', 'n']

    # connecting to the device
    JC = funtions_jose.get_credentials_and_interface()
    net_connect = ConnectHandler(**JC)
    net_connect.enable()

    # check and remove packet capture

    # create the packet capture
    inter = str(input("==> Enter the interface or VLAN you want to capture<==: ")).lower()

    # getting hostname and removing PCL from the name
    dev_name = net_connect.send_command('sh run' + " " + '| inc hostname')
    host = re.search(r'host\w+\s(.*)', dev_name)
    xx = re.search(r'PCL(\w{1,3})', host.group(1))

    # check and remove pcap file from flash
    check_file = net_connect.send_command('sh flash:' + " " + '| inc' + " " + xx.group(1) + '_capture.pcap')
    if check_file:
        print('==> Old capture file found it on the flash, preparing to remove it')
        delete = 'delete flash:' + xx.group(1) + '_capture.pcap'
        delete_file = net_connect.send_command(delete, expect_string=r'Delete filename')
        try:
            delete_file += net_connect.send_command('\n', expect_string=r'Delete flash:/'+xx.group(1)+'_capture.pcap?')
            delete_file += net_connect.send_command('\n', expect_string=r'#')
        except:
            raise
        # checking again flash on file
        check_file_after = net_connect.send_command('sh flash:' + " " + '| inc' + " " + xx.group(1) + '_capture.pcap')
        if check_file_after:
            print('==> File' + " " + xx.group(1) + '_capture.pcap' + " " + 'could not been removed')
        else:
            print('==> File' + " " + xx.group(1) + '_capture.pcap' + " " + 'has been removed')

    else:
        print('==> NO old capture .pcap file found on flash')

    # checking and removing JC_XX from switch
    removing_capture = net_connect.send_command('no monitor capture' + " " + 'JC_' + xx.group(1))

    # creating the capture
    capture = net_connect.send_command('monitor capture' + " " + 'JC_' + xx.group(
        1) + " " + 'buffer size 50 vlan' + " " + inter + " " + 'both match any')
    # checking the capture
    capture_check = net_connect.send_command('show monitor capture' + " " + 'JC_' + xx.group(1))
    if 'JC_' + xx.group(1) in capture_check:
        print('=> Capture on int||Vlan' + " " + inter + " " + 'has been created')
    else:
        print('=> Capture was not created')

    # capture_location = net_connect.send_command('monitor capture' + " " + 'JC_' + xx.group(1) + " " + 'file location flash:' + xx.group(1) + '_capture.pcap')
    # cmd = 'monitor capture JC_SA file location flash:SA_capture.pcap'
    cmd = 'monitor capture' + " " + 'JC_' + xx.group(1) + " " + 'file location flash:' + xx.group(1) + '_capture.pcap'
    capture_location = net_connect.send_command(cmd,
                                                expect_string=r'Buffer is already associated to this Capture want to configure File')
    try:
        capture_location += net_connect.send_command('\n', expect_string=r'#')

    except:
        raise

    capture_location_check = net_connect.send_command(
        'show monitor capture' + " " + 'JC_' + xx.group(1) + " " + '| inc name')
    capture_location_result = re.search(r'Ass\w+\s\w+\sn\w+.\s(.*)', capture_location_check)

    # checking the capture location
    if xx.group(1) + '_capture.pcap' in capture_location_check:
        print('=> Location created successfully =>' + " " + capture_location_result.group(1))
    else:
        print('=> location creation failed')

    # Starting the capture
    # waiting XX second in order to stop the capture
    timer = int(input("==> Enter time in seconds for packet capture running <==: "))

    capture_start = net_connect.send_command('monitor capture' + " " + 'JC_' + xx.group(1) + " " + 'start')
    # checking if the capture started
    if 'Started' in capture_start:
        print('==> Capture has started')
    else:
        print('=> Capture has not started')

    # Waiting
    time.sleep(timer)
    # print('=> Capture will run for ' + " " + str(timer) + " " + 'seconds')

    # stopping the capture
    stop = net_connect.send_command('monitor capture' + " " + 'JC_' + xx.group(1) + " " + 'stop')
    if 'statistics' in stop:
        print('=> Capture has been stopped')

    # showing results
    capture_duration = re.search(r'Capt\w+\sd.*', stop)
    pkts_rcvd = re.search(r'Pa\w+\sre.*', stop)
    if capture_duration.group():
        print(capture_duration.group())
    else:
        print('=> Packet Duration = 0')

    if pkts_rcvd.group():
        print(pkts_rcvd.group())
    else:
        print('=> Packets Received = 0')

    # Asking to copy the file to JC tftp
    copy_JC = input("==> Jose, do you want to copy the pcap file to your personal TFTP,(Y) to continue (N) to cancel:").lower()
    if copy_JC in yes_option:
        tftp = str(input("==> Enter the tftp ip address <==: "))
        copy_cmd = 'copy flash: tftp'
        copy_file = net_connect.send_command(copy_cmd, expect_string=r'Source filename')
        try:
            copy_file += net_connect.send_command(xx.group(1)+'_capture.pcap', expect_string=r'Address or name of remote host')
            copy_file += net_connect.send_command(tftp, expect_string=r'Destination filename')
            copy_file += net_connect.send_command('\n', expect_string=r'#')
        except:
            raise
    elif copy_JC in no_option:
        print('==> No files will be copied')