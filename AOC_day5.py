
f = open("input_day5.txt")

all_ids = []


for line in f:
    start = 0 
    end = 127
    chars = list(line)
    size = 128
    for i in range(7):
        char = chars[i]
        size = size / 2
        if(char == 'F'):
            end = start + (size-1)
        elif(char == 'B'):
            start = start + size
        

    col_start = 0
    col_end = 7  
    size = 8  
    for i in range(3):
        char = chars[i+7]
        size = size / 2
        if(char == 'L'):
            col_end = col_start + (size-1)
        elif(char == 'R'):
            col_start = col_start + (size)

    seatID = (start * 8) + col_start
    all_ids.append(seatID)

all_ids.sort()

lastid = all_ids[0]
for id in all_ids:
    if (id - lastid) > 1:
        print(id)
    lastid = id