# CPU Scheduling Algorithms
# Author: Jai
# Description: Implements FCFS, SJF, Round Robin, and Priority Scheduling
# Each calculates Waiting Time (WT) and Turnaround Time (TAT)

def find_avg_times(processes, bt, at=None, priority=None, quantum=None):
    print("\n========= CPU Scheduling Results =========")
    if at is None:
        at = [0] * len(processes)

    # FCFS
    fcfs(processes, bt, at)

    # SJF Non-Preemptive
    sjf(processes, bt, at)

    # Round Robin
    if quantum:
        rr(processes, bt, at, quantum)

    # Priority Scheduling
    if priority:
        priority_scheduling(processes, bt, at, priority)


# ---------- FCFS ----------
def fcfs(processes, bt, at):
    n = len(processes)
    wt = [0] * n
    tat = [0] * n
    ct = [0] * n

    for i in range(n):
        if i == 0:
            ct[i] = at[i] + bt[i]
        else:
            ct[i] = max(at[i], ct[i-1]) + bt[i]
        tat[i] = ct[i] - at[i]
        wt[i] = tat[i] - bt[i]

    print("\n--- FCFS Scheduling ---")
    print_table(processes, bt, at, wt, tat)


# ---------- SJF Non-Preemptive ----------
def sjf(processes, bt, at):
    n = len(processes)
    completed = [False] * n
    wt = [0] * n
    tat = [0] * n
    ct = [0] * n
    time = 0
    done = 0

    while done < n:
        idx = -1
        min_bt = 9999
        for i in range(n):
            if not completed[i] and at[i] <= time and bt[i] < min_bt:
                min_bt = bt[i]
                idx = i
        if idx == -1:
            time += 1
            continue
        time += bt[idx]
        ct[idx] = time
        tat[idx] = ct[idx] - at[idx]
        wt[idx] = tat[idx] - bt[idx]
        completed[idx] = True
        done += 1

    print("\n--- SJF (Non-Preemptive) Scheduling ---")
    print_table(processes, bt, at, wt, tat)


# ---------- Round Robin ----------
def rr(processes, bt, at, quantum):
    n = len(processes)
    rem_bt = bt.copy()
    t = 0
    wt = [0] * n
    tat = [0] * n
    ready_queue = []

    print("\n--- Round Robin Scheduling (q =", quantum, ") ---")
    while True:
        done = True
        for i in range(n):
            if rem_bt[i] > 0:
                done = False
                if rem_bt[i] > quantum:
                    t += quantum
                    rem_bt[i] -= quantum
                else:
                    t += rem_bt[i]
                    wt[i] = t - bt[i] - at[i]
                    rem_bt[i] = 0
        if done:
            break

    for i in range(n):
        tat[i] = bt[i] + wt[i]

    print_table(processes, bt, at, wt, tat)


# ---------- Priority Scheduling ----------
def priority_scheduling(processes, bt, at, priority):
    n = len(processes)
    completed = [False] * n
    wt = [0] * n
    tat = [0] * n
    ct = [0] * n
    time = 0
    done = 0

    while done < n:
        idx = -1
        highest_priority = 9999
        for i in range(n):
            if not completed[i] and at[i] <= time and priority[i] < highest_priority:
                highest_priority = priority[i]
                idx = i
        if idx == -1:
            time += 1
            continue
        time += bt[idx]
        ct[idx] = time
        tat[idx] = ct[idx] - at[idx]
        wt[idx] = tat[idx] - bt[idx]
        completed[idx] = True
        done += 1

    print("\n--- Priority Scheduling ---")
    print_table(processes, bt, at, wt, tat, priority)


# ---------- Helper to print results ----------
def print_table(processes, bt, at, wt, tat, priority=None):
    print("PID\tAT\tBT\t", end="")
    if priority: print("PR\t", end="")
    print("WT\tTAT")
    for i in range(len(processes)):
        print(f"{processes[i]}\t{at[i]}\t{bt[i]}\t", end="")
        if priority: print(f"{priority[i]}\t", end="")
        print(f"{wt[i]}\t{tat[i]}")
    print(f"\nAverage WT = {sum(wt)/len(wt):.2f}")
    print(f"Average TAT = {sum(tat)/len(tat):.2f}")


# ---------- MAIN ----------
if __name__ == "__main__":
    processes = [1, 2, 3, 4]
    burst_time = [6, 8, 7, 3]
    arrival_time = [0, 1, 2, 3]
    priority = [2, 1, 3, 4]
    quantum = 3

    find_avg_times(processes, burst_time, arrival_time, priority, quantum)
