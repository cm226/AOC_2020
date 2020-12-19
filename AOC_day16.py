def getMatchingRules(ticket):
    mathchingRules = {}
    index = 0
    for v in ticket:
        invalidTicket = True
        for name,r in rules.items():
            for e in [r[0], r[1]]:
                if v >= e[0] and v <= e[1]:
                    invalidTicket = False
                    if name in mathchingRules:
                        mathchingRules[name].append(index)
                    else:
                        mathchingRules[name] = [index]
        if invalidTicket:
            return []
        index+=1

    return mathchingRules

def filterValidIndexes(matching):
    for name,r in rules.items():
        posible_indexes = matching[name]
        all_indexes = list(range(len(myTicket)))

        for a in all_indexes:
            if a not in posible_indexes and a in r[2]:
                r[2].remove(a)

def deduceIndexes():
    removedSomething = True
    while removedSomething:
        removedSomething = False
        for name,r in rules.items():
            if len(r[2]) == 1:
                for n2,r2 in rules.items():
                    if n2!=name and r[2][0] in r2[2]:
                        r2[2].remove(r[2][0])
                        removedSomething = True
    

f = open("input_day16.txt")

section = 0
rules = {}
myTicket = []
scanError = 0
for line in f:

    line = line.strip()
    if line == '':
        continue

    if "your ticket:" in line:
        section = 1
        continue
    if "nearby tickets:" in line:
        section = 2
        continue

    if section == 0:
        # parsing rules
        name,rule = line.split(':')
        r1, r2 = rule.split(" or ")
        r1_range = list(map(int, r1.split('-')))
        r2_range = list(map(int, r2.split('-')))
        rules[name] = [r1_range, r2_range, []]

    if section == 1:
        myTicket = list(map(int, line.split(',')))

        for r in rules.values():
            r[2] = list(range(len(myTicket)))

    if section == 2:
        # parsing nearby
        ticket = list(map(int, line.split(',')))
        matching = getMatchingRules(ticket)
        if len(matching) > 0:
            filterValidIndexes(matching)


deduceIndexes()
val = 1
for r, v in rules.items():
    if 'departure' in r:
        val *= myTicket[v[2][0]]

print(val)

