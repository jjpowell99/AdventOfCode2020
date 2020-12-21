def main():
    input_file = "input/day20.txt"
    with open(input_file, 'r') as data:
        lines = data.readlines()
        tiles = {}
        currentTileData = []
        currentTileId = ""
        for line in lines:
            if line == "\n":
                tiles[currentTileId] = Tile(currentTileId, currentTileData)
                currentTileData = []
                currentTileId = ""
            elif currentTileId == "":
                currentTileId = line.strip()[:-1].split(" ")[1]
            else:
                currentTileData.append(line.strip())
        total = 1
        queue = [tiles.popitem()[1]]
        tiles[queue[0].tid] = queue[0]
        seen = []
        processed = 0
        corners = []
        while len(queue) > 0:
            tile = queue.pop()
            tid = tile.tid
            seen.append(tid)
            processed += 1
            count = 0
            for tid2, tile2 in tiles.items():
                if tid != tid2 and tile2 not in tile.matchList and tile not in tile2.matchList:
                    tile.tryMatch(tile2)
                    if tile2 in tile.matchList and tile2.tid not in seen:
                        queue.append(tile2)
                        seen.append(tid2)
            tile.finished = True
        
            if len(tile.matchList) == 2:
                print(f"{tid}")
                corners.append(tile)
        #         total *= int(tid)
        # print(total)
        print(processed)
        orderedTiles = getOrderedTiles(list(tiles.values()), corners)
        # printOrderedTilesIds(orderedTiles)
        # printOrderedTilesData(orderedTiles)
        for row in orderedTiles:
            for tile in row:
                tile.removeBorder()

        newData = []    
        for row in orderedTiles:
            rowData = [] + row[0].data
            for tile in row[1:]:
                for dataRowInd in range(len(tile.data)):
                    rowData[dataRowInd] += tile.data[dataRowInd]
            for r in rowData:
                newData.append(r)
        combinedTile = Tile("1", newData)
        with open("input/day20pattern.txt") as patternFile:
            lines = patternFile.readlines()
            pattern = []
            for line in lines:
                pattern.append(list(line.replace("\n","")))
        print(combinedTile.getAreaRoughness(pattern))

def getOrderedTiles(tiles, corners):
    startTile = tiles[0]
    for tile in tiles:
        if tile.isTopLeftCorner():
            startTile = tile
            tiles.remove(tile)
            break
    
    rows = [[startTile]]
    
    while len(tiles) > 0:
        print("Tiles left: " + str(len(tiles)) + "\r")
        # printOrderedTilesData(rows)
        matchExists = True
        while matchExists:
            current = rows[-1][-1]
            current.matched = {}
            matchExists = False
            for tile in current.matchList:
                if len(rows) > 1 and tile in rows[-2]:
                    current.trySingleMatch(tile, "N")
                    # current.matchList.remove(tile)
                    # tile.matchList.remove(current)
                    print("Tiles left: " + str(len(tiles)) + "\r")
                    # printOrderedTilesData(rows)
                else:
                    current.trySingleMatch(tile, "E")
                    if "E" in current.matched and not matchExists:
                        matchExists = True
                        rows[-1].append(rows[-1][-1].matched["E"])
                        tiles.remove(tile)
                        # current.matchList.remove(tile)
                        # tile.matchList.remove(current)
                        print("Tiles left: " + str(len(tiles)) + "\r")
                        # printOrderedTilesData(rows)
            # if not matchExists:
            #     print("")
                        
        current = rows[-1][0]
        current.matched = {}
        for tile in current.matchList:
            current.trySingleMatch(tile, "S")
            if "S" in current.matched:
                matchExists = True
                rows.append([rows[-1][0].matched["S"]])
                tiles.remove(tile)
                break
    return rows

def printOrderedTilesIds(tiles):
    for row in tiles:
        for tile in row:
            print(tile, end=" ")
        print()

def printOrderedTilesData(tiles):
    for row in tiles:
        rowData = [] + row[0].data
        for tile in row[1:]:
            for dataRowInd in range(len(tile.data)):
                rowData[dataRowInd] += " " + tile.data[dataRowInd]
        for r in rowData:
            print(r)
        print()

def getOppositeEdge(edge):
    if edge == "N": return "S"
    if edge == "S": return "N"
    if edge == "W": return "E"
    if edge == "E": return "W"

class Tile:
    def __init__(self, tid, data):
        self.tid = tid
        self.data = data
        self.finished = False
        self.matched = {}
        self.matchList = []

    def getEdge(self, direction):
        data = self.data

        if direction == "N":
            return data[0]
        elif direction == "S":
            return data[-1]
        elif direction == "W":
            return "".join(list(map(lambda row : row[0], data)))
        else:
            return "".join(list(map(lambda row : row[-1], data)))

    def isMatch(self, otherTile, selfEdge):
        edge = self.getEdge(selfEdge)
        if selfEdge == "N":
            return edge == otherTile.getEdge("S")
        elif selfEdge == "S":
            return edge == otherTile.getEdge("N")
        elif selfEdge == "W":
            return edge == otherTile.getEdge("E")
        else:
            return edge == otherTile.getEdge("W")

    def tryRotations(self, otherTile, selfEdge):
        for i in range(4):
            otherTile.rotateData90Clock()
            if self.isMatch(otherTile, selfEdge):
                return True
        return False

    def tryFlips(self, otherTile, selfEdge):
        otherTile.flipDataY()
        if self.tryRotations(otherTile, selfEdge):
            return True
        otherTile.flipDataX()
        if self.tryRotations(otherTile, selfEdge):
            return True
        otherTile.flipDataY()
        if self.tryRotations(otherTile, selfEdge):
            return True
        otherTile.flipDataX()
        return self.tryRotations(otherTile, selfEdge)

    def tryMatch(self, otherTile):
        edges = ["N", "S", "W", "E"]

        for e1 in edges:
            if True: #self.isEdgeValid(otherTile, e1):
                if self.tryFlips(otherTile, e1):
                    # self.matched[e1] = otherTile
                    # if getOppositeEdge(e1) in otherTile.matched:
                    #     print(otherTile.tid)
                    # otherTile.matched[getOppositeEdge(e1)] = self
                    self.matchList.append(otherTile)
                    otherTile.matchList.append(self)

    def trySingleMatch(self, otherTile, edge):
        if self.isEdgeValid(otherTile, edge):
            if self.tryFlips(otherTile, edge):
                self.matched[edge] = otherTile
                otherTile.matched[getOppositeEdge(edge)] = self

    def isEdgeValid(self, otherTile, edge):
        valid = edge not in self.matched #and getOppositeEdge(edge) not in otherTile.matched
        # edges = [["N", "S"], ["W", "E"]]
        # if edge in edges[0]:
        #     for e in edges[1]:
        #         if e in self.matched:
        #             valid = valid and (not self.matched[e].finished or edge in self.matched[e].matched)
        # if edge in edges[1]:
        #     for e in edges[0]:
        #         if e in self.matched:
        #             valid = valid and (not self.matched[e].finished or edge in self.matched[e].matched)
        return valid

    def rotateData90Clock(self):
        newData = []
        for col in range(len(self.data[0])):
            newRow = ""
            for row in range(1,len(self.data)+1):
                newRow += self.data[-1 * row][col]
            newData.append(newRow)
        self.data = newData
    
    def flipDataY(self):
        newData = []
        for row in self.data:
            newData.append(row[::-1])
        self.data = newData

    def flipDataX(self):
        self.data = self.data[::-1]
    
    def removeBorder(self):
        newData = self.data[1:-1]
        newData = list(map(lambda row: row[1:-1], newData))
        self.data = newData

    def __str__(self):
        return self.tid

    def isTopLeftCorner(self):
        if len(self.matchList) == 2:
            for m in self.matchList:
                self.trySingleMatch(m, "E")
                self.trySingleMatch(m, "S")
            return "E" in self.matched and "S" in self.matched
        return False
    
    def countPattern(self, pattern):
        count = 0
        colBuffer = len(pattern[0])
        rowBuffer = len(pattern)
        for row in range(len(self.data) - rowBuffer):
            for col in range(len(self.data[0]) - colBuffer):
                valid = True
                for dr in range(rowBuffer):
                    for dc in range(colBuffer):
                        if pattern[dr][dc] == "#" and self.data[row + dr][col + dc] != "#":
                            valid = False
                if valid:
                    count += 1
        return count

    def countWithRotate(self, pattern):
        count = 0
        for i in range(4):
            self.rotateData90Clock()
            self.flipDataX()
            count += self.countPattern(pattern)
            self.flipDataY()
            count += self.countPattern(pattern)
            self.flipDataX()
            count += self.countPattern(pattern)
            self.flipDataY()
            count += self.countPattern(pattern)
            if count > 0:
                return count
        return count

    def getAreaRoughness(self, pattern):
        count = self.countWithRotate(pattern)
        patternNum = 0
        totalNum = 0
        for row in pattern:
            for col in row:
                if col == "#":
                    patternNum += 1
        for row in self.data:
            for col in row:
                if col == "#":
                    totalNum += 1
        return totalNum - (count * patternNum)

if __name__ == '__main__': main()