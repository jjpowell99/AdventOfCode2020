def main():
    input_file = "input/day13.txt"
    with open(input_file, 'r') as data:
        lines = data.readlines()
        earliest = int(lines[0].strip())
        buses = list(map(int, filter(lambda x : x != "x", lines[1].strip().split(","))))
        differences = []
        minWait = 1000
        minBus = 0
        for bus in buses:
            diff = (bus - ((earliest % bus))) 
            # differences.append(diff)
            if diff <= minWait:
                minWait = diff
                minBus = bus
        print(minBus * minWait)


if __name__ == '__main__': main()