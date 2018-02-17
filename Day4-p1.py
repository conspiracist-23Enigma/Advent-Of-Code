true_passes = 0

while True:
    passphrase = input().split()

    if passphrase == []:
        break
    
    for iter in range(len(passphrase)):
        if passphrase[iter] in passphrase[iter + 1 : len(passphrase)]:
            break
    else:
        true_passes += 1

print (true_passes)
