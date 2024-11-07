from scapy.all import sniff, sendp, IP, Ether

def packet_handler(packet):
    if packet.haslayer(IP):
        modified_packet = packet.copy()
        modified_packet[IP].dst = "10.2.2.1

        del modified_packet[IP].chksum
        sendp(modified_packet, iface="eth1")
        print(f"Pacote encaminhado de {packet[IP].src} para {modified_packet[IP].dst}")

sniff(iface="eth0", prn=packet_handler, filter="ip", store=0)
