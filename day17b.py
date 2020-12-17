def main():
    input_file = "input/day17.txt"
    with open(input_file, 'r') as data:
        lines = data.readlines()
        vals = {}
        minW = 0
        maxW = 1
        minZ = 0
        maxZ = 1
        minY = 0
        maxY = len(lines)
        minX = 0
        maxX = len(lines[0].strip())
        data = []
        for line in lines:
            data.append(list(line.strip()))
        for x in range(minX, maxX):
            for y in range(minY, maxY):
                for z in range(minZ, maxZ):
                    key = hashKey(x,y,z,0)
                    vals[key] = data[y][x]
                    
        for i in range(6):
            minW -= 1
            maxW += 1
            minZ -= 1
            maxZ += 1
            minY -= 1
            maxY += 1
            minX -= 1
            maxX += 1
            vals = runRound(vals, range(minX, maxX), range(minY, maxY), range(minZ, maxZ), range(minW, maxW))
        count = 0
        for val in vals.values():
            if val == "#":
                count += 1
        print(count) 
            
def runRound(vals, xRange, yRange, zRange, wRange):
    newVals = {}
    for x in xRange:
        for y in yRange:
            for z in zRange:
                for w in wRange:
                    newVal = getNewVal(vals, x, y, z, w)
                    newVals[hashKey(x,y,z,w)] = newVal
    # printGrid(vals, xRange, yRange, zRange)
    return newVals

def getNewVal(vals, x, y, z, w):
    # if hashKey(x,y,z) == "0,1,-1":
    #     print()
    neighborActiveCount = getNumActiveNeighbors(vals, x, y, z, w)
    currentVal = getVal(vals, x, y, z, w)
    newVal = "."
    if currentVal == "#" and (neighborActiveCount == 2 or neighborActiveCount == 3):
        newVal = "#"
    elif currentVal == "." and neighborActiveCount == 3:
        newVal = "#"
    return newVal

def getVal(vals, x, y, z, w):
    key = hashKey(x,y,z,w)
    if key in vals:
        return vals[key]
    else:
        return "."

def getNumActiveNeighbors(vals, x, y, z, w):
    count = 0
    for dx in range(-1,2):
        for dy in range(-1,2):
            for dz in range(-1,2):
                for dw in range(-1,2):
                    newX = dx + x
                    newY = dy + y
                    newZ = dz + z
                    newW = dw + w
                    if (not (dx == 0 and dy == 0 and dz == 0 and dw == 0)) and getVal(vals, newX, newY, newZ, newW) == "#":
                        count += 1
    return count

def hashKey(x,y,z,w):
    return str(x) + "," + str(y) + "," + str(z) + "," + str(w)

def printGrid(vals, xRange, yRange, zRange, wRange):
    for w in wRange:
        for z in zRange:
            print("z=" + str(z) + ", w=" + str(w))
            for y in yRange:
                for x in xRange:
                    print(getVal(vals, x, y, z, w), end="")
                print()
if __name__ == '__main__': main()