def main():
    input_file = "input/day9.txt"
    with open(input_file, 'r') as data:
        lines = data.readlines()
        vals = []
        for line in lines:
            vals.append(int(line.strip()))
       
        for ind in range(len(lines)):
            numCheck = 25
            i = ind + numCheck
            valid = False
            for j in vals[ind:ind+numCheck]:
                for k in vals[ind:ind+numCheck]:
                    valid = valid or (j != k and j+k == vals[i])
            if not valid:
                print(vals[i])
                return
# def func(line):
#     line
if __name__ == '__main__': main()