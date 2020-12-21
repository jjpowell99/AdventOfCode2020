def main():
    input_file = "input/day21.txt"
    with open(input_file, 'r') as data:
        lines = data.readlines()
        ingredients = {}
        allergens = {}
        for line in lines:
            spl = line.strip().split("(")
            ings = spl[0].strip().split(" ")
            alls = spl[1].replace("contains", "").replace(")", "").replace(" ", "").strip().split(",")
            for i in ings:
                if i in ingredients:
                    ingredients[i] += 1
                else:
                    ingredients[i] = 1
            for a in alls:
                if a in allergens:
                    allergens[a].intersection_update(ings)
                else:
                    allergens[a] = set(ings)
        
        knownAlls = {}
        while len(allergens.keys()) > 0:
            toRemove = ""
            for a in allergens:
                if len(allergens[a]) == 1:
                    toRemove = a
                    break
            knownAlls[toRemove] = list(allergens[toRemove])[0]
            allergens.pop(toRemove)
            removeVal(knownAlls[toRemove], allergens)
        for a in sorted(knownAlls.keys()):
            print(knownAlls[a], end=",")

def removeVal(val, d):
    for e in d:
        if val in d[e]:
            d[e].remove(val)
if __name__ == '__main__': main()