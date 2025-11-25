#Implement a Python-based failover mechanism simulation where service
#requests are switched between primary and backup in stances.
import random
import time

# ---------------- SERVICE INSTANCE ----------------
class ServiceInstance:
    def __init__(self, name):
        self.name = name
        self.active = True  # Instance initially healthy

    def handle_request(self, request_id):
        if self.active:
            print(f"[{self.name}] handled request #{request_id}")
        else:
            print(f"[{self.name}] is DOWN!")

    def simulate_failure(self):
        # Randomly fail instance
        if random.random() < 0.2:   # 20% chance of failure
            self.active = False
            print(f"❌ {self.name} FAILED!")

    def simulate_recovery(self):
        # Random recovery
        if not self.active and random.random() < 0.3:
            self.active = True
            print(f"✅ {self.name} RECOVERED!")


# ---------------- FAILOVER CONTROLLER ----------------
class FailoverController:
    def __init__(self, primary, backup):
        self.primary = primary
        self.backup = backup

    def route_request(self, request_id):
        # If primary is healthy → use it
        if self.primary.active:
            self.primary.handle_request(request_id)
        else:
            print("⚠️ Primary down! Switching to backup...")
            self.backup.handle_request(request_id)

    def health_check(self):
        # Simulate primary failure or recovery
        self.primary.simulate_failure()
        self.primary.simulate_recovery()

        # Backup failures also (rare)
        self.backup.simulate_failure()
        self.backup.simulate_recovery()


# ---------------- MAIN SIMULATION ----------------
if __name__ == "__main__":
    primary = ServiceInstance("Primary-Server")
    backup = ServiceInstance("Backup-Server")

    controller = FailoverController(primary, backup)

    for req in range(1, 15):  # 15 incoming requests
        print(f"\nIncoming request #{req}")

        controller.health_check()      # Run health checks
        controller.route_request(req)  # Send request to correct server

        time.sleep(1)
