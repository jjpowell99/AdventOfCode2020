def main():
    input_file = "input/day11.txt"
    with open(input_file, 'r') as data:
        lines = data.readlines()
        grid = []
        val = 0
        for line in lines:
            grid.append(list(line.strip()))
        changed = True
        while(changed):
            grid, changed = gridRound(grid)
        print(countTotalOccupied(grid))

def countTotalOccupied(grid):
    count = 0
    for row in grid:
        for col in row:
            if col == "#":
                count += 1
    return count

def gridRound(grid):
    gridCounts = getCounts(grid)
    changed = False
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            newValue, newChanged = newVal(grid[r][c], gridCounts[r][c])
            grid[r][c] = newValue
            changed = changed or newChanged
    return grid, changed

def getCounts(grid):
    gridCounts = []
    for r in range(len(grid)):
        rowCounts = []
        for c in range(len(grid[0])):
            rowCounts.append(getCount(grid, r, c))
        gridCounts.append(rowCounts)
    return gridCounts

def getCount(grid, r, c):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (not(i==0 and j==0)) and firstInDirection(grid, r, c, i, j):
                count += 1
    return count

def firstInDirection(grid, r, c, dr, dc):
    currentR = r + dr
    currentC = c + dc
    while(onGrid(grid, currentR, currentC)):
        if grid[currentR][currentC] == "L":
            return False
        elif grid[currentR][currentC] == "#":
            return True
        currentR += dr
        currentC += dc
    return False

def onGrid(grid, r, c):
    return not( r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]))

def isOccupied(grid, r, c):
    if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
        return False
    return grid[r][c] == "#"

def newVal(currentVal, numOccupied):
    if currentVal == "L" and numOccupied == 0:
        return "#", True
    elif currentVal == "#" and numOccupied >= 5:
        return "L", True
    return currentVal, False

if __name__ == '__main__': main()