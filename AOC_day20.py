
from pprint import pprint
import copy

f = open('input_day20.txt')


tiles = {}


def rotateTile(t, n):
    t2 = copy.deepcopy(t)
    for k in range(n):
        for i in range(len(t)):
            for j in range(len(t[i])):
                t2[i][len(t2)-1-j] = t[j][i] 
        t = copy.deepcopy(t2)

    return t2


def flipTileH(t):
    t = copy.deepcopy(t)
    fliped = []

    for row in t:
        f_row = row
        f_row.reverse()
        fliped.append(f_row)

    return fliped

def flipTileV(t):
    t = copy.deepcopy(t)
    t.reverse()
    return t

def fitTiles(t1, t2, t1_coord):
    
    def checkFitsV(t1, t2, top):
        if top:
            j1 = 0
            j2 = -1
        else : 
            j1 = -1
            j2 = 0
        for i in range(0, len(t1[0])):
            if t1[j1][i] != t2[j2][i]:
                return False
        return True
    
    def checkFitsH(t1, t2, right):
        if right:
            j1 = -1
            j2 = 0
        else:
            j1 = 0
            j2 = -1
        for i in range(0, len(t1)):
            if t1[i][j1] != t2[i][j2]:
                return False
        return True

    
    for flipH in [True, False]:
        for flipV in [True, False]:
            for rotate in range(4):
                tmp_tile = t2
                if flipH:
                    tmp_tile = flipTileH(tmp_tile)
                if flipV:
                    tmp_tile = flipTileV(tmp_tile)

                tmp_tile = rotateTile(tmp_tile, rotate)

                for v in [True, False]:
                    if checkFitsV(t1, tmp_tile, v):
                        return (tmp_tile, (t1_coord[0], t1_coord[1]-1 if v else t1_coord[1]+1))
                    if checkFitsH(t1, tmp_tile, v):
                        return (tmp_tile, (t1_coord[0]+1 if v else t1_coord[0]-1, t1_coord[1]))

    return False



cur_tile = 0
for line in f:
    
    if line.strip() == '':
        continue

    if "Tile" in line:
        cur_tile = line.strip().split(' ')[1][:-1]
        tiles[cur_tile] = []
        continue


    tiles[cur_tile].append(list(line.strip()))


placed_tiles = {}

# pick the first tile 
keys = tiles.keys()
key_it = iter(keys)
t1_key = next(key_it)
t1 = tiles[t1_key]


placed_tiles = []
# find an corner peice, edges will only have 3 adjacent tiles

for t1_name, t1 in tiles.items():
    adjacent = 0
    for t2_name, t2 in tiles.items():
        if t1_name == t2_name:
                continue
        res = fitTiles(t1, t2, (0,0))
        if res:
            adjacent+=1
    
    if adjacent == 2:
        # found an corner
        placed_tiles.append([t1_name])
        break

# go row by row trying to fit peices to the edges
tmp_placed_list = []
tmp_placed_list.append(t1_name)

foundRowPeice = True
row = 0
while foundRowPeice:
    while foundRowPeice:
        foundRowPeice = False
        for t2_name, t2 in tiles.items():
            if t2_name in tmp_placed_list:
                continue

            t1 = tiles[placed_tiles[row][-1]]
            res = fitTiles(t1, t2, (0,0))
            if res and res[1] == (1,0):
                placed_tiles[row].append(t2_name)
                tmp_placed_list.append(t2_name)
                tiles[t2_name] = res[0]
                foundRowPeice = True
            
    # fill in first tile in the next row
    for t2_name, t2 in tiles.items():
        if t2_name in tmp_placed_list:
                continue

        t1 = tiles[placed_tiles[row][0]]
        res = fitTiles(t1, t2, (0,0))
        if res and res[1][1] != 0:
            newTile = res[0]
            if res[1][1] < 0: # first row is upside down so flip it
                for t_name in placed_tiles[row]:
                    tiles[t_name] = flipTileV(tiles[t_name])
                newTile = flipTileV(newTile)

            placed_tiles.append([t2_name])
            tmp_placed_list.append(t2_name)
            tiles[t2_name] = newTile
            foundRowPeice = True
    row+=1

def removeborder(t):
    t = t[1:-1]
    for i in range(len(t)):
        t[i] = t[i][1:-1]
    return t

#fullimage = [[None]* (8*len(placed_tiles[0]))] * (8*len(placed_tiles))
fullimage = []
for i in range (8*len(placed_tiles)):
    fullimage.append([None]* (8*len(placed_tiles[0])))

i = 0
j = 0
for row in placed_tiles:
    for name in row:
        t = tiles[name]
        t = removeborder(t)

        for r in range(len(t)):
            for c in range(len(t[r])):
                fullimage[(j*8)+r][(i*8)+c] = t[r][c]
        i+=1
    i=0
    j+=1


for row in fullimage:
    line = ''
    for col in row:
        line += col
    print(line)


# get the right orientation
pattern = []
pattern.append(list("                  #"))
pattern.append(list("#    ##    ##    ###"))
pattern.append(list(" #  #  #  #  #  #  "))


# fullimage = flipTileH(fullimage)
# fullimage = rotateTile(fullimage,3)

# print()

# for row in fullimage:
#     line = ''
#     for col in row:
#         line += col
#     print(line)

for flipH in [True, False]:
        for flipV in [True, False]:
            for rotate in range(4):

                if flipH:
                    fullimage = flipTileH(fullimage)
                if flipV:
                    fullimage = flipTileV(fullimage)

                fullimage = rotateTile(fullimage, rotate)

                num_matches = 0
                for i in range(0,len(fullimage[0])-3):
                    for j in range(0,len(fullimage)-19):
                        match=True
                        for y in range(3):
                            for x in range(19):
                                if pattern[y][x] == '#' and fullimage[i+y][j+x] != '#':
                                    match = False
                        if match:
                            print("match at ",i,j)
                            num_matches+=1
                if num_matches >0:
                    numHash = 0
                    for row in fullimage:
                        numHash += row.count("#")

                    numHash -= num_matches*15
                    print(numHash)
                    exit()                           



