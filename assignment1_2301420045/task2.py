import os
import sys

def task2():
    """Creates a child process that executes a Linux command."""
    print("--- Running Task 2: Command Execution ---")
    pid = os.fork()
    if pid == 0:  # Child
        print(f"Child (PID: {os.getpid()}) is executing the 'ls -l' command.")
        try:
            os.execvp("ls", ["ls", "-l"])
        except FileNotFoundError:
            print("Error: Command not found.")
            os._exit(1)
    else:  # Parent
        os.wait()
        print("--- Task 2 Finished: Child has executed the command. ---\n")

if __name__ == "__main__":
    task2()
