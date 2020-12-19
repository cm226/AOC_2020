import copy
from operator import add

def AddW(idx, grid):
    global m_dim
    global min_dim

    # make a box the right size
    box = {}
    for z in range(min_dim[1], m_dim[1]):
        box[z] = {}
        for y in range(min_dim[2], m_dim[2]):
            box[z][y]={}
            for x in range(min_dim[3], m_dim[3]):
                box[z][y][x] = '.'

    grid[idx] = box


def AddLayer(idx, grid):
    global m_dim
    global min_dim

    if idx in grid[0]:
        return

    # make a layer of the right size 
    layer = {}
    for y in range(min_dim[2], m_dim[2]):
        layer[y] = {}
        for x in range(min_dim[3], m_dim[3]):
            layer[y][x] = '.'

    for w in range(min_dim[0], m_dim[0]):
        grid[w][idx] = copy.deepcopy(layer)

def AddY(idx, grid):
    global m_dim
    global min_dim

    if idx in grid[0][0]:
        return

    for w in range(min_dim[0], m_dim[0]):
        for z in range(min_dim[1], m_dim[1]):
            new_y = {}
            for x in range(min_dim[3], m_dim[3]):
                new_y[x] = '.'
            grid[w][z][idx] = new_y

def AddX(idx, grid):
    global m_dim
    global min_dim

    if idx in grid[0][0][0]:
        return

    for w in range(min_dim[0], m_dim[0]):
        for z in range(min_dim[1], m_dim[1]):
            for y in range(min_dim[2], m_dim[2]):
                grid[w][z][y][idx] = '.'

def getCountforLayer(w, z, xc, yc, includeCenter):
    global grid

    if w not in grid or z not in grid[w]:
        if includeCenter:
            return (0, 9)
        else:
            return (0, 8)

    layer = grid[w][z]
    activeCount = 0
    inactiveCount = 0

    for x in range(xc-1, xc+2):
        for y in range(yc-1, yc+2):
            if not includeCenter and x == xc and y == yc:
                continue
            if y not in layer:
                inactiveCount+=1
            elif x not in layer[y]:
                inactiveCount+=1
            elif layer[y][x] == '#':
                activeCount+=1
            else:
                inactiveCount+=1
    return (activeCount, inactiveCount)

def runCycle():
    global grid
    global m_dim
    global min_dim

    newGrid = copy.deepcopy(grid)


    for w, box in grid.items():
        for z, layer in box.items():
            for y, row in layer.items():
                for x, val in row.items():

                    combined = (0,0)
                    for w_idx in range(w-1, w+2):
                        if w_idx == w:
                            l0 = getCountforLayer(w_idx, z, x, y, False)
                        else:
                            l0 = getCountforLayer(w_idx, z, x, y, True)
                        ln = getCountforLayer(w_idx,z-1, x, y, True)
                        lp = getCountforLayer(w_idx,z+1, x, y, True)

                        tmp = tuple( map(add, l0, ln) )
                        tmp = tuple( map(add, tmp, lp))
                        combined = tuple( map(add, combined, tmp))

                    cubeActive = grid[w][z][y][x] == '#'

                    neighbourActiveCount = combined[0]
                    newVal = '.'
                    if cubeActive:
                        if neighbourActiveCount == 2 or neighbourActiveCount == 3:
                            newVal = '#'
                    else:
                        if neighbourActiveCount == 3:
                            newVal = '#'

                    newGrid[w][z][y][x] = newVal
                    if newVal == '#':

                        if w == m_dim[0]-1:
                            m_dim[0]+=1
                            AddW(m_dim[0]-1, newGrid)
                        if z == m_dim[1]-1:
                            m_dim[1]+=1
                            AddLayer(m_dim[1]-1, newGrid)
                        elif y == m_dim[2]-1:
                            m_dim[2]+=1
                            AddY(m_dim[2]-1, newGrid)
                        elif x == m_dim[3]-1:
                            m_dim[3]+=1
                            AddX(m_dim[3]-1, newGrid)
                        elif w == min_dim[0]:
                            min_dim[0]-=1
                            AddW(min_dim[0], newGrid)
                        elif z == min_dim[1]:
                            min_dim[1]-=1
                            AddLayer(min_dim[1], newGrid)
                        elif y == min_dim[2]:
                            min_dim[2]-=1
                            AddY(min_dim[2], newGrid)
                        elif x == min_dim[3]:
                            min_dim[3]-=1
                            AddX(min_dim[3], newGrid)
            #if w == 0 and z == 0:
                #printGrid(newGrid)

    
    grid = newGrid

f = open("input_day17.txt")

grid = {} 
m_dim = [1,1,0,0]
min_dim = [0,0,0,0]

col = 0
tmp_layer = {}
for line in f:
    x = {}
    xState = list(line.strip())
    for i in range(len(xState)):
        x[i] = xState[i]

    m_dim[3]= len(xState)
    tmp_layer[col] = x
    col+=1

tmp_box = {}
tmp_box[0] = tmp_layer
grid[0] = tmp_box
m_dim[2] = col

# add dimetion in every dir
m_dim[0]+=1
AddW(m_dim[0]-1, grid)

m_dim[1]+=1
AddLayer(m_dim[1]-1, grid)

m_dim[2]+=1
AddY(m_dim[2]-1, grid)

m_dim[3]+=1
AddX(m_dim[3]-1, grid)

min_dim[0]-=1
AddW(min_dim[0], grid)

min_dim[1]-=1
AddLayer(min_dim[1], grid)

min_dim[2]-=1
AddY(min_dim[2], grid)

min_dim[3]-=1
AddX(min_dim[3], grid)


def printGrid(grid):

    for w in range(min_dim[0], m_dim[0]):
        for z in range(min_dim[1], m_dim[1]):
            for y in range(min_dim[2], m_dim[2]):
                line = ''
                for x in range(min_dim[3], m_dim[3]):
                    line += grid[w][z][y][x]

                print(line)
            print("w = {0}, z = {1}".format(w, z))

for i in range(6):
    runCycle()
    #printGrid(grid)

activeCount = 0
for w in range(min_dim[0], m_dim[0]):
    for z in range(min_dim[1], m_dim[1]):
        for y in range(min_dim[2], m_dim[2]):
            for x in range(min_dim[3], m_dim[3]):
                if grid[w][z][y][x] == '#':
                    activeCount+=1

print(activeCount)







