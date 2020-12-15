def main():
    input_file = "input/day15.txt"
    with open(input_file, 'r') as data:
        lines = data.readlines()
        vals = {}
        line = lines[0].split(",")
        i = len(line) - 1
        said = int(line[-1])
        for count, val in enumerate(line[:-1]):
            vals[int(val)] = count
        for j in range(i, 29999999):
            if said in vals:
                nextSaid = j - vals[said]
            else:
                nextSaid = 0
            vals[said] = j
            said = nextSaid

        print(said)

if __name__ == '__main__': main()