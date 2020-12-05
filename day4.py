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
    keys = []
    for pf in passFields:
        if len(pf.split(":")) > 1:
            keys.append(pf.split(":")[0])
    for f in fields:
        if f not in keys:
            return False
    return True

    
if __name__ == '__main__': main()