def main():
    input_file = "input/day19.txt"
    with open(input_file, 'r') as data:
        lines = data.readlines()
        val = 0
        rules = {}
        isRuleLine = True
        count = 0
        for line in lines:
            if isRuleLine:
                if line == "\n":
                    isRuleLine = False
                else:
                    ruleProd = line.strip().split(":")
                    rule = ruleProd[0]
                    prod = ruleProd[1].split("|")
                    prods = []
                    for p in prod:
                        prods.append(p.strip().split(" "))
                    rules[rule] = prods
            elif "" in isRuleValid(rules, "0",line.strip()):
                count += 1
        print(count)
            
def isRuleValid(rules, rule, text):
    ''' return possible valid texts after rule application '''
    possibleTexts = []
    for prods in rules[rule]:
        possibleTexts += (ruleApplications(rules, prods, text))
    return possibleTexts

def ruleApplications(rules, prods, text):
    valid = True
    possibleTexts = [text]
    for p in prods:
        newTexts = []
        for t in possibleTexts:
            if p.find("\"") != -1: 
                if p.replace("\"","") == t[0]:
                    newTexts.append(t[1:])
            else:
                results = isRuleValid(rules, p, t)
                newTexts += results
        possibleTexts = newTexts
    return possibleTexts

if __name__ == '__main__': main()