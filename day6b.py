def main():
    input_file = "input/day6.txt"
    with open(input_file, 'r') as data:
        lines = data.readlines()
        val = 0
        groups = []
        currentGroup = []
        for line in lines:
            if line == "\n":
                groups.append(currentGroup)
                currentGroup = []
            else:
                currentGroup.append(line.strip())
        count = 0
        for g in groups:
            count += func(g)
        print(count)
def func(g):
    count  = 0
    for a in g[0]:
        valid = True
        for g2 in g[1:]:
            valid = valid and a in g2
        if valid:
            count +=1 
    return count
if __name__ == '__main__': main()