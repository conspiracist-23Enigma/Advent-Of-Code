count = 0
arr = list(map(int,input().split()))
while len(arr) != 0:
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):

            val_1 = arr[i]
            val_2 = arr[j]

            if (val_1 / val_2).is_integer() or (val_2 / val_1).is_integer():

                if val_1 > val_2:
                    count += val_1 // val_2
                    break
                else:
                    count += val_2 // val_1
                    break
        else:
            continue

        break
                
    arr = list(map(int,input().split()))
print(count)
               
                


