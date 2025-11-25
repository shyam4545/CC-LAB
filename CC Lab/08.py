#Create a Python-based service that replicates a data file across multiple
#simulated storage nodes, demonstrating data redundancy.

import os
import shutil

# ---------------- CREATE SIMULATED STORAGE NODES ----------------
def create_storage_nodes(node_count):
    nodes = []
    for i in range(1, node_count + 1):
        node_name = f"storage_node_{i}"
        os.makedirs(node_name, exist_ok=True)
        nodes.append(node_name)
    return nodes


# ---------------- REPLICATE FILE TO STORAGE NODES ----------------
def replicate_file(file_path, nodes):
    if not os.path.exists(file_path):
        print(f"Source file '{file_path}' not found!")
        return

    print("\n=== Replicating Data Across Storage Nodes ===")
    for node in nodes:
        dest_path = os.path.join(node, os.path.basename(file_path))
        shutil.copy(file_path, dest_path)
        print(f"✔ File replicated to: {node}")


# ---------------- SHOW NODE CONTENT ----------------
def show_node_contents(nodes):
    print("\n=== Storage Node Contents ===")
    for node in nodes:
        print(f"\n{node}:")
        files = os.listdir(node)
        for f in files:
            print(" -", f)


# ---------------- MAIN FUNCTION ----------------
if __name__ == "__main__":
    print("Cloud Storage Data Redundancy Simulation\n")

    # Step 1: Create Simulated Storage Nodes
    storage_nodes = create_storage_nodes(3)   # 3 storage nodes

    # Step 2: Replicate Target File
    source_file = "data.txt"   # File to replicate
    replicate_file(source_file, storage_nodes)

    # Step 3: Show replicated data
    show_node_contents(storage_nodes)
