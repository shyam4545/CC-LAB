#Develop a Python script to simulate SLA monitoring by measuring
#response time of service endpoints and checking against defined
#thresholds.

import requests
import time
import datetime

# ---------------- CONFIGURATION ----------------
ENDPOINTS = [
    "https://httpbin.org/get",
    "https://jsonplaceholder.typicode.com/posts",
]
SLA_THRESHOLD_MS = 300      # SLA threshold: 300 ms allowed
CHECK_INTERVAL = 3          # Check every 3 seconds


# ---------------- SLA CHECK FUNCTION ----------------
def check_endpoint(url):
    try:
        start = time.time()
        response = requests.get(url, timeout=5)
        response_time = (time.time() - start) * 1000  # convert to ms

        status = "OK" if response.status_code == 200 else "ERROR"

        print(f"[{status}] {url}")
        print(f"  Response Time: {response_time:.2f} ms")

        if response_time > SLA_THRESHOLD_MS:
            print("  ⚠️ SLA VIOLATION: Response time exceeded threshold!")

        print("-" * 50)

    except requests.exceptions.RequestException:
        print(f"❌ ERROR: Unable to reach {url}")
        print("-" * 50)


# ---------------- MONITOR LOOP ----------------
def sla_monitor():
    print("=== SLA Monitoring Started ===")
    print(f"SLA Threshold: {SLA_THRESHOLD_MS} ms")
    print("Press CTRL+C to stop.\n")

    while True:
        print("\nTime:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        print("=" * 50)

        for url in ENDPOINTS:
            check_endpoint(url)

        time.sleep(CHECK_INTERVAL)


if __name__ == "__main__":
    sla_monitor()

'''
⭐ SLA Monitoring Concepts (Simple)
🔹 SLA kya hota hai?

Service provider guarantee deta hai:

Max response time

Max downtime

Availability %

Example:
SLA Response Time ≤ 300 ms

Agar service slow ho jaye → SLA violation alert.

⭐ Python Script: SLA Monitoring (Response Time Checker)

Use this file name: sla_monitor.py

✔ Uses requests library
✔ Measures response time
✔ Checks against threshold
✔ Shows SLA violations

🔧 Required Library:
pip install requests

⭐ Simple Hinglish Explanation (Viva Perfect)
🔹 check_endpoint(url)

Ek particular API ko hit karta hai

time.time() se start/end distance se response time calculate karta hai

Response time milliseconds (ms) me convert karta hai

response_time = (time.time() - start) * 1000

🔹 SLA Threshold Check
if response_time > SLA_THRESHOLD_MS:
    print("⚠️ SLA VIOLATION")


Agar response time > SLA threshold
→ SLA Violation print hoti hai (Alert)

🔹 Continuous Monitoring
while True:
    ...
    time.sleep(CHECK_INTERVAL)


Script bar-bar endpoints check karta rahega

Real monitoring tools jaisa

⭐ Real Cloud Concept Mapping
Python Simulation	Real Cloud Feature
Response time measurement	CloudWatch Metrics, New Relic
Threshold checking	AWS Alarm Rule
SLA violation alert	Cloud Alert / SMS / Email
Continuous checker	Prometheus scrapers
⭐ Final Summary (Exam Ready)

✔ Measures API response time
✔ SLA threshold compare
✔ Detects violations
✔ Supports multiple endpoints
✔ Text-based monitoring dashboard


'''