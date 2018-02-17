steps = 0
jump_list = []
index = 0

while True:
    new = input()
    if new == "":
        break
    else:
        jump_list += [int(new)]

while index >= 0 and index < len(jump_list):
    jump_list[index] += 1
    index += (jump_list[index] - 1)
    steps += 1

print(steps)            
