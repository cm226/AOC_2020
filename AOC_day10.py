adapters = []
f = open("input_day10.txt")

for l in f:
    adapters.append(int(l))

adapters.append(0) # for the wall delta
adapters.sort()

adapters.append(adapters[len(adapters)-1]+3)

prev = None
arrangement_count = 0

segments = []

def findNext3Gap(i):
    while i < len(adapters)-1:
        if adapters[i+1] - adapters[i] == 3:
            return i 
        i+=1

    return len(adapters)-1 

def validCombination(seg):
    i = 0
    for i in range(len(seg)-1):
        if seg[i+1] - seg[i] > 3:
            return False
    
    return True

def calcCombinations(seg):
    if len(segments) == 1 or len(segments) == 2:
            return 1

    # cant move the edges, so just manipulate the centers
    validCount = 1 # current arrangement is valid
    for i in range(1, len(seg)-1):
        copy = seg.copy()
        del copy[i]
        if validCombination(copy):
            validCount+=1

    for i in range(1, len(seg)-2):
        copy = seg.copy()
        del copy[i:i+1]
        if validCombination(copy):
            validCount+=1

    for i in range(1, len(seg)-3):
        copy = seg.copy()
        del copy[i:i+2]
        if validCombination(copy):
            validCount+=1

    return validCount

    

# find segments bound by 3 gaps
inSegment = True
cur_segment = []
i = 0
while i < len(adapters):
    
    cur = adapters[i]
    next3 = findNext3Gap(i)  

    segments.append(adapters[i:next3+1])
    i = next3+1


#calc combinations of segments
combs = 1
for segment in segments:
    comb = calcCombinations(segment)
    print(segment, comb)
    combs *= comb

print(combs)


