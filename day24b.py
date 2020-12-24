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
        for i in range(100):
            count = 0
            for val in tiles.values():
                if val:
                    count += 1
            tiles = runDay(tiles)
        count = 0
        for val in tiles.values():
            if val:
                count += 1
        print(count)

def runDay(tiles):
    minX, minY, maxX, maxY = 0,0,0,0
    for tile in tiles:
        minX = min(minX, tile[0])
        minY = min(minY, tile[1])
        maxX = max(maxX, tile[0])
        maxY = max(maxY, tile[1])
    minX -= 2
    maxX += 3
    minY -= 1
    maxY += 2
    newTiles = {}
    for x in range(minX, maxX):
        for y in range(minY, maxY):
            tile = (x,y)
            numNeighbors = getNumNeighbors(x,y,tiles)
            if (tile not in tiles or not tiles[tile]) and numNeighbors == 2:
                newTiles[tile] = True
            elif (tile in tiles and tiles[tile]) and (numNeighbors == 0 or numNeighbors > 2):
                newTiles[tile] = False
            elif tile in tiles:
                newTiles[tile] = tiles[tile]
    return newTiles

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

def getNumNeighbors(x,y,tiles):
    count = 0
    neighbors = [[2,0],[-2,0],[1,1],[-1,1],[-1,-1],[1,-1]]
    for n in neighbors:
        newX = x + n[0]
        newY = y + n[1]
        if (newX,newY) in tiles and tiles[(newX,newY)]:
            count += 1
    return count

if __name__ == "__main__": main()
