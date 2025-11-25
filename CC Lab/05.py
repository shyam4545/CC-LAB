#Write a Python program to simulate load balancing using round-robin or
#least-connection algorithm across multiple service instances.

import random
import time

# ---------------- Server Class ----------------
class Server:
    def __init__(self, name):
        self.name = name
        self.active_connections = 0

    def handle_request(self):
        self.active_connections += 1
        print(f"Request assigned to {self.name} | Active Connections: {self.active_connections}")

        # Simulated request finishing time
        time.sleep(0.5)
        self.active_connections -= 1


# ---------------- Round-Robin Load Balancer ----------------
class RoundRobinBalancer:
    def __init__(self, servers):
        self.servers = servers
        self.index = 0

    def get_server(self):
        server = self.servers[self.index]
        self.index = (self.index + 1) % len(self.servers)
        return server


# ---------------- Least-Connection Load Balancer ----------------
class LeastConnectionBalancer:
    def __init__(self, servers):
        self.servers = servers

    def get_server(self):
        return min(self.servers, key=lambda s: s.active_connections)


# ---------------- SIMULATION FUNCTION ----------------
def simulate(balancer, num_requests=10):
    print("\n--- Load Balancer Simulation ---")
    for i in range(1, num_requests + 1):
        print(f"\nIncoming Request #{i}")
        server = balancer.get_server()
        server.handle_request()


# ---------------- MAIN ----------------
if __name__ == "__main__":
    servers = [Server("Server-1"), Server("Server-2"), Server("Server-3")]

    print("\n===== ROUND ROBIN LOAD BALANCING =====")
    rr = RoundRobinBalancer(servers)
    simulate(rr, num_requests=6)

    print("\n===== LEAST CONNECTION LOAD BALANCING =====")
    lc = LeastConnectionBalancer(servers)
    simulate(lc, num_requests=6)
