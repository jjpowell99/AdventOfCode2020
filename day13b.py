def main():
    input_file = "input/day13.txt"
    with open(input_file, 'r') as data:
        lines = data.readlines()
        earliest = int(lines[0].strip())
        ids = lines[1].strip().split(",")
        buses = []
        for ind,i in enumerate(ids):
            if i != "x":
                diff = int(i) - ind
                buses.append((int(i),diff))
        m = getM(list(map(lambda x : x[0], buses)))
        total = 0
        for mi, ai in buses:
            bi, binv = getBis(m, mi)
            total = (total + (ai * bi * binv)) % m

        
        print(total)

def getM(mods):
    total = 1
    for mod in mods:
        total *= mod
    return total

def getBis(m, mi):   
    bi = m // mi
    binv = pow(bi, -1, mi)
    return bi, binv

if __name__ == '__main__': main()