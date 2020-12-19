f = open("input_day3.txt")
input = []
for line in f:
    input.append(list(line)[:-1])


def check(x_mov, y_mov):
    x = 0
    y = 0
    treeCount = 0
    while y < (len(input)-1):
        x = (x+x_mov) % len(input[0])
        y+=y_mov
        if input[y][x] == '#':
            treeCount+=1
    
    return treeCount;

res = check(1,1) * check(3,1) * check(5,1) * check(7,1) * check(1,2);

print(res)

