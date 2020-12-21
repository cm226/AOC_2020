from pprint import pprint

f = open('input_day21.txt')

pos_ingred_alergin_map = {}
meals = []

for l in f:
    ingreds, alegrins = l.split('(')
    ingreds = ingreds.strip().split(' ')
    alegrins = alegrins.strip()[len("contains"):-1].split(',')

    for ingred in ingreds:
        if ingred not in pos_ingred_alergin_map:
            pos_ingred_alergin_map[ingred] =[]

        for a in alegrins:
            if a not in pos_ingred_alergin_map[ingred]:
                pos_ingred_alergin_map[ingred].append(a)

    meals.append((ingreds, alegrins))


for ingreds, meal_alergins in meals:
    # remove all the posible alergins frm ingreds that are NOT in this list of ingreds 
    for ingred, pos_alergins in pos_ingred_alergin_map.items():

        if ingred not in ingreds:
            pos_ingred_alergin_map[ingred] = [a for a in pos_alergins if a not in meal_alergins]


madeRemoval = True
while madeRemoval:
    madeRemoval = False
    for ingred, pos_alergins in pos_ingred_alergin_map.items():
        if len(pos_alergins) == 1:
            for i2, a2 in pos_ingred_alergin_map.items():
                if i2!=ingred and pos_alergins[0] in a2:
                    pos_ingred_alergin_map[i2].remove(pos_alergins[0])
                    madeRemoval = True

pprint(pos_ingred_alergin_map)

dangerous_ingreds = []
for ingred, pos_alergins in pos_ingred_alergin_map.items():
    if len(pos_alergins) == 1:
        dangerous_ingreds.append((ingred, pos_alergins[0]))

dangerous_ingreds = sorted(dangerous_ingreds, key=lambda x: x[-1])
for ingred, alergin in dangerous_ingreds:
    print(ingred,",",end='', sep='')

