def main():
    with open("day24.txt") as data:
        lines = data.readlines()
        tiles = {}
        for line in lines:
            tile = getTileFromLine(list(line.strip()))
            if tile in tiles:
                tiles[tile] = not tiles[tile]
            else:
                tiles[tile] = True
        count = 0
        for val in tiles.values():
            if val:
                count += 1
        print(count)

def getTileFromLine(line): 
    x = 0
    y = 0
    while len(line) > 0:
        current = line.pop(0)
        if current == "e":
            x += 2
        elif current == "w":
            x -= 2
        else:
            if current == "n":
                y += 1
            else:
                y -= 1
            nextOne = line.pop(0)
            if nextOne == "e":
                x += 1
            else:
                x -= 1
    return (x,y)

if __name__ == "__main__": main()
