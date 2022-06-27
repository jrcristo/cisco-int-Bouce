import netmiko
import getpass

from netmiko import ConnectHandler

import funtions_jose
import os


path = os.path.join("C:\\", "Jose", "python_ouput", str(funtions_jose.get_time_date()[0]), 'test.txt')



# file = funtions_jose.create_folder_logs()[0]
print(funtions_jose.create_folder_logs())





