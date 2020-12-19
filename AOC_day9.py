f = open("input_day9.txt")

last_25 = []
invalidNumbr = 0
for line in f:
    number = int(line.strip())

    if len(last_25) < 25:
        last_25.append(number)
        continue

    valid = False
    for i in range(len(last_25)):
        for j in range(i, len(last_25)):
            if last_25[i]+last_25[j] == number:
                valid=True
                break
        if valid:
            break
    
    if not valid:
        invalidNumbr = number
        break
    
    last_25.pop(0)
    last_25.append(number)


sums = []
f = open("input_day9.txt")
for line in f:
    number = int(line.strip())

    for s in sums:
        s.append(number)

    sums.append([number])

    sums_too_big = []
    for s in sums:
        if sum(s) > invalidNumbr:
            sums_too_big.append(s)
        elif sum(s) == invalidNumbr:
            print (min(s) + max(s))
            exit()
    
    for s in sums_too_big:
        sums.remove(s)

print("something went wrong")

    
    


