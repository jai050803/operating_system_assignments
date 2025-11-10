def mft(total_memory, block_size, process_sizes):
    num_blocks = total_memory // block_size
    memory_left = total_memory
    allocated = []
    internal_frag = 0
    external_frag = 0
    block_used = 0

    print("\n--- MFT (Fixed Partition) ---")
    for i, size in enumerate(process_sizes):
        if block_used < num_blocks:
            if size <= block_size:
                allocated.append(True)
                internal_frag += (block_size - size)
                block_used += 1
                memory_left -= block_size
                print(f"Process {i+1} ({size} KB) → Block {block_used}")
            else:
                allocated.append(False)
                print(f"Process {i+1} ({size} KB) → Too large! Not allocated.")
        else:
            allocated.append(False)
            print(f"Process {i+1} ({size} KB) → No space left.")

    external_frag = memory_left
    print(f"\nTotal Internal Fragmentation = {internal_frag} KB")
    print(f"Total External Fragmentation = {external_frag} KB")


def mvt(total_memory, process_sizes):
    print("\n--- MVT (Variable Partition) ---")
    memory_left = total_memory
    allocated = []

    for i, size in enumerate(process_sizes):
        if size <= memory_left:
            allocated.append(True)
            memory_left -= size
            print(f"Process {i+1} ({size} KB) allocated. Remaining Memory = {memory_left} KB")
        else:
            allocated.append(False)
            print(f"Process {i+1} ({size} KB) cannot be allocated. Not enough memory!")

    print(f"\nTotal Memory Left = {memory_left} KB")


# --- Main Program ---
total_memory = int(input("Enter total memory size (in KB): "))

print("\n--- MFT Simulation ---")
block_size = int(input("Enter block size (in KB): "))
process_sizes = list(map(int, input("Enter process sizes (space separated, in KB): ").split()))
mft(total_memory, block_size, process_sizes)

print("\n--- MVT Simulation ---")
process_sizes = list(map(int, input("Enter process sizes again (space separated, in KB): ").split()))
mvt(total_memory, process_sizes)
