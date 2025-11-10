import os
import sys

def task1(n=3):
    """Creates n child processes, each printing its PID and parent PID."""
    print("--- Running Task 1: Process Creation ---")
    pids = []
    for i in range(n):
        pid = os.fork()
        if pid == 0:  # Child
            print(f"Child (PID: {os.getpid()}) created by Parent (PPID: {os.getppid()}). Message: Hello from child {i+1}")
            os._exit(0)
        else:
            pids.append(pid)

    # Wait for all children
    for pid in pids:
        os.waitpid(pid, 0)
    print("--- Task 1 Finished: Parent has waited for all children. ---\n")

if __name__ == "__main__":
    task1()
