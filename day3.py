def main():
    input_file = "input/day3.txt"
    with open(input_file, 'r') as data:
        lines = data.readlines()
        grid = []
        for line in lines:
            grid.append(line.strip())
        print(traverse(1,1,grid) * traverse(3,1,grid) * traverse(5,1,grid) * traverse(7,1,grid) * traverse(1,2,grid))
        print(traverse(3,1,grid))
def traverse(x,y, grid):
    currentX = 0
    currentY = 0
    count = 0
    while currentY < len(grid):
        # print(grid[currentY][currentX])
        if grid[currentY][currentX] == '#':
            count += 1
        currentX = (currentX + x) % len(grid[0])
        currentY += y
    return count
if __name__ == '__main__': main()