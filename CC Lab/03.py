#Virtual Machine (VM) creation and management using libvirt
#and Python bindings, or simulate virtual machine scheduling

import libvirt
import sys

# 1. Hypervisor se connect hona (QEMU/KVM)
try:
    conn = libvirt.open('qemu:///system')
except libvirt.libvirtError:
    print("Failed to open connection to qemu:///system")
    sys.exit(1)

# 2. Sare defined VMs (domains) list karna
print("=== List of VMs (domains) ===")
for domain_id in conn.listDomainsID():  # running VMs
    dom = conn.lookupByID(domain_id)
    print(f"Running VM: {dom.name()} (ID={domain_id})")

for name in conn.listDefinedDomains():  # shutoff/defined VMs
    print(f"Defined but not running VM: {name}")

# 3. Ek specific VM ko name se dhundhna
vm_name = "test-vm"   # yaha apne VM ka naam daalna
try:
    dom = conn.lookupByName(vm_name)
except libvirt.libvirtError:
    print(f"VM '{vm_name}' not found.")
    conn.close()
    sys.exit(1)

print(f"\nSelected VM: {dom.name()}")

# 4. Agar VM band hai to start karo
if dom.isActive() == 0:
    print("VM is not running. Starting it...")
    dom.create()
else:
    print("VM is already running.")

# 5. Status print karna
state, reason = dom.state()
print(f"Current VM state: {state} (libvirt state code)")

# 6. VM ko stop (shutdown) ka example
# WARNING: comment/uncomment as per need
user_input = input("\nShutdown VM? (y/n): ")
if user_input.lower() == "y":
    print("Shutting down VM...")
    dom.shutdown()   # soft shutdown request
    # dom.destroy()  # force power off (hard)

# 7. Connection close
conn.close()
print("Connection closed.")
