# Calculating the Number of Connections needed in a Full Mesh Network

print("-------------------------------------")
print("       FULL MESH CALCULATOR          ")
print("-------------------------------------\n")


while True:
    n = int(input("Amount of nodes: ")) # Nodes are every one of the connected device on the network
    undirected_connections = n * (n - 1) // 2 # Undirected connections formula
    directed_connections = n * (n - 1) # Directed connections formula

    print(f"{undirected_connections} undirected connections required")
    print(f"{directed_connections} directed connections required")
    use_again = input("Use again? [Y/N]").strip().upper()
    if use_again != "Y":
        break

