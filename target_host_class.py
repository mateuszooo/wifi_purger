class target_host_class:
    def __init__(self, mac_adr,ipv4_adr):
        self.mac_addres = mac_adr
        self.ipv4_address = ipv4_adr



    def get_info(self):
        print('#'*80 + '\n')
        print('MAC: ' + self.mac_addres)
        print('IPv4: ' + self.ipv4_address)