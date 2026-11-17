from scapy.all import sniff, IP, TCP, UDP, ICMP, get_if_list
from datetime import datetime

print("=" * 50)
print(" CODEALPHA - BASIC NETWORK SNIFFER")
print("=" * 50)

# Display available network interfaces
interfaces = get_if_list()

print("\nAvailable Network Interfaces:")

for i, interface in enumerate(interfaces):
    print(f"{i}. {interface}")

# Select interface
try:
    choice = int(input("\nEnter interface number: "))
    selected_interface = interfaces[choice]

except (ValueError, IndexError):
    print("Invalid interface selection!")
    raise SystemExit

packet_count = 0

# Analyze captured packets
def analyze_packet(packet):
    global packet_count

    if IP not in packet:
        return

    packet_count += 1

    source = packet[IP].src
    destination = packet[IP].dst

    if TCP in packet:
        protocol = "TCP"
        source_port = packet[TCP].sport
        destination_port = packet[TCP].dport

    elif UDP in packet:
        protocol = "UDP"
        source_port = packet[UDP].sport
        destination_port = packet[UDP].dport

    elif ICMP in packet:
        protocol = "ICMP"
        source_port = "-"
        destination_port = "-"

    else:
        protocol = "OTHER"
        source_port = "-"
        destination_port = "-"

    print("\n" + "-" * 50)
    print("Packet Number:", packet_count)
    print("Time:", datetime.now().strftime("%H:%M:%S"))
    print("Source IP:", source)
    print("Destination IP:", destination)
    print("Protocol:", protocol)
    print("Source Port:", source_port)
    print("Destination Port:", destination_port)
    print("Packet Size:", len(packet), "bytes")


# Start capturing packets
print("\nStarting packet capture...")
print("Capturing up to 20 packets or 30 seconds.")

try:
    sniff(
        iface=selected_interface,
        filter="ip",
        prn=analyze_packet,
        store=False,
        count=20,
        timeout=30
    )

except KeyboardInterrupt:
    print("\nCapture stopped by user.")

except Exception as error:
    print("\nError:\n", error)

print("\nCapture completed!")
print("Total packets captured:", packet_count)
