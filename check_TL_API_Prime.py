from netmiko import ConnectHandler
import getpass
import re
import funtions_jose
import requests
import json
from argparse import ArgumentParser

print('==> script to check switch from IDF <==')

if __name__ == '__main__':

    tl_name = input("What's the TL name: ")

    # validation and addition of domain
    if re.match(r'PCLXP', tl_name):
        tl_name = tl_name + '.xp.cruises.princess.com'
    elif re.match(r'PCLEX', tl_name):
        tl_name = tl_name + '.ex.cruises.princess.com'
    elif re.match(r'PCLYP', tl_name):
        tl_name = tl_name + '.yp.cruises.princess.com'
    elif re.match(r'PCLGP', tl_name):
        tl_name = tl_name + '.gp.cruises.princess.com'
    elif re.match(r'PCLRP', tl_name):
        tl_name = tl_name + '.rp.cruises.princess.com'
    elif re.match(r'PCLMJ', tl_name):
        tl_name = tl_name + '.mj.cruises.princess.com'
    elif re.match(r'PCLAP', tl_name):
        tl_name = tl_name + '.ap.cruises.princess.com'
    elif re.match(r'PCLCB', tl_name):
        tl_name = tl_name + '.cb.cruises.princess.com'
    elif re.match(r'PCLCO', tl_name):
        tl_name = tl_name + '.co.cruises.princess.com'
    elif re.match(r'PCLDI', tl_name):
        tl_name = tl_name + '.di.cruises.princess.com'
    elif re.match(r'PCLEP', tl_name):
        tl_name = tl_name + '.ep.cruises.princess.com'
    elif re.match(r'PCLKP', tl_name):
        tl_name = tl_name + '.kp.cruises.princess.com'
    elif re.match(r'PCLIP', tl_name):
        tl_name = tl_name + '.ip.cruises.princess.com'
    elif re.match(r'PCLRU', tl_name):
        tl_name = tl_name + '.ru.cruises.princess.com'
    elif re.match(r'PCLSA', tl_name):
        tl_name = tl_name + '.SA.cruises.princess.com'

    # I don't need domain anymore, but I won't change the code. LAZY day. I'm sorry.

    # checking with prime for details
    try:
        xp = re.match('^PCLXP', tl_name)
        ex = re.match('^PCLEX', tl_name)
        yp = re.match('^PCLYP', tl_name)
        gp = re.match('^PCLGP', tl_name)
        rp = re.match('^PCLRP', tl_name)
        mj = re.match('^PCLMJ', tl_name)
        ap = re.match('^PCLAP', tl_name)
        cb = re.match('^PCLCB', tl_name)
        co = re.match('^PCLCO', tl_name)
        di = re.match('^PCLDI', tl_name)
        ep = re.match('^PCLEP', tl_name)
        kp = re.match('^PCLKP', tl_name)
        ip = re.match('^PCLIP', tl_name)
        ru = re.match('^PCLRU', tl_name)
        sa = re.match('^PCLSA', tl_name)
        pev2 = re.match('^PEV', tl_name)

    except AttributeError:
        pass

    try:
        if xp.group():
            pi_ip = '10.125.164.196'
            domain = '.xp.cruises.princess.com'
            print('=> Trying to get info from Discovery Prime ' + pi_ip)
            # connecting PI
            funtions_jose.cisco_prime_api_results_devices(tl_name, pi_ip, domain, net_connect=False)
            exit(0)

    except AttributeError:
        pass

    try:
        if ex.group():
            pi_ip = '10.125.100.196'
            domain = '.ex.cruises.princess.com'
            print('=> Trying to get info from Enchanted Prime ' + pi_ip)
            # connecting PI
            funtions_jose.cisco_prime_api_results_devices(tl_name, pi_ip, domain, net_connect=False)
            exit(0)

    except AttributeError:
        pass

    try:
        if yp.group():
            pi_ip = '10.125.36.196'
            domain = '.yp.cruises.princess.com'
            print('=> Trying to get info from Sky Prime ' + pi_ip)
            # connecting PI
            funtions_jose.cisco_prime_api_results_devices(tl_name, pi_ip, domain, net_connect=False)
            exit(0)

    except AttributeError:
        pass

    try:
        if gp.group():
            pi_ip = '10.122.227.196'
            domain = '.gp.cruises.princess.com'
            print('=> Trying to get info from Regal Prime ' + pi_ip)
            # connecting PI
            funtions_jose.cisco_prime_api_results_devices(tl_name, pi_ip, domain, net_connect=False)
            exit(0)

    except AttributeError:
        pass

    try:
        if rp.group():
            pi_ip = '10.123.36.196'
            domain = '.rp.cruises.princess.com'
            print('=> Trying to get info from Royal Prime ' + pi_ip)
            # connecting PI
            funtions_jose.cisco_prime_api_results_devices(tl_name, pi_ip, domain, net_connect=False)
            exit(0)

    except AttributeError:
        pass

    try:
        if mj.group():
            pi_ip = '10.124.164.196'
            domain = '.mj.cruises.princess.com'
            print('=> Trying to get info from Majestic Prime ' + pi_ip)
            # connecting PI
            funtions_jose.cisco_prime_api_results_devices(tl_name, pi_ip, domain, net_connect=False)
            exit(0)

    except AttributeError:
        pass

    try:
        if ap.group():
            pi_ip = '10.121.228.196'
            domain = '.ap.cruises.princess.com'
            print('=> Trying to get info from Grand Prime ' + pi_ip)
            # connecting PI
            funtions_jose.cisco_prime_api_results_devices(tl_name, pi_ip, domain, net_connect=False)
            exit(0)

    except AttributeError:
        pass

    try:
        if cb.group():
            pi_ip = '10.120.36.196'
            domain = '.cb.cruises.princess.com'
            print('=> Trying to get info from Caribbean Prime ' + pi_ip)
            # connecting PI
            funtions_jose.cisco_prime_api_results_devices(tl_name, pi_ip, domain, net_connect=False)
            exit(0)

    except AttributeError:
        pass

    try:
        if co.group():
            pi_ip = '10.120.100.196'
            domain = '.co.cruises.princess.com'
            print('=> Trying to get info from Coral Prime ' + pi_ip)
            # connecting PI
            funtions_jose.cisco_prime_api_results_devices(tl_name, pi_ip, domain, net_connect=False)
            exit(0)

    except AttributeError:
        pass

    try:
        if di.group():
            pi_ip = '10.121.36.196'
            domain = '.di.cruises.princess.com'
            print('=> Trying to get info from Diamond Prime ' + pi_ip)
            # connecting PI
            funtions_jose.cisco_prime_api_results_devices(tl_name, pi_ip, domain, net_connect=False)
            exit(0)

    except AttributeError:
        pass

    try:
        if ep.group():
            pi_ip = '10.121.100.196'
            domain = '.ep.cruises.princess.com'
            print('=> Trying to get info from Emerald Prime ' + pi_ip)
            # connecting PI
            funtions_jose.cisco_prime_api_results_devices(tl_name, pi_ip, domain, net_connect=False)
            exit(0)

    except AttributeError:
        pass

    try:
        if kp.group():
            pi_ip = '10.120.164.196'
            domain = '.kp.cruises.princess.com'
            print('=> Trying to get info from Crown Prime at ' + pi_ip)
            # connecting PI
            funtions_jose.cisco_prime_api_results_devices(tl_name, pi_ip, domain, net_connect=False)
            exit(0)

    except AttributeError:
        pass

    try:
        if ip.group():
            pi_ip = '10.122.36.196'
            domain = '.ip.cruises.princess.com'
            print('=> Trying to get info from Island Prime at ' + pi_ip)
            # connecting PI
            funtions_jose.cisco_prime_api_results_devices(tl_name, pi_ip, domain, net_connect=False)
            exit(0)

    except AttributeError:
        pass

    try:
        if ru.group():
            pi_ip = '10.123.100.196'
            domain = '.ru.cruises.princess.com'
            print('=> Trying to get info from Ruby Prime at ' + pi_ip)
            # connecting PI
            funtions_jose.cisco_prime_api_results_devices(tl_name, pi_ip, domain, net_connect=False)
            exit(0)

    except AttributeError:
        pass

    try:
        if sa.group():
            pi_ip = '10.123.164.196'
            domain = '.sa.cruises.princess.com'
            print('=> Trying to get info from Sapphire Prime at ' + pi_ip)
            # connecting PI
            funtions_jose.cisco_prime_api_results_devices(tl_name, pi_ip, domain, net_connect=False)
            exit(0)

    except AttributeError:
        pass

    try:
        if pev2.group():
            print('=> There is no Prime for PEv2')
            exit(0)

    except AttributeError:
        pass

