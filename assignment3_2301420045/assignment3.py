
def priority_scheduling(ls):
    ls.sort(key=lambda x: x[2])

    waiting_time = [0] * len(ls)
    turnaround_time = [0] * len(ls)
    total_waiting = 0
    total_turnaround = 0

    for i in range(len(ls)):
        if i == 0:
            waiting_time[i] = 0
        else:
            waiting_time[i] = waiting_time[i-1] + ls[i-1][1]

    for i in range(len(ls)):
        turnaround_time[i] = waiting_time[i] + ls[i][1]

    print("PID\tBurst\tPriority\tWaiting\tTurnaround")
    for i in range(len(ls)):
        pid, burst, priority = ls[i]
        print(f"{pid}\t{burst}\t{priority}\t\t{waiting_time[i]}\t{turnaround_time[i]}")
        total_waiting += waiting_time[i]
        total_turnaround += turnaround_time[i]

    print(f"\nAverage Waiting Time: {total_waiting / len(ls):.2f}")
    print(f"Average Turnaround Time: {total_turnaround / len(ls):.2f}")

process_list = [["P1", 5, 3], ["P2", 1, 1], ["P3", 4, 3], ["P4", 4, 5], ["P5", 5, 2]]
priority_scheduling(process_list)
