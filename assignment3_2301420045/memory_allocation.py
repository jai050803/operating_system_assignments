def first_fit(partitions, processes):
    allocation = [-1] * len(processes)
    for i in range(len(processes)):
        for j in range(len(partitions)):
            if partitions[j] >= processes[i]:
                allocation[i] = j
                partitions[j] -= processes[i]
                break
    return allocation


def best_fit(partitions, processes):
    allocation = [-1] * len(processes)
    for i in range(len(processes)):
        best_idx = -1
        for j in range(len(partitions)):
            if partitions[j] >= processes[i]:
                if best_idx == -1 or partitions[j] < partitions[best_idx]:
                    best_idx = j
        if best_idx != -1:
            allocation[i] = best_idx
            partitions[best_idx] -= processes[i]
    return allocation


def worst_fit(partitions, processes):
    allocation = [-1] * len(processes)
    for i in range(len(processes)):
        worst_idx = -1
        for j in range(len(partitions)):
            if partitions[j] >= processes[i]:
                if worst_idx == -1 or partitions[j] > partitions[worst_idx]:
                    worst_idx = j
        if worst_idx != -1:
            allocation[i] = worst_idx
            partitions[worst_idx] -= processes[i]
    return allocation


def display(processes, allocation):
    print("\nProcess No.\tProcess Size\tPartition No.")
    for i in range(len(processes)):
        if allocation[i] != -1:
            print(f"{i+1}\t\t{processes[i]}\t\t{allocation[i]+1}")
        else:
            print(f"{i+1}\t\t{processes[i]}\t\tNot Allocated")


partitions = list(map(int, input("Enter partition sizes (space separated): ").split()))
processes = list(map(int, input("Enter process sizes (space separated): ").split()))

print("\n--- First Fit ---")
allocation = first_fit(partitions.copy(), processes)
display(processes, allocation)

print("\n--- Best Fit ---")
allocation = best_fit(partitions.copy(), processes)
display(processes, allocation)

print("\n--- Worst Fit ---")
allocation = worst_fit(partitions.copy(), processes)
display(processes, allocation)
