f = open("input_day14.txt")

def getPermutations(address, mask):
    
    perms = []
    for c in mask:
        if c == 'X':
            if len(perms) == 0:
                perms.append(0)
                perms.append(1)
            else:
                permsLen = len(perms)
                for i in range(permsLen):
                    perms[i] = perms[i] << 1
                    perms.append(perms[i]+1)
        else:
            for i in range(len(perms)):
                perms[i] = perms[i] << 1


    for i in range(len(perms)):
        perms[i] = perms[i] | address

    return perms


memory = {}
bit_mask = 0
x_mask = 0
cur_mask = ''
for line in f:
    op, val = line.split('=')
    op = op.strip()
    val = val.strip()
    if op == 'mask':
        cur_mask = list(val)
        bit_mask = 0
        for b in cur_mask:
            bit_mask = bit_mask << 1
            x_mask = x_mask << 1
            if b == '1':
                bit_mask+=1
            if b != 'X':
                x_mask +=1
    else:
        addres = int(op[op.find('[')+1:op.find(']')])
        val = int(val)

        addres = addres | bit_mask
        addres = addres & x_mask
        addreses = getPermutations(addres, cur_mask)

        for a in addreses:
            memory[a] = val

#print(memory)
        
sum = 0
for val in memory.values():
    sum+=val

print(sum)