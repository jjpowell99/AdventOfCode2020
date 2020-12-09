def main():
    input_file = "input/day9.txt"
    with open(input_file, 'r') as data:
        lines = data.readlines()
        vals = []
        for line in lines:
            vals.append(int(line.strip()))
        addSet = []
        total = 0
        # target = 127
        target = 530627549
        for val in vals:
            if total == target:
                print(min(addSet) + max(addSet))
                return
            addSet.append(val)
            total += val
            while total > target:
                total -= addSet.pop(0)
            if total == target:
                print(min(addSet) + max(addSet))
                return
            

# def func(line):
#     line
if __name__ == '__main__': main()