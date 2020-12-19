import sys
import math 
from math import gcd

def findBases(f, s, offset):
    mod = f%s
    intercept = 1
    base = mod
    while base != (offset%s):
        base = (base + mod)%s
        intercept+=1

    return (intercept, s, f, offset)


def LCD(a):
    lcm = a[0]
    for i in a[1:]:
        lcm = lcm*i//gcd(lcm, i)
    return lcm



f = open("input_day13.txt")
arivalTime = int(f.readline())
inservice = f.readline().split(',')


next_bus = 0
next_bus_time = sys.maxsize

firsttBus = int(inservice[0])
offsets = []
for i in range(1,len(inservice)):
    if inservice[i] == 'x':
        continue

    bus = int(inservice[i])
    # part1
    #bus = int(bus)
    #tmp_bus_time = math.ceil(arivalTime / bus) * bus

    #if tmp_bus_time - arivalTime < next_bus_time - arivalTime:
    #    next_bus = bus
    #    next_bus_time = tmp_bus_time

    
    offsets.append(findBases(bus, firsttBus, i))

indexes = []
for ofset in offsets:
    fm = ofset[0]
    interval = ofset[1]
    num = ofset[2]
    os = ofset[3]

    # check all numbers fit with current best
    #all_satisfied = True
    # for ofset in offsets:
    #     num_div = (cur_best_index + ofset[3]) / ofset[2]
    #     if not num_div.is_integer():
    #         all_satisfied = False
    #         break

    # if all_satisfied:
    #     break

    indexes.append((fm*num) - os)

print(indexes)

print(LCD(indexes))