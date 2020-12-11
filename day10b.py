def main():
    input_file = "input/day10.txt"
    with open(input_file, 'r') as data:
        lines = data.readlines()
        vals = [0]
        for line in lines:
            vals.append(int(line.strip()))
        vals.sort()
        vals.append(vals[-1]+3)
        groups = []
        currentGroup = []
        for i in range(len(vals)-1):
            currentGroup.append(vals[i])
            if vals[i+1] - vals[i] == 3:
                groups.append(currentGroup)
                currentGroup = []
        total = 1
        for group in groups:
            total *= runGroup(group)
        print(total)

def runGroup(vals):
    currentSet = (firstRemove(vals))
    count = 0
    while(len(currentSet) > 0):
        newSet = []
        for ind in range(len(currentSet[:-1])):
            i = 1
            while(ind + i < len(currentSet) and canCombine(vals, currentSet[ind], currentSet[ind+i])):
                combined = currentSet[ind] + currentSet[ind+i][-1:]
                if canRemoveMultiple(vals, combined):
                    newSet.append(combined)
                i+=1
        count += len(currentSet)
        currentSet = newSet
    return count + 1

def canCombine(vals, set1, set2):
    return sorted(set1[:-1]) == sorted(set2[:-1]) and set2[-1] not in set1

def firstRemove(vals):
    valid = []

    for i in range(len(vals)):
        if canRemove(vals, vals[i]):
            valid.append([vals[i]])
            
    return valid

def canRemoveMultiple(vals, toRemove):
    temp = []
    temp += vals
    for i in toRemove[:-1]:
        temp.remove(i)
    return canRemove(temp, toRemove[-1])

def canRemove(vals, toRemove):
    i = vals.index(toRemove)
    if i == 0 or i == (len(vals) - 1):
        return False
    prev = vals[i-1]
    nextVal = vals[i+1]
    return nextVal - prev <= 3
if __name__ == '__main__': main()