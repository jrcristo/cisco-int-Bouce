from netmiko import ConnectHandler
import getpass
import re
import funtions_jose
from snmp_helper import snmp_get_oid, snmp_extract

print('==> script to show WLC general info <==')

if __name__ == '__main__':

    wlc = ['10.121.199.225', '10.120.7.225', '10.120.71.225', '10.121.7.225', '10.121.71.225', '10.122.199.226',
           '10.122.7.225', '10.120.135.225', '10.124.154.225', '10.5.144.10', '10.5.160.10', '10.123.7.225',
           '10.123.71.225', '10.123.135.225', '10.125.7.225']

    yes_option = ['yes', 'y']
    no_option = ['no', 'n']

    all_wlc = input("==> do you want to check one SHIP or all, (Y) to ONE (N) to all:").lower()

    if all_wlc in yes_option:
        print("==> Checking one SHIP")

        ship = input("What's the SHIP code: ").upper()
        try:
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
            ex = re.match('^EX', ship)
            xp = re.match('^XP', ship)
            pev2 = re.match('^PEV', ship)
            prc = re.match('^PRC', ship)

        except AttributeError:
            pass

        try:
            if yp.group():
                print('==> Sky WLC <==')
                ip = '10.125.7.225'
                community = 'msdp725'
                # getting snmp
                funtions_jose.check_wlc_snmp(ip, community)

        except AttributeError:
            pass

        try:
            if gp.group():
                print('==> Regal WLC <==')
                ip = '10.122.199.226'
                community = 'msdp725'
                # getting snmp
                funtions_jose.check_wlc_snmp(ip, community)

        except AttributeError:
            pass

        try:
            if rp.group():
                print('==> Royal WLC <==')
                ip = '10.123.7.225'
                community = 'msdp725'
                # getting snmp
                funtions_jose.check_wlc_snmp(ip, community)

        except AttributeError:
            pass

        try:
            if mj.group():
                print('==> Majestic WLC <==')
                ip = '10.124.154.225'
                community = 'msdp725'
                # getting snmp
                funtions_jose.check_wlc_snmp(ip, community)

        except AttributeError:
            pass

        try:
            if ap.group():
                print('==> Grand WLC <==')
                ip = '10.121.199.225'
                community = 'msdp725'
                # getting snmp
                funtions_jose.check_wlc_snmp(ip, community)

        except AttributeError:
            pass

        try:
            if cb.group():
                print('==> Caribbean WLC <==')
                ip = '10.120.7.225'
                community = 'msdp725'
                # getting snmp
                funtions_jose.check_wlc_snmp(ip, community)

        except AttributeError:
            pass

        try:
            if co.group():
                print('==> Coral WLC <==')
                ip = '10.120.71.225'
                community = 'msdp725'
                # getting snmp
                funtions_jose.check_wlc_snmp(ip, community)

        except AttributeError:
            pass

        try:
            if di.group():
                print('==> Diamond WLC <==')
                ip = '10.121.7.225'
                community = 'msdp725'
                # getting snmp
                funtions_jose.check_wlc_snmp(ip, community)

        except AttributeError:
            pass

        try:
            if ep.group():
                print('==> Emerald WLC <==')
                ip = '10.121.71.225'
                community = 'msdp725'
                # getting snmp
                funtions_jose.check_wlc_snmp(ip, community)

        except AttributeError:
            pass

        try:
            if kp.group():
                print('==> Crown WLC <==')
                ip = '10.120.135.225'
                community = 'msdp725'
                # getting snmp
                funtions_jose.check_wlc_snmp(ip, community)

        except AttributeError:
            pass

        try:
            if ip.group():
                print('==> Island WLC <==')
                ip = '10.122.7.225'
                community = 'msdp725'
                # getting snmp
                funtions_jose.check_wlc_snmp(ip, community)

        except AttributeError:
            pass

        try:
            if ru.group():
                print('==> Ruby WLC <==')
                ip = '10.123.71.225'
                community = 'msdp725'
                # getting snmp
                funtions_jose.check_wlc_snmp(ip, community)

        except AttributeError:
            pass

        try:
            if sa.group():
                print('==> SA WLC <==')
                ip = '10.123.135.225'
                community = 'msdp725'
                # getting snmp
                funtions_jose.check_wlc_snmp(ip, community)

        except AttributeError:
            pass

        try:
            if pev2.group():
                print('==> Port Everglades WLC <==')
                ip = '10.5.144.10'
                community = 'Ic3L@nD'
                # getting snmp
                funtions_jose.check_wlc_snmp(ip, community)

        except AttributeError:
            pass

        try:
            if prc.group():
                print('==> Princess Cays WLC <==')
                ip = '10.5.160.10'
                community = 'Ic3L@nD'
                # getting snmp
                funtions_jose.check_wlc_snmp(ip, community)

        except AttributeError:
            pass

    elif all_wlc in no_option:
        print("==> Checking all the WLCs <==")
        for j in wlc:
            if '10.5.160.10' in j or '10.5.144.10' in j:
                community = 'Ic3L@nD'
                funtions_jose.check_wlc_snmp(j, community)
            else:
                community = 'msdp725'
                funtions_jose.check_wlc_snmp(j, community)



