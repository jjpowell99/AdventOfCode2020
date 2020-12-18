def main():
    input_file = "input/day18.txt"
    with open(input_file, 'r') as data:
        lines = data.readlines()
        val = 0
        for line in lines:
            val += func(line.strip().split(" "))
        print(val)

def func(ops):
    
    opList = []
    currentOpSet = []
    numOpen = 0
    for op in ops:
        numOpen += op.count("(")
        numOpen -= op.count(")")
        if op == "*" and numOpen == 0:
            opList.append(currentOpSet)
            currentOpSet = []
        else:
            currentOpSet.append(op)
    opList.append(currentOpSet)
    result = 1
    for opSet in opList:
        result *= addition(opSet)
    return result

def addition(ops):
    leftVal = 0
    operator = "+"
    while(len(ops) > 0):
        current = ops.pop(0)
        if current in ["+", "*"]:
            operator = current
        else:
            if current.find("(") != -1:
                endInd = findLastClosingParen(ops, current.count("("))
                current = current.replace("(","",1)
                ops[endInd] = ops[endInd].replace(")","",1)
                subOps = [current]
                for i in range(endInd+1):
                    subOps.append(ops.pop(0))
                current = func(subOps)
            if operator == "+":
                leftVal += int(current)
            else:
                leftVal *= int(current)
    return leftVal

def findLastClosingParen(ops, numOpen):
    for i in range(len(ops)): 
        numOpen += ops[i].count("(")
        numOpen -= ops[i].count(")")
        if numOpen == 0:
            return i
    print("Couldn't find closing paren")

if __name__ == '__main__': main()