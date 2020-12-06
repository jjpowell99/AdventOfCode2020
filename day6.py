def main():
    input_file = "input/day6.txt"
    with open(input_file, 'r') as data:
        lines = data.readlines()
        val = 0
        groups = []
        currentGroup = ""
        for line in lines:
            if line == "\n":
                groups.append(currentGroup)
                currentGroup = ""
            else:
                currentGroup += line.strip()
        count = 0
        for g in groups:
            count += func(g)
        print(count)
def func(g):
    count  = 0
    for i in range(26):
        if chr(ord('a') + i) in g:
            count +=1 
    return count
if __name__ == '__main__': main()