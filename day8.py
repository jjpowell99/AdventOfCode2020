def main():
    input_file = "input/day8.txt"
    with open(input_file, 'r') as data:
        lines = data.readlines()
        val = 0
        instructions = []
        for line in lines:
            instructions.append(line.strip().split(" "))

        accum = 0
        seen = []
        i = 0
        while True:
            if i in seen:
                print(accum)
                return
            seen.append(i)
            if instructions[i][0] == "acc":
                accum += int(instructions[i][1])
            elif instructions[i][0] == "jmp":
                i = i + int(instructions[i][1]) - 1
            
            i += 1
def func(line):
    line
if __name__ == '__main__': main()