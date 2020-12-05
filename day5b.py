def main():
    input_file = "input/day5.txt"
    with open(input_file, 'r') as data:
        lines = data.readlines()
        maxId = 0
        ids = []
        for line in lines:
            row = line.strip()[:-3]
            col = line.strip()[-3:]
            row = row.replace("B","1")
            row = row.replace("F", "0")
            col = col.replace("R", "1")
            col = col.replace("L", "0")
            rowi = int(row, 2)
            coli = int(col, 2)
            val = rowi * 8 + coli
            ids.append(val)
        for i in ids:
            if (i + 1) not in ids and (i + 2) in ids:
                print(i+1)
if __name__ == '__main__': main()