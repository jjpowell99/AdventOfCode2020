def main():
    input_file = "input/day16.txt"
    with open(input_file, 'r') as data:
        lines = data.readlines()
        rules = {}
        readingRules = True
        readingMyTicket = False
        readingNearbyTickets = False
        myTicket = []
        nearbyTickets = []
        for line in lines:
            if readingRules:
                if line == "\n":
                    readingRules = False
                else:
                    fnr = line.strip().split(":")
                    field, ranges = fnr[0], fnr[1]
                    ranges = ranges.strip().split("or")
                    actualRanges = []
                    for r in ranges:
                        actualRanges.append(list(map(int, r.strip().split("-"))))
                    rules[field] = actualRanges
            elif readingMyTicket:
                myTicket = list(map(int, line.strip().split(",")))
                readingMyTicket = False
            elif readingNearbyTickets:
                nearbyTickets.append(list(map(int, line.strip().split(","))))
            elif line.strip() == "nearby tickets:":
                readingNearbyTickets = True
            elif line.strip() == "your ticket:":
                readingMyTicket = True
        print(getInvalidCount(rules, nearbyTickets))

def getInvalidCount(rules, nearby):
    count = 0
    for n in nearby:
        for v in n:
            if not inAnyRule(rules, v):
                count += v
    return count

def inAnyRule(rules, val):
    inRule = False
    for r in rules.values():
        for indR in r:
            inRule = inRule or (val >= indR[0] and val <= indR[1])
    return inRule

if __name__ == '__main__': main()