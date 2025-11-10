import os
import time

def zombie_process():
    """Creates a zombie process."""
    print("--- Running Task 3a: Zombie Process Simulation ---")
    pid = os.fork()
    if pid == 0:
        print(f"Zombie Child (PID: {os.getpid()}) created. It will exit immediately.")
        os._exit(0)
    else:
        print(f"Parent (PID: {os.getpid()}) is sleeping for 10 seconds, not waiting.")
        print("--> While sleeping, open another terminal and run: ps -el | grep defunct")
        time.sleep(10)
        os.wait()
        print("--- Task 3a Finished. Zombie cleaned up. ---\n")

if __name__ == "__main__":
    zombie_process()
