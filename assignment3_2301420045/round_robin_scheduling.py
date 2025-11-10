def round_robin(process, quantum = 2):
    n = len(process)
    t = 0
    waiting_time = [0] * n
    turnaround_time = [0] * n
    processes = [p[0] for p in process_list]
    burst_time = [p[1] for p in process_list]
    remaining_time = burst_time.copy()

    while True:
        done = True
        for i in range(n):
            if remaining_time[i] > 0:
                done = False
                if remaining_time[i] > quantum:
                    t += quantum
                    remaining_time[i] -= quantum
                else:
                    t += remaining_time[i]
                    waiting_time[i] = t - burst_time[i]
                    remaining_time[i] = 0
        if done:
            break

    for i in range(n):
        turnaround_time[i] = burst_time[i] + waiting_time[i]

    print("Process\tBT\tWT\tTAT")
    for i in range(n):
        print(f"{processes[i]}\t{burst_time[i]}\t{waiting_time[i]}\t{turnaround_time[i]}")

    print(f"\nAverage Waiting Time: {sum(waiting_time)/n:.2f}")
    print(f"Average Turnaround Time: {sum(turnaround_time)/n:.2f}")

# Example input
process_list = [["p1", 3], ["p2", 6], ["p3", 4], ["p4", 5]]
round_robin(process_list, quantum=2)

