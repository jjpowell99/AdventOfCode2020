def main():
    input_file = "input/day10.txt"
    with open(input_file, 'r') as data:
        lines = data.readlines()
        vals = [0]
        for line in lines:
            vals.append(int(line.strip()))
        vals.sort()
        ones = 0
        threes = 0
        for i in range(len(vals)-1):
            diff = vals[i+1] - vals[i]
            if diff == 1:
                ones += 1
            elif diff == 3:
                threes += 1
        threes += 1
        print(ones * threes)
def func(line):
    line
if __name__ == '__main__': main()