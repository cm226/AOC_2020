
def insertNumSpken(num, idx):
    if num in num_spoken:
        num_spoken[num].append(idx)
        if len(num_spoken[num]) > 2:
            num_spoken[num].pop(0)
    else:
        num_spoken[num] = [idx]


input="13,0,10,12,1,5,8".split(',')
input = list(map(int, input))

num_spoken = {}

i=1
for n in input:
    insertNumSpken(n,i )
    i+=1


lastSpoken = input[-1]
turn = len(input)+1
for i in range(turn, 30000001):
    cur_num = 0
    if lastSpoken in num_spoken and len(num_spoken[lastSpoken])==2:
        lastturns = num_spoken[lastSpoken]
        cur_num = lastturns[1]-lastturns[0]
        insertNumSpken(cur_num, i)
    else:
        insertNumSpken(0, i)

    lastSpoken = cur_num

        

print(lastSpoken)


