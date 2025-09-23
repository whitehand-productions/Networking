import socket
import time
from scapy.all import ARP, Ether, srp
import networkx as nx
import matplotlib.pyplot as plt

def scan_network(ip_range):
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp
    result = srp(packet, timeout=2, verbose=True)[0]

    devices = []

    for sent, received in result:
        try:
            hostname = socket.gethostbyaddr(received.psrc)[0]
        except:
            hostname = "Unknown"
        devices.append[{'ip': received.psrc, 'mac': received.hwsrc, 'host': hostname }]
    return devices

def build_network_graph(devices, gateway_ip="192.168.0.1"):
    G = nx.Graph()

    G.add_node(gateway_ip, label="Gateway", color = "red")

    for device in devices:
        label = f"{device['ip']}\n{device['host']}"
        G.add_node(device['ip'], label=label, color="skyblue")
        G.add_edge(gateway_ip, device['ip'])

    pos = nx.spring_layout(G, seed=42)
    colors = [G.nodes[n]['color'] for n in G.nodes()]
    labels = nx.get_node_attributes(G, 'label')

    plt.figure(figsize=(10,8))
    nx.draw(G, pos, with_labels=True, labels=labels, node_color=colors, node_size=2500, font_size=8, font_color="black", edge_color="gray")
    
    plt.title("Home Network Mapper", fontsize=14)
    plt.show()

    if __name__ == "__main__":
        ip_range = "192.168.1.0/24"

        print("[*] Scanning network...")
        devices = scan_network(ip_range)

        print(f"[*] Found {len(devices)} devices:")

        for d in devices:
            print(f"IP: {d['ip']}, MAC: {d['mac']}, Host: {d['host']}")

        build_network_graph(devices)