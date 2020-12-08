def main():
    input_file = "input/day8.txt"
    with open(input_file, 'r') as data:
        lines = data.readlines()
        val = 0
        instructions = []
        orig = []
        for line in lines:
            instructions.append(line.strip().split(" "))
        orig += instructions
        for i in range(len(orig)):
            if instructions[i][0] == "jmp":
                instructions[i] = ["nop", instructions[i][1]]
                val = run(instructions)
                if not val:
                    instructions = []
                    instructions += orig
                else:
                    print(val)
                    return
            elif instructions[i][0] == "nop":
                instructions[i] = ["jmp", instructions[i][1]]
                if not val:
                    instructions = []
                    instructions += orig
                else:
                    print(val)
                    return
def run(instructions):
    accum = 0
    seen = []
    i = 0
    while i < len(instructions):
        if i in seen:
            return False
        seen.append(i)
        if instructions[i][0] == "acc":
            accum += int(instructions[i][1])
        elif instructions[i][0] == "jmp":
            i = i + int(instructions[i][1]) - 1
        i += 1
    return accum
if __name__ == '__main__': main()