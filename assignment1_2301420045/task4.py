import os

def inspect_process(pid):
    """Reads and prints details for a given PID from the /proc filesystem."""
    print(f"--- Running Task 4: Inspecting PID {pid} ---")
    try:
        with open(f"/proc/{pid}/status") as f:
            for line in f:
                if line.startswith(("Name:", "State:", "VmSize:")):
                    print(line.strip())

        exe_path = os.readlink(f"/proc/{pid}/exe")
        print(f"Executable Path: {exe_path}")

        fds = os.listdir(f"/proc/{pid}/fd")
        print(f"Open File Descriptors: {len(fds)} ({fds})")

    except (FileNotFoundError, PermissionError) as e:
        print(f"Could not inspect PID {pid}. Error: {e}")
    print("--- Task 4 Finished. ---\n")

if __name__ == "__main__":
    pid_input = input("Enter PID to inspect: ")
    try:
        inspect_process(int(pid_input))
    except ValueError:
        print("Invalid PID.")
