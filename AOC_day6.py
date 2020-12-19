f = open("input_day6.txt")

group_answers =[]
tmp_answer =[]
for line in f:
    if line == '\n':
        group_answers.append(tmp_answer)
        tmp_answer = []
    else:
        tmp_answer.append(line.strip())

if tmp_answer != []:
    group_answers.append(tmp_answer)

res = 0
for answeSet in group_answers:
    ans_dic = {}
    for person in answeSet:
        for a in list(person):
            if a in ans_dic:
                ans_dic[a] = ans_dic[a] +1
            else:
                ans_dic[a] = 1
            
    for v in ans_dic.values():
        if v == len(answeSet):
            res = res + 1

print(res)
    