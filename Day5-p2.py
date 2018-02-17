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
    temp = jump_list[index]
    if jump_list[index] < 3:
        jump_list[index] += 1
    else:
        jump_list[index] -= 1
    index += temp
    steps += 1

print(steps)            
