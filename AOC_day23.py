
input="916438275"
cups = list(input)
curCupIdx = 0

cups = list(map(int, cups))

# find min and max cup vals
lims = [max(cups),min(cups)] 

for i in range(100):
    grabedCups = []
    curCupVal = cups[curCupIdx]

    for j in range(curCupIdx+1,curCupIdx+4):
        grabedCups.append( cups[(j) % len(cups)] )

    # remove the grabed cups
    cups = [c for c in cups if c not in grabedCups]
    # index is prob no longer correct so find it again
    for i in range(len(cups)):
        if cups[i] == curCupVal:
            curCupIdx = i
            break
    

    #find dest
    dest = None
    val = cups[curCupIdx]
    while dest == None:
        val -= 1
        val = lims[0] if val < lims[1] else val
        for i in range(len(cups)):
            if(cups[i] == val):
                dest = i
                break

    for j in range(len(grabedCups)):
        cups.insert(dest+j+1, grabedCups[j])


    # index is prob no longer correct so find it again
    for i in range(len(cups)):
        if cups[i] == curCupVal:
            curCupIdx = i
            break
    #print(cups)
    curCupIdx= (curCupIdx+1) % len(cups)


for i in range(len(cups)):
    if cups[i] == 1:
        for j in range(1,len(cups)):
            print(cups[(i+j) % len(cups)], sep='', end='')
        break

    
