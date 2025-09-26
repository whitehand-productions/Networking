# Local Machine Network Mapper (Works for one device that is my local machine only)

import socket
import networkx as nx
import matplotlib
matplotlib.use('TkAgg')  # Makes sure matplot works on Windows
import matplotlib.pyplot as plt

# Information about Local machine
def get_local_machine_info():
    hostname = socket.gethostname()
    try:
        ip_address = socket.gethostbyname(hostname)
    except:
        ip_address = "Unknown"
    return {'ip': ip_address, 'host': hostname}

# Visuals for Network Graph 
def build_network_graph(devices, gateway_ip="127.0.0.1"):
    G = nx.Graph()
    G.add_node(gateway_ip, label="Local Machine", color="red")

    for device in devices:
        label = f"{device['ip']}\n{device['host']}"
        G.add_node(device['ip'], label=label, color="skyblue")
        G.add_edge(gateway_ip, device['ip'])

    pos = nx.spring_layout(G, seed=42)
    colors = [G.nodes[n]['color'] for n in G.nodes()]
    labels = nx.get_node_attributes(G, 'label')

    plt.figure(figsize=(6,6))
    nx.draw(G, pos, with_labels=True, labels=labels, node_color=colors,
            node_size=2000, font_size=10, font_color="black", edge_color="gray")
    plt.title("Local Machine Mapper", fontsize=14)
    plt.show()

if __name__ == "__main__":
    # Scan local machine
    devices = [get_local_machine_info()]

    # Print table
    print("\nDevice Table:")
    print("IP Address       Hostname")
    print("-"*30)
    for d in devices:
        print(f"{d['ip']:15} {d['host']}")

    # Build graph
    build_network_graph(devices)