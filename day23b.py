def main():
    input_file = "input/day23.txt"
    with open(input_file, 'r') as data:
        lines = data.readlines()
        cups = list(map(int,list(lines[0].strip())))
        # maxVal = 9
        # rounds = 100
        maxVal = 1000000
        rounds = 10000000
        for i in range(10,maxVal+1):
            cups.append(i)
        currentCupInd = 0
        removed = []
        for i in range(rounds):
            if i % 100000 == 0:
                print("Move " + str(i) + ", " + str(100 * (i/rounds)) + "%", end="\r")
            removed = []
            currentCup = cups[currentCupInd]
            removeInd = (currentCupInd + 1) % len(cups)
            for j in range(1,4):
                if removeInd != 0:
                    removeInd %= len(cups)
                if removeInd < currentCupInd:
                    currentCupInd -= 1
                removed.append(cups.pop(removeInd))
            destinationCup = (currentCup-1)
            while(destinationCup in removed or destinationCup == 0):
                destinationCup = (destinationCup - 1)
                if destinationCup <= 0:
                    destinationCup = maxVal
            insertInd = cups.index(destinationCup) + 1
            for r in removed:
                if currentCupInd >= insertInd:
                    currentCupInd += 1
                cups.insert(insertInd, r)
                insertInd += 1
                
            # currentCupInd = cups.index(currentCup)
            currentCupInd = (currentCupInd + 1) % len(cups)
        startInd = cups.index(1)
        total = 1
        print()
        for i in range(1,9):
            print(cups[(startInd+i) % len(cups)], end=",")
        for i in range(1,3):
            total *= cups[(startInd+i) % len(cups)]
        print()
        print(total)
if __name__ == '__main__': main()
# 16902792 - too low