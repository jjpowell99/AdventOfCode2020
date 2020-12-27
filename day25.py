def main():
    input_file = "input/day25.txt"
    with open(input_file, 'r') as data:
        lines = data.readlines()
        pk1 = int(lines[0].strip())
        pk2 = int(lines[1].strip())
        mod = 20201227
        subjectNumber = 7
        total = subjectNumber
        anyFound = False
        sk1Found = True
        sk = 0
        for i in range(2,mod):
            total *= subjectNumber
            total %= mod
            if total == pk1:
                anyFound = True
                sk = i
                break
            elif total == pk2:
                anyFound = True
                sk1Found = False
                sk = i
                break
        if anyFound:
            if sk1Found:
                print(pk2**sk % mod)
            else:
                print(pk1**sk % mod)

def func(line):
    line
if __name__ == '__main__': main()