def main():
    input_file = "input/day1.txt"
    with open(input_file, 'r') as data:
        lines = data.readlines()
    vals = []
    for line in lines:
        vals.append(int(line))
    for val in vals:
        for val2 in vals:
            for val3 in vals:
                if(val + val2 + val3 == 2020):
                    print(val * val2 * val3)
if __name__ == '__main__': main()