def main():
    input_file = "input/day14.txt"
    with open(input_file, 'r') as data:
        lines = data.readlines()
        vals = {}
        mask = ""
        for line in lines:
            val = line.split("=")
            if val[0].startswith("mask"):
                mask = val[1].strip()
            else:
                memLoc = int(val[0][val[0].index("[") + 1 : val[0].index("]")])
                setVal = int(val[1].strip())
                memLocs = applyMask(mask, memLoc)
                for m in memLocs:
                    vals[m] = setVal
        total = 0
        for key, val in vals.items():
            total += val
        print(total)

def floatingCombinations(val):
    combs = [val]
    while combs[0].find('X') != -1:
        current = combs.pop(0)
        combs.append(current.replace('X','0',1))
        combs.append(current.replace('X','1',1))
    return list(map(lambda x: int(x,2), combs))

def applyMask(mask, val):
    ret = ""
    binVal = getBinary(val)
    for i in range(len(mask)):
        if(mask[i] == '0'):
            ret += binVal[i]
        else:
            ret += mask[i]
    return floatingCombinations(ret)

def getBinary(val):
    binary = bin(val)[2:]
    numZeros = 36 - len(binary)
    return (numZeros * '0') + binary

if __name__ == '__main__': main()