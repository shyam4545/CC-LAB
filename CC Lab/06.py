#Develop a resource monitoring script in Python using psutil to monitor
#CPU, memory, and disk usage, simulating a cloud monitoring mechanism
import psutil
import time
import datetime
import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def monitor_resources(interval=2):
    while True:
        clear_screen()

        print("===== CLOUD RESOURCE MONITORING SYSTEM =====")
        print("Time:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        print("---------------------------------------------")

        # CPU Usage
        cpu_percent = psutil.cpu_percent(interval=1)
        print(f"CPU Usage       : {cpu_percent}%")

        # Memory Usage
        memory = psutil.virtual_memory()
        print(f"Memory Used     : {memory.percent}%  ({memory.used // (1024**2)} MB / {memory.total // (1024**2)} MB)")

        # Disk Usage
        disk = psutil.disk_usage('/')
        print(f"Disk Used       : {disk.percent}%  ({disk.used // (1024**3)} GB / {disk.total // (1024**3)} GB)")

        print("---------------------------------------------")

        # Simulate cloud alert system
        if cpu_percent > 80:
            print("⚠️  ALERT: High CPU usage detected!")

        if memory.percent > 80:
            print("⚠️  ALERT: High Memory usage detected!")

        if disk.percent > 80:
            print("⚠️  ALERT: Disk almost full!")

        print("\nUpdating in", interval, "seconds...")
        time.sleep(interval)

if __name__ == "__main__":
    monitor_resources(interval=2)


'''
⭐ Hinglish Explanation (Simple + Viva Friendly)
🔹 psutil kya karta hai?

psutil = Python System and Process Utilities
Ye system-level information deta hai:

CPU usage

Memory usage

Disk usage

Processes

Network stats

Cloud monitoring tools jaisa hi kaam karta hai.

🔹 Code Explanation (Very Simple)
1️⃣ Clear screen:
clear_screen()


Console clean karta rehta hai, live dashboard jaisa lagta hai.

2️⃣ CPU usage:
cpu_percent = psutil.cpu_percent(interval=1)


1 second ka average CPU usage deta hai.

3️⃣ Memory usage:
memory = psutil.virtual_memory()
memory.percent


Total memory

Used memory

Percentage usage

4️⃣ Disk usage:
disk = psutil.disk_usage('/')
disk.percent


Total disk

Used

Free

Usage %

5️⃣ Cloud-Style Alert Simulation:
if cpu_percent > 80:
    print("⚠️ High CPU usage!")


Real cloud me AWS CloudWatch jaisa alert rule hota hai.

Yaha simplified simulation bana diya.

6️⃣ Loop to repeat monitoring:
time.sleep(interval)


Script har 2 seconds me refresh hota rehta hai.

⭐ Final Summary (Exam Perfect)

✔ psutil ka use kar ke CPU, RAM, Disk monitor kiya
✔ Real cloud monitoring jaisa console dashboard banaya
✔ Threshold-based alert system add kiya
✔ Fully working Python script
✔ Viva me easy explain ho jayega




'''