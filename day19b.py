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
            else:
                possibleText = isRuleValid(rules, "42", line.strip())
                maxReps = 0
                while len(possibleText) > 0:  
                    current = possibleText.pop(0)
                    results = isRuleValid(rules, "42", current)
                    maxReps += 1
                    possibleText += results
                    for r in results:
                        if isRepeatedRule(rules, "31", r, maxReps):
                            count += 1
                            possibleText = []
                            break
        print(count)

def isRepeatedRule(rules, rule, text, maxReps):
    possibleText = isRuleValid(rules, rule, text)
    while len(possibleText) > 0 and maxReps > 0:  
        if "" in possibleText:
            return True
        current = possibleText.pop(0)
        results = isRuleValid(rules, rule, current)
        possibleText += results
        maxReps -= 1
    return False

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
                if len(t) > 0 and p.replace("\"","") == t[0]:
                    newTexts.append(t[1:])
            else:
                results = isRuleValid(rules, p, t)
                newTexts += results
        possibleTexts = newTexts
    return possibleTexts

if __name__ == '__main__': main()

# Guessed 241 - too high