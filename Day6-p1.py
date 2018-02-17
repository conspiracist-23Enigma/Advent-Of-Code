banks = list(map(int, input().split()))
cycles = 0
seen_states = []

while not (banks in seen_states):
    cycles += 1
    seen_states += [banks[:]]

    avail_blocks = max(banks)
    current_index = banks.index(max(banks))
    banks [current_index] = 0

    for _ in range(avail_blocks):
        current_index = (current_index + 1) % len(banks)
        banks[current_index] += 1

print(cycles)
