from copy import copy
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
    roundHistory = {}

    while len(player1) > 0 and len(player2) > 0:
        p1str = str(player1)
        p2str = str(player2)
        stateHash = p1str + ',' + p2str

        if stateHash in roundHistory:
            return 'p1', player1
        
        roundHistory[stateHash] = ''

        c1 = player1.pop(0)
        c2 = player2.pop(0)

        subWinner = None
        if len(player1) >= c1 and len(player2) >= c2:
            subWinner, deck = simulateGame(copy(player1[0:c1]), copy(player2[0:c2]))

        if subWinner != None:
            if subWinner == 'p1':
                player1.extend([c1,c2])
            else:
                player2.extend([c2,c1])
        else:
            if c1>c2:
                player1.extend([c1, c2])
            else:
                player2.extend([c2, c1])

    if len(player2)!=0:
        return 'p2', player2
    else:
        return 'p1', player1

    
def calcScore(winner):
    # calc score
    score = 0
    i = 1
    while len(winner) != 0:
        score+= winner.pop(-1) * i
        i+=1

    print(score)

winner, deck = simulateGame(player1, player2)

print(winner, deck)

calcScore(deck)