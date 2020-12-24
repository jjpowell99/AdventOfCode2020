
def main():
    input_file = "input/day22.txt"
    with open(input_file, 'r') as data:
        lines = data.readlines()
        player1 = []
        player2 = []
        readP1 = True
        for line in lines[1:]:
            if readP1:
                if line == "\n":
                    readP1 = False
                else:
                    player1.append(int(line.strip()))
            elif line.strip().find("Player") == -1:
                player2.append(int(line.strip()))
        total = 0
        won, player1, player2 = playGame(player1, player2)
        comb = player1 if won else player2
        for i in range(1,len(comb)+1):
            total += i * comb[-1 * i]
        print(total)

def playGame(player1, player2):        
    """ Return true if p1 wins """
    p1Seen = []
    p2Seen = []

    while len(player1) > 0 and len(player2) > 0:
        if player1 in p1Seen or player2 in p2Seen:
            return True, player1, player2
        player1Copy = [] + player1
        player2Copy = [] + player2
        p1Seen.append(player1Copy)
        p2Seen.append(player2Copy)

        p1 = player1.pop(0)
        p2 = player2.pop(0)
        if len(player1) >= p1 and len(player2) >= p2:
            won = playGame([] + player1[:p1], [] + player2[:p2])[0]
        else:
            won = p1 > p2
        if won:
            player1.append(p1)
            player1.append(p2)
        else:
            player2.append(p2)
            player2.append(p1)
    winner = len(player1) > 0
    return winner, player1, player2
        
        

    
    
if __name__ == '__main__': main()