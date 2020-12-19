import math
import operator

nav = [[line[0],int(line[1:])] for line in open("input_day12.txt")]

wp_pos = [1,10]
s_pos = [0,0]

for n in nav:
    ins = n[0]
    val = n[1]

    if ins == 'F':
        v = [val*x for x in wp_pos]
        s_pos= list(map(operator.add, s_pos, v))
    if ins == 'L':
        v = math.floor(val / 90)
        for i in range(v):
            tmp_wp = wp_pos.copy()
            wp_pos[1] = -wp_pos[0]
            wp_pos[0] = tmp_wp[1]
    if ins == 'R':
        v = math.floor(val / 90)
        for i in range(v):
            tmp_wp = wp_pos.copy()
            wp_pos[1] = wp_pos[0] 
            wp_pos[0] = -tmp_wp[1]
    if ins == 'N':
        wp_pos[0]+=val
    if ins == 'E':
        wp_pos[1]+=val
    if ins == 'S':
        wp_pos[0]-=val
    if ins == 'W':
        wp_pos[1]-=val

print(s_pos)
print(abs(s_pos[0])+abs(s_pos[1]))
