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
        
        while len(player1) > 0 and len(player2) > 0:
            p1 = player1.pop(0)
            p2 = player2.pop(0)
            if p1 > p2:
                player1.append(p1)
                player1.append(p2)
            else:
                player2.append(p2)
                player2.append(p1)
        total = 0
        comb = player1 + player2
        for i in range(1,len(comb)+1):
            total += i * comb[-1 * i]
        print(total)
if __name__ == '__main__': main()