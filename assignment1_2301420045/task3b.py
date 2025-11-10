import os
import time

def orphan_process():
    """Creates an orphan process."""
    print("--- Running Task 3b: Orphan Process Simulation ---")
    pid = os.fork()
    if pid == 0:
        print(f"Child (PID: {os.getpid()}) is sleeping for 5 seconds.")
        time.sleep(5)
        print(f"Child is awake. My PID is {os.getpid()}, and my Parent's PID is now {os.getppid()}.")
        os._exit(0)
    else:
        print(f"Parent (PID: {os.getpid()}) is exiting immediately.")
        os._exit(0)

if __name__ == "__main__":
    orphan_process()
