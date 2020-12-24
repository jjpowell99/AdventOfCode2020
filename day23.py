def main():
    input_file = "input/day23.txt"
    with open(input_file, 'r') as data:
        lines = data.readlines()
        cups = list(map(int,list(lines[0].strip())))
        currentCupInd = 0
        removed = []
        mod = 10
        for i in range(100):
            removed = []
            currentCup = cups[currentCupInd]
            for j in range(1,4):
                currentCupInd = cups.index(currentCup)
                removed.append(cups.pop((currentCupInd+1) % len(cups)))
            destinationCup = (currentCup-1)
            while(cups.count(destinationCup) == 0):
                destinationCup = (destinationCup - 1)
                if destinationCup <= 0:
                    destinationCup = mod-1
            insertInd = cups.index(destinationCup) + 1
            for r in removed:
                cups.insert(insertInd, r)
                insertInd += 1
            currentCupInd = cups.index(currentCup)
            currentCupInd = (currentCupInd + 1) % len(cups)
        startInd = cups.index(1)
        for i in range(1,9):
            print(cups[(startInd+i) % len(cups)], end="")
        print()
if __name__ == '__main__': main()