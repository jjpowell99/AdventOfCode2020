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
        nearbyTickets = (getInvalidCount(rules, nearbyTickets))
        allTickets = []
        allTickets += nearbyTickets
        allTickets += [myTicket]
        validRules = getValidRules(getValsForIndexes(allTickets), rules)
        matchedRules = matchValidRules(validRules)
        total = 1
        for rule, val in matchedRules.items():
            if rule.startswith("departure"):
                total *= myTicket[val]
        print(total)
            
def matchValidRules(validRules):
    matched = {}
    while(len(validRules.keys()) > 0):
        ruleToRemove = ""
        valToRemove = ""
        for rule, vals in validRules.items():
            if len(vals) == 1:
                ruleToRemove = rule
                valToRemove = vals[0]
                break
        try:
            matched[rule] = valToRemove
            validRules.pop(ruleToRemove)
            for rule in validRules:
                if valToRemove in validRules[rule]:
                    validRules[rule].remove(valToRemove)
        except Exception as e:
            print(e)
    return matched
    
def getValsForIndexes(allTickets):
    vals = {}
    for i in range(len(allTickets[0])):
        vals[i] = []
    for t in allTickets:
        for ind, val in enumerate(t):
            vals[ind].append(val)
    return vals

def getValidRules(indexValues, rules):
    validRules = {}
    for rule in rules:
        validRules[rule] = []
    for ind, vals in indexValues.items():
        for rule, ranges in rules.items():
            if allValsMatchRule(vals, ranges):
                validRules[rule].append(ind)
    return validRules

def allValsMatchRule(vals, ranges):
    valid = True
    for val in vals:
        rangeValid = False
        for indR in ranges:
            rangeValid = rangeValid or (val >= indR[0] and val <= indR[1])
        # if not rangeValid:
        #     print(str(val) + " not in " + str(ranges))
        valid = valid and rangeValid
    return valid

def getInvalidCount(rules, nearby):
    count = 0
    toRemove = []
    for n in nearby:
        for v in n:
            if not inAnyRule(rules, v):
                toRemove.append(n)
                break
    for rem in toRemove:
        nearby.remove(rem)
    return nearby

def inAnyRule(rules, val):
    inRule = False
    for r in rules.values():
        for indR in r:
            inRule = inRule or (val >= indR[0] and val <= indR[1])
    return inRule

if __name__ == '__main__': main()