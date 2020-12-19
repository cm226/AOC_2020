from collections import Counter
import copy
import operator

layout = [list(line.strip()) for line in open("input_day11.txt")]

iteration = 0

def traverseSpaces(p, v):
    p = tuple(map(operator.add, p, v))

    if p[0] <0 or p[0] >= len(layout):
        return '.'
    if p[1] < 0 or p[1]>= len(layout[p[0]]):
        return '.'

    while layout[p[0]][p[1]] == '.':
        p = tuple(map(operator.add, p, v))

        if p[0] <0 or p[0] >= len(layout):
            return '.'
        if p[1] < 0 or p[1]>= len(layout[p[0]]):
            return '.'

    return layout[p[0]][p[1]];
    

def getAdjacent(i,j):
    result = [
        traverseSpaces((i,j),(1,0)),
        traverseSpaces((i,j),(-1,0)),
        traverseSpaces((i,j),(1,1)),
        traverseSpaces((i,j),(-1,-1)),
        traverseSpaces((i,j),(0,1)),
        traverseSpaces((i,j),(0,-1)),
        traverseSpaces((i,j),(1,-1)),
        traverseSpaces((i,j),(-1,1))
    ]

    
    
    #result.extend(['L']*(8-len(result)))
    return result

for a in layout:
    line = ''
    for b in a:
        line+=b
    print(line)

changed = True
while changed:
    nextFrame = copy.deepcopy(layout)
    changed = False
    for i in range(len(layout)):
        for j in range(len(layout[i])):
            if layout[i][j] == '.':
                continue

            adjacent = getAdjacent(i, j)
            if '#' not in adjacent and layout[i][j] != '.' and layout[i][j]!='#':
                nextFrame[i][j] = '#'
                changed = True
                continue
            
            if layout[i][j] == '#' and adjacent.count('#') >= 5:
                nextFrame[i][j] = 'L'  
                changed = True

    layout = nextFrame
    iteration+=1
    
    # for a in nextFrame:
    #    line = ''
    #    for b in a:
    #        line+=b
    #    print(line)

    # print()

count = 0
for l in layout:
    count += l.count('#')
print(count)