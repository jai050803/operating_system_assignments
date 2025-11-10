import os

def task5(n=3):
    """Demonstrates scheduler impact using different nice values."""
    print("--- Running Task 5: Process Prioritization ---")
    print("Starting CPU-intensive tasks with different priorities (lower nice value = higher priority).")

    for i in range(n):
        pid = os.fork()
        if pid == 0:
            nice_val = i * 5
            os.nice(nice_val)
            print(f"Child (PID: {os.getpid()}, nice: {nice_val}) starting.")
            result = sum(j for j in range(30000000))
            print(f"Child (PID: {os.getpid()}, nice: {nice_val}) finished.")
            os._exit(0)

    for _ in range(n):
        os.wait()
    print("--- Task 5 Finished. Observe the finishing order. ---\n")

if __name__ == "__main__":
    task5()
