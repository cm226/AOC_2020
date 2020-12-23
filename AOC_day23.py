import math

def printList(l):
    start = l
    cur = start
    while cur != start:
        print(cur.val, sep=',', end='')
        cur = cur.next

class Cup:

    next = None
    val = None
    def __init__(self, val):
        self.next = None
        self.val = val



input="916438275"
cuplist = list(input)
cuplist = list(map(int, cuplist))

# find min and max cup vals
lims = [max(cuplist),min(cuplist)] 
cuplist.extend(range(lims[0]+1, 1000001))
# adjust limits after extending
lims[0] = 1000000 

cups = Cup(cuplist[0])
cupMap = {}
cupMap[cuplist[0]] = cups
last = cups
for c in cuplist[1:]:
    last.next = Cup(c)
    last = last.next
    cupMap[c] = last

last.next = cups

curCup = cups


lastReported = 0

# add the other cups 


#for i in range(100):
for i in range(10000000):
    
    #print("cups")
    #printList(curCup)

    grabedCups = curCup.next

    #print("grabed")
    #printList(grabedCups)

    lastGrabed = curCup
    for i in range(3):
        lastGrabed = lastGrabed.next
    
    curCup.next = lastGrabed.next
    lastGrabed.next = None
    
    
    #find dest
    dest = None
    val = curCup.val

    while True:
        val -= 1
        val = lims[0] if val < lims[1] else val

        cur_grabed = grabedCups
        inGrabed = False
        while cur_grabed != lastGrabed.next:
            if cur_grabed.val == val:
                inGrabed = True
                break
            cur_grabed = cur_grabed.next
        if not inGrabed:
            break


    dest = cupMap[val]

    tmp = dest.next
    dest.next = grabedCups

    lastGrabed.next = tmp

    curCup = curCup.next

    progress = math.floor((i / 1000000.0)*100.0)
    if progress > lastReported:
        print(progress)
        lastReported = progress

#print(cups)

# startCup = cupMap[1].next
# for j in range(1,len(cupMap)):
#    print(startCup.val, sep='', end='')
#    startCup = startCup.next
        
print()
print(cupMap[1].next.val)
print(cupMap[1].next.next.val)
print(cupMap[1].next.val*cupMap[1].next.next.val)

    
