
f = open("input_day2.txt");
valid = 0;
for line in f:
    num, letter, pw = line.split(' ');
    low, high = num.split('-')
    letter = letter[0]

    if (pw[int(high)-1] == letter) != (pw[int(low)-1] == letter): 
        valid+=1

print(valid)