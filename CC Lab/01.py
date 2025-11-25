#scaling scenarios (horizontal vs. vertical scaling) using simple process/thread creation and control.
import time
import threading      # For vertical scaling (threads)
import multiprocessing  # For horizontal scaling (processes)


# Ye ek simple fake task hai jo time leta hai (sleep karta hai)
def fake_task(name, duration=1):
    print(f"{name} START")
    time.sleep(duration)   # Assume ye koi heavy kaam kar raha hai
    print(f"{name} END")


# ---------------- VERTICAL SCALING SIMULATION ----------------
def vertical_scaling(num_threads):
    print("\n=== VERTICAL SCALING: One big machine, many threads ===")
    threads = []

    # Ek hi process ke andar multiple threads bana rahe hain
    for i in range(num_threads):
        t = threading.Thread(
            target=fake_task, 
            args=(f"Thread-{i + 1}", 1)
        )
        threads.append(t)
        t.start()   # Thread start karo

    # Sab threads ke khatam hone ka wait karna (join)
    for t in threads:
        t.join()


# ---------------- HORIZONTAL SCALING SIMULATION ----------------
def horizontal_scaling(num_processes):
    print("\n=== HORIZONTAL SCALING: Many small machines (processes) ===")
    processes = []

    # Multiple processes bana rahe hain
    for i in range(num_processes):
        p = multiprocessing.Process(
            target=fake_task,
            args=(f"Process-{i + 1}", 1)
        )
        processes.append(p)
        p.start()   # Process start karo

    # Sab processes ke khatam hone ka wait karna (join)
    for p in processes:
        p.join()


if __name__ == "__main__":
    start = time.time()
    vertical_scaling(num_threads=4)
    print(f"Vertical scaling total time: {time.time() - start:.2f} seconds")

    start = time.time()
    horizontal_scaling(num_processes=4)
    print(f"Horizontal scaling total time: {time.time() - start:.2f} seconds")
