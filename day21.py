def main():
    input_file = "input/test2.txt"
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
        allIngs = set()
        for ings in allergens.values():
            allIngs.update(ings)
        clearIngs = set(ingredients.keys()).difference(allIngs)
        count = 0
        for i in clearIngs:
            count += ingredients[i]
        print(count)

if __name__ == '__main__': main()