def main():
    input_file = "input/day7.txt"
    with open(input_file, 'r') as data:
        lines = data.readlines()
        val = 0
        rules = {}
        for line in lines:
            func(rules, line.strip())
        target = "shiny gold bag"
        count = 0
        for rule in rules:
            if bfs(target, rule, rules):
                count += 1
        print(count)
def bfs(target, src, rules):
    if target == src:
        return False
    queue = []
    queue += rules[src]
    visited = []
    while len(queue) > 0:
        current = queue.pop(0)
        visited.append(current)
        if current == target:
            return True
        if current in rules:
            for e in rules[current]:
                if e not in visited and e not in queue:
                    queue.append(e)
    return False


def func(rules, line):
    key, val = line.split("contain")
    key = key.replace("bags", "bag").strip()
    val = val.replace(".", "")
    edges = val.split(",")
    edges = list(filter(lambda a : "no other bags" not in a, edges))
    edges = list(map(lambda a : a.strip(), edges))
    edges = list(map(lambda a : a[a.index(" ") + 1 : ], edges))
    edges = list(map(lambda a : a.replace("bags", "bag"), edges))
    if key in rules:
        rules[key] += (edges)
    else:
        rules[key] = edges
if __name__ == '__main__': main()