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
        for tid, tile in tiles.items():
            count = 0
            for tid2, tile2 in tiles.items():
                if tid != tid2 and tile.shareEdge(tile2):
                    count += 1
            
            if count == 2:
                print(f"{tid}: {count}")
                total *= int(tid)
        print(total)
            

class Tile:
    def __init__(self, tid, data):
        self.tid = tid
        self.data = data
        self.rotated = False

    def getEdge(self, direction):
        data = self.data
        # if self.rotated:
        #     if direction == "N":

        #         ret = data[-1]
        #     elif direction == "S":
        #         ret = data[0]
        #     elif direction == "W":
        #         ret = list(map(lambda row : row[-1], data))
        #     else:
        #         ret = list(map(lambda row : row[0], data))
        #     ret.reverse()
        #     return ret
        # else:

        if direction == "N":
            return data[0]
        elif direction == "S":
            return data[-1]
        elif direction == "W":
            return "".join(list(map(lambda row : row[0], data)))
        else:
            return "".join(list(map(lambda row : row[-1], data)))

    def shareEdge(self, otherTile):
        edges = ["N", "S", "W", "E"]

        for e1 in edges:
            e1str = self.getEdge(e1)
            for e2 in edges:
                if e1str == otherTile.getEdge(e2) or e1str == otherTile.getEdge(e2)[::-1]:
                    return True
        return False
if __name__ == '__main__': main()