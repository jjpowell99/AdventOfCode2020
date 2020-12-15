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
                setVal = int(val[1])
                vals[memLoc] = applyMask(mask, setVal)
        total = 0
        for key, val in vals.items():
            total += val
        print(total)

def applyMask(mask, val):
    ret = ""
    binVal = getBinary(val)
    for i in range(len(mask)):
        if(mask[i] == 'X'):
            ret += binVal[i]
        else:
            ret += mask[i]
    return int(ret,2)

def getBinary(val):
    binary = bin(val)[2:]
    numZeros = 36 - len(binary)
    return (numZeros * '0') + binary

if __name__ == '__main__': main()