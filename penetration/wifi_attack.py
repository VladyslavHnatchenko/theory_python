import socket

from scapy.all import *
from scapy.layers.dot11 import Dot11ProbeReq

probe_list = []

ap_name = input("Enter the name of access point ")


def probe_info(pkt):
    if pkt.haslayer(Dot11ProbeReq):
        client_name = pkt.info

        if client_name == ap_name:
            if pkt.addr2 not in probe_info:
                print("New Probe request - -", client_name)
                print("MAC is --", pkt.addr2)
                probe_list.append(pkt.addr2)


sniff(iface="mon0", prn=probe_info)

# ------------------------------------------------------------------- #
# s = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0003))
# s.bind(("mon0", 0x0003))
#
# ap_list = []
#
# while True:
#     packet = s.recvfrom(2048)
#
#     if packet[26] == "\x80":
#         if packet[36:42] not in ap_list and ord(packet[63]) > 0:
#             ap_list.add(packet[36:42])
#     print("SSID:", (pkt[64:64+ord(pkt[63])], pkt[36:42].encode('hex')))
