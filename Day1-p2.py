arr = list(input())
size = len(arr)
count = 0
for i in range(size):
    if arr[i] == arr[(i + size // 2)% size]:
        count += int(arr[i])
print ( count)
