from snmp_helper import snmp_get_oid, snmp_extract
import funtions_jose

print('==> Script to check WLC values <==')

wlc = ['10.121.199.225', '10.120.7.225', '10.120.71.225', '10.121.7.225', '10.121.71.225', '10.122.199.226', '10.122.7.225', '10.120.135.225', '10.124.154.225', '10.5.144.10', '10.5.160.10', '10.123.7.225', '10.123.71.225', '10.123.135.225', '10.125.7.225']

name = None

# loog to get the values
print('*---*-*---*-*---*-*---*')
for j in wlc:
    COMMUNITY_STRING = 'msdp725'
    SNMP_PORT = 161
    a_device = (j, COMMUNITY_STRING, SNMP_PORT)
    print('==> Date =', funtions_jose.get_time_date()[0], '=> Time =', funtions_jose.get_time_date()[1])
    try:
        if snmp_get_oid(a_device, oid='.1.3.6.1.2.1.1.5.0', display_errors=True):
            name = snmp_get_oid(a_device, oid='.1.3.6.1.2.1.1.5.0', display_errors=True)
            name_output = snmp_extract(name)
            print('==> WLC name =', name_output)

        if snmp_get_oid(a_device, oid='1.3.6.1.4.1.9.9.618.1.8.4.0', display_errors=True):
            total_ap = snmp_get_oid(a_device, oid='1.3.6.1.4.1.9.9.618.1.8.4.0', display_errors=True)
            total_output = snmp_extract(total_ap)
            print('==> Total AP joined WLC =', total_output)

        if snmp_get_oid(a_device, oid='1.3.6.1.4.1.9.9.618.1.8.12.0', display_errors=True):
            total_clients = snmp_get_oid(a_device, oid='1.3.6.1.4.1.9.9.618.1.8.12.0', display_errors=True)
            clients_output = snmp_extract(total_clients)
            print('==> Total Clients Connected to WLC =', clients_output)

        if 'PCLAP' in name_output:
            ap_mednet = '5'
            ap_crewnet = '9'
            ap_crew_compass = '6'
            if snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.5', display_errors=True):
                mednet_ap = snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.5', display_errors=True)
                mednet_ap_output = snmp_extract(mednet_ap)
                print('==> Total Clients connected to MedNet =', mednet_ap_output)
            if snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.9', display_errors=True):
                crewnet_ap = snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.9', display_errors=True)
                crewnet_ap_output = snmp_extract(crewnet_ap)
                print('==> Total Clients connected to CrewNet =', crewnet_ap_output)
            if snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.6', display_errors=True):
                crew_compass_ap = snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.6', display_errors=True)
                crew_compass_ap_output = snmp_extract(crew_compass_ap)
                print('==> Total Clients connected to CrewCompass =', crew_compass_ap_output)

        if 'PCLCB' in name_output:
            cb_mednet = '13'
            cb_crewnet = '14'
            cb_crew_compass = '16'
            if snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.13', display_errors=True):
                mednet_cb = snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.13', display_errors=True)
                mednet_cb_output = snmp_extract(mednet_cb)
                print('==> Total Clients connected to MedNet =', mednet_cb_output)
            if snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.14', display_errors=True):
                crewnet_cb = snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.14', display_errors=True)
                crewnet_cb_output = snmp_extract(crewnet_cb)
                print('==> Total Clients connected to CrewNet =', crewnet_cb_output)
            if snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.16', display_errors=True):
                crew_compass_cb = snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.16', display_errors=True)
                crew_compass_cb_output = snmp_extract(crew_compass_cb)
                print('==> Total Clients connected to CrewCompass =', crew_compass_cb_output)

        if 'PCLCO' in name_output:
            cb_mednet = '11'
            cb_crewnet = '12'
            cb_crew_compass = '14'
            if snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.11', display_errors=True):
                mednet_co = snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.11', display_errors=True)
                mednet_co_output = snmp_extract(mednet_co)
                print('==> Total Clients connected to MedNet =', mednet_co_output)
            if snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.12', display_errors=True):
                crewnet_co = snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.12', display_errors=True)
                crewnet_co_output = snmp_extract(crewnet_co)
                print('==> Total Clients connected to CrewNet =', crewnet_co_output)
            if snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.14', display_errors=True):
                crew_compass_co = snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.14', display_errors=True)
                crew_compass_co_output = snmp_extract(crew_compass_co)
                print('==> Total Clients connected to CrewCompass =', crew_compass_co_output)

        if 'PCLDI' in name_output:
            cb_mednet = '13'
            cb_crewnet = '14'
            cb_crew_compass = '9'
            if snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.13', display_errors=True):
                mednet_di = snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.13', display_errors=True)
                mednet_di_output = snmp_extract(mednet_di)
                print('==> Total Clients connected to MedNet =', mednet_di_output)
            if snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.14', display_errors=True):
                crewnet_di = snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.14', display_errors=True)
                crewnet_di_output = snmp_extract(crewnet_di)
                print('==> Total Clients connected to CrewNet =', crewnet_di_output)
            if snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.9', display_errors=True):
                crew_compass_di = snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.9', display_errors=True)
                crew_compass_di_output = snmp_extract(crew_compass_di)
                print('==> Total Clients connected to CrewCompass =', crew_compass_di_output)

        if 'PCLEP' in name_output:
            cb_mednet = '12'
            cb_crewnet = '14'
            cb_crew_compass = '8'
            if snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.12', display_errors=True):
                mednet_ep = snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.12', display_errors=True)
                mednet_ep_output = snmp_extract(mednet_ep)
                print('==> Total Clients connected to MedNet =', mednet_ep_output)
            if snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.14', display_errors=True):
                crewnet_ep = snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.14', display_errors=True)
                crewnet_ep_output = snmp_extract(crewnet_ep)
                print('==> Total Clients connected to CrewNet =', crewnet_ep_output)
            if snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.8', display_errors=True):
                crew_compass_ep = snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.8', display_errors=True)
                crew_compass_ep_output = snmp_extract(crew_compass_ep)
                print('==> Total Clients connected to CrewCompass =', crew_compass_ep_output)

        if 'PCLGP' in name_output:
            gp_mednet = '14'
            gp_crewnet = '15'
            gp_crew_compass = '19'
            if snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.14', display_errors=True):
                mednet_gp = snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.14', display_errors=True)
                mednet_gp_output = snmp_extract(mednet_gp)
                print('==> Total Clients connected to MedNet =', mednet_gp_output)
            if snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.15', display_errors=True):
                crewnet_gp = snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.15', display_errors=True)
                crewnet_gp_output = snmp_extract(crewnet_gp)
                print('==> Total Clients connected to CrewNet =', crewnet_gp_output)
            if snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.19', display_errors=True):
                crew_compass_gp = snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.19', display_errors=True)
                crew_compass_gp_output = snmp_extract(crew_compass_gp)
                print('==> Total Clients connected to CrewCompass =', crew_compass_gp_output)

        if 'PCLIP' in name_output:
            ip_mednet = '9'
            ip_crewnet = '12'
            ip_crew_compass = '16'
            if snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.9', display_errors=True):
                mednet_ip = snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.9', display_errors=True)
                mednet_ip_output = snmp_extract(mednet_ip)
                print('==> Total Clients connected to MedNet =', mednet_ip_output)
            if snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.12', display_errors=True):
                crewnet_ip = snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.12', display_errors=True)
                crewnet_ip_output = snmp_extract(crewnet_ip)
                print('==> Total Clients connected to CrewNet =', crewnet_ip_output)
            if snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.16', display_errors=True):
                crew_compass_ip = snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.16', display_errors=True)
                crew_compass_ip_output = snmp_extract(crew_compass_ip)
                print('==> Total Clients connected to CrewCompass =', crew_compass_ip_output)

        if 'PCLKP' in name_output:
            kp_mednet = '14'
            kp_crewnet = '15'
            kp_crew_compass = '13'
            if snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.14', display_errors=True):
                mednet_kp = snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.14', display_errors=True)
                mednet_kp_output = snmp_extract(mednet_kp)
                print('==> Total Clients connected to MedNet =', mednet_kp_output)
            if snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.15', display_errors=True):
                crewnet_kp = snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.15', display_errors=True)
                crewnet_kp_output = snmp_extract(crewnet_kp)
                print('==> Total Clients connected to CrewNet =', crewnet_kp_output)
            if snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.13', display_errors=True):
                crew_compass_kp = snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.13', display_errors=True)
                crew_compass_kp_output = snmp_extract(crew_compass_kp)
                print('==> Total Clients connected to CrewCompass =', crew_compass_kp_output)

        if 'PCLMJ' in name_output:
            mj_mednet = '9'
            mj_crewnet = '10'
            mj_crew_compass = '11'
            if snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.9', display_errors=True):
                mednet_mj = snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.9', display_errors=True)
                mednet_mj_output = snmp_extract(mednet_mj)
                print('==> Total Clients connected to MedNet =', mednet_mj_output)
            if snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.10', display_errors=True):
                crewnet_mj = snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.10', display_errors=True)
                crewnet_mj_output = snmp_extract(crewnet_mj)
                print('==> Total Clients connected to CrewNet =', crewnet_mj_output)
            if snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.10', display_errors=True):
                crew_compass_mj = snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.10', display_errors=True)
                crew_compass_mj_output = snmp_extract(crew_compass_mj)
                print('==> Total Clients connected to CrewCompass =', crew_compass_mj_output)

        if 'PLC-PEV2' in name_output:
            pev2_mednet = '1'
            pev2_crewnet = '10'
            pev2_crew_compass = '3'
            if snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.1', display_errors=True):
                mednet_pev2 = snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.1', display_errors=True)
                mednet_pev2_output = snmp_extract(mednet_pev2)
                print('==> Total Clients connected to MedNet =', mednet_pev2_output)
            if snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.3', display_errors=True):
                crew_compass_pev2 = snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.3', display_errors=True)
                crew_compass_pev2_output = snmp_extract(crew_compass_pev2)
                print('==> Total Clients connected to CrewCompass =', crew_compass_pev2_output)

        if 'PCL-PRC' in name_output:
            prc_mednet = '7'
            prc_crewnet = '8'
            prc_crew_compass = '4'
            if snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.7', display_errors=True):
                mednet_prc = snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.7', display_errors=True)
                mednet_prc_output = snmp_extract(mednet_prc)
                print('==> Total Clients connected to MedNet =', mednet_prc_output)
            if snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.8', display_errors=True):
                crewnet_prc = snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.8', display_errors=True)
                crewnet_prc_output = snmp_extract(crewnet_prc)
                print('==> Total Clients connected to CrewNet =', crewnet_prc_output)
            if snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.4', display_errors=True):
                crew_compass_prc = snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.4', display_errors=True)
                crew_compass_prc_output = snmp_extract(crew_compass_prc)
                print('==> Total Clients connected to CrewCompass =', crew_compass_prc_output)

        if 'PCLRP' in name_output:
            rp_mednet = '8'
            rp_crewnet = '9'
            rp_crew_compass = '14'
            if snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.8', display_errors=True):
                mednet_rp = snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.8', display_errors=True)
                mednet_rp_output = snmp_extract(mednet_rp)
                print('==> Total Clients connected to MedNet =', mednet_rp_output)
            if snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.9', display_errors=True):
                crewnet_rp = snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.9', display_errors=True)
                crewnet_rp_output = snmp_extract(crewnet_rp)
                print('==> Total Clients connected to CrewNet =', crewnet_rp_output)
            if snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.14', display_errors=True):
                crew_compass_rp = snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.14', display_errors=True)
                crew_compass_rp_output = snmp_extract(crew_compass_rp)
                print('==> Total Clients connected to CrewCompass =', crew_compass_rp_output)

        if 'PCLRU' in name_output:
            ru_mednet = '16'
            ru_crewnet = '8'
            ru_crew_compass = '14'
            if snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.16', display_errors=True):
                mednet_ru = snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.16', display_errors=True)
                mednet_ru_output = snmp_extract(mednet_ru)
                print('==> Total Clients connected to MedNet =', mednet_ru_output)
            if snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.8', display_errors=True):
                crewnet_ru = snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.8', display_errors=True)
                crewnet_ru_output = snmp_extract(crewnet_ru)
                print('==> Total Clients connected to CrewNet =', crewnet_ru_output)
            if snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.14', display_errors=True):
                crew_compass_ru = snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.14', display_errors=True)
                crew_compass_ru_output = snmp_extract(crew_compass_ru)
                print('==> Total Clients connected to CrewCompass =', crew_compass_ru_output)

        if 'PCLSA' in name_output:
            ru_mednet = '12'
            ru_crewnet = '13'
            ru_crew_compass = '10'
            if snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.12', display_errors=True):
                mednet_sa = snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.12', display_errors=True)
                mednet_sa_output = snmp_extract(mednet_sa)
                print('==> Total Clients connected to MedNet =', mednet_sa_output)
            if snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.13', display_errors=True):
                crewnet_sa = snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.13', display_errors=True)
                crewnet_sa_output = snmp_extract(crewnet_sa)
                print('==> Total Clients connected to CrewNet =', crewnet_sa_output)
            if snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.10', display_errors=True):
                crew_compass_sa = snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.10', display_errors=True)
                crew_compass_sa_output = snmp_extract(crew_compass_sa)
                print('==> Total Clients connected to CrewCompass =', crew_compass_sa_output)

        if 'PCLYP' in name_output:
            ru_mednet = '4'
            ru_crewnet = '5'
            ru_crew_compass = '6'
            if snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.4', display_errors=True):
                mednet_yp = snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.4', display_errors=True)
                mednet_yp_output = snmp_extract(mednet_yp)
                print('==> Total Clients connected to MedNet =', mednet_yp_output)
            if snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.5', display_errors=True):
                crewnet_yp = snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.5', display_errors=True)
                crewnet_yp_output = snmp_extract(crewnet_yp)
                print('==> Total Clients connected to CrewNet =', crewnet_yp_output)
            if snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.6', display_errors=True):
                crew_compass_yp = snmp_get_oid(a_device, oid='1.3.6.1.4.1.14179.2.1.1.1.38.6', display_errors=True)
                crew_compass_yp_output = snmp_extract(crew_compass_yp)
                print('==> Total Clients connected to CrewCompass =', crew_compass_yp_output)

    except TypeError:
        pass
    print('*---*-*---*-*---*-*---*')


