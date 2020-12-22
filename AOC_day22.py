f = open("input_day22.txt")

player1 = []
player2 = []
cur_player = player1
for l in f:
    if l.strip() == '':
        continue

    if "Player" in l:
        if "2" in l :
            cur_player = player2
        continue

    cur_player.append(int(l))

# sim game
def simulateGame(player1, player2):
    while len(player1) > 0 and len(player2) > 0:
        c1 = player1.pop(0)
        c2 = player2.pop(0)

        if c1>c2:
            player1.extend([c1, c2])
        else:
            player2.extend([c2, c1])

    winner = player2 if len(player2)!=0 else player1
    
def calcScore(winner):
    # calc score
    score = 0
    i = 1
    while len(winner) != 0:
        score+= winner.pop(-1) * i
        i+=1

    print(score)
