def main():
    input_file = "input/day2.txt"
    with open(input_file, 'r') as data:
        lines = data.readlines()
        count = 0
        for line in lines:
            count += validPass(line)
    print(count)
def validPass(line):
    arr = line.split(" ")
    minMax = arr[0].split("-")
    minVal = int(minMax[0])
    maxVal = int(minMax[1])
    char = arr[1][0]
    count = 0
    for c in arr[2]:
        if c == char:
            count += 1
    part2Check = (arr[2][minVal - 1] == char) ^ (arr[2][maxVal - 1] == char)
    return 1 if part2Check else 0
if __name__ == '__main__': main()