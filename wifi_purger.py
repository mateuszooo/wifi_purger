#!/usr/bin/python

import sys, getopt

def main(argv):
   inputfile = ''
   main_menu()


def main_menu():
    while(True):
        print("1. Deauth attack")
        print('2. Attack')
        print('Q  Quit')

        menu_key = input('Select option')

        if(menu_key == "Q" or menu_key == 'q'):
            sys.exit(0)





if __name__ == "__main__":
   main(sys.argv[1:])