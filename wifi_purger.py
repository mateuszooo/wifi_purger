#!/usr/bin/python

import sys, getopt
from context import *
def main(argv):
   inputfile = ''
   main_menu()


def main_menu():
    tool_context = context('2137')
    while(True):
        print("1. Deauth attack")
        print('2. Attack TCP SYN')

        print('3  Reconnaissance mode')
        print('4  Take gateway address')
        print('Q  Quit')
        menu_key = input('Select option\n')

        if(menu_key == "Q" or menu_key == 'q'):
            sys.exit(0)
        if(menu_key == "4"):
            tool_context.get_gateway_ip_addr()
        if(menu_key == "2"):
            tool_context.tcp_syn_attack()
        if(menu_key == "3"):
            tool_context.recoissance()
        if(menu_key == '5'):
            tool_context.deauth_ap_attack()

if __name__ == "__main__":
   main(sys.argv[1:])