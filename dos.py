import sys
import time
from scapy.all import Ether, IP, TCP, sendp

TARGET_IP = "192.168.x.x" #informar o ip target
INTERFACE = "eth0" #trocar com a interface do seu provedor de internet
NUM_PACKETS = 100
DURATION = 5

def send_packets(target_ip,interface,num_packets, duration):
    packet = Ether() / IP(dst=target_ip) / TCP()
    endtime = time.time() + duration
    packet_count = 0

    while time.time() < endtime and packet_count < num_packets:
        sendp(packet, iface=interface)
        packet_count += 1

if __name__ == "__main__":
    if sys.version_info[0] < 3:
        print("this script requires Python 3")
        sys.exit(1)

    send_packets(TARGET_IP, INTERFACE, NUM_PACKETS, DURATION)