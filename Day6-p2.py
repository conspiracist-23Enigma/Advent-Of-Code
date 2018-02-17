banks = list(map(int, input().split()))
cycles = 0
seen_states = []

while ([item for item in seen_states if item[0] == banks] == []):
    seen_states += [(banks[:],cycles)]

    avail_blocks = max(banks)
    current_index = banks.index(max(banks))
    banks [current_index] = 0

    for _ in range(avail_blocks):
        current_index = (current_index + 1) % len(banks)
        banks[current_index] += 1
    
    cycles += 1
else:
    previous_cycles = [item for item in seen_states if item[0] == banks][0][1]
    
print(cycles - previous_cycles)
