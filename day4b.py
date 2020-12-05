def main():
    input_file = "input/day4.txt"
    with open(input_file, 'r') as data:
        lines = data.readlines()
        passes = []
        currentPass = ""
        for line in lines:
            if len(line) < 3:
                passes.append(currentPass)
                currentPass = ""
            else:
                currentPass += " " + line.strip() + " "
        count = 0
        for p in passes:
            if validatePass(p):
                count += 1
        print(count)
def validatePass(passport):
    fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    passFields = passport.split(" ")
    keys = {}
    for pf in passFields:
        sp = pf.split(":")
        if len(sp) > 1:
            keys[sp[0]] = sp[1]
    valid = True
    for f in fields:
        if f not in keys:
            return False
        if f == "byr":
            valid = valid and len(keys[f]) == 4 and int(keys[f]) >= 1920 and int(keys[f]) <= 2002
        if f == "iyr":
            valid = valid and len(keys[f]) and int(keys[f]) >= 2010 and int(keys[f]) <= 2020
        if f == "eyr":
            valid = valid and len(keys[f]) and int(keys[f]) >= 2020 and int(keys[f]) <= 2030
        if f == "hgt":
            valid = valid and  validHeight(keys[f])
        if f == "hcl":
            valid = valid and  validHair(keys[f])
        if f == "ecl":
            valid = valid and  validEye(keys[f])
        if f == "pid":
            valid = valid and validPID(keys[f])
    return valid
def validHeight(height):
    if len(height) < 3:
        return False
    units = height[-2:]
    val = int(height[:-2])
    if units == "cm":
        return val >= 150 and val <= 193
    elif units == "in":
        return val >= 59 and val <= 76
    else:
        return False

def validHair(hair):
    valid = hair[0] == '#'
    poss = list(map(str,(range(0,10))))
    poss += ['a','b','c','d','e','f']
    for c in hair[1:]:
        valid = valid and c in poss
    return valid

def validEye(eye):
    poss = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    return eye.strip() in poss

def validPID(pid):
    try:
        int(pid)
        return len(pid) == 9
    except:
        return False
    
if __name__ == '__main__': main()