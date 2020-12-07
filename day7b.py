def main():
    input_file = "input/day7.txt"
    with open(input_file, 'r') as data:
        lines = data.readlines()
        val = 0
        rules = {}
        for line in lines:
            func(rules, line.strip())
        target = "shiny gold bag"
        count = total(target, rules)
        print(count-1)
def total(src, rules):
    count = 1
    for (e, c) in rules[src]:
        count += c * total(e, rules)
    return count

def func(rules, line):
    key, val = line.split("contain")
    key = key.replace("bags", "bag").strip()
    val = val.replace(".", "")
    edges = val.split(",")
    edges = list(filter(lambda a : "no other bags" not in a, edges))
    edges = list(map(lambda a : a.strip(), edges))
    edges = list(map(lambda a : a.replace("bags", "bag"), edges))
    edges = list(map(lambda a : (a[a.index(" ") + 1 : ] , int(a[:a.index(" ")])), edges))
    if key in rules:
        rules[key] += (edges)
    else:
        rules[key] = edges
if __name__ == '__main__': main()