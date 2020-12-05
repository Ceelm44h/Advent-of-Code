def getRow(line):
    bin = line.replace("B", "1").replace("F", "0")
    return int(bin, 2)

def getColumn(line):
    bin = line.replace("R", "1").replace("L", "0")
    return int(bin, 2)

def getID(line):
    return getRow(line[:7]) * 8 + getColumn(line[7:])

r = open("day5_input.txt", "r")
lines = r.read().splitlines()

highest = -1
for line in lines:
    candidate = getID(line)
    if candidate > highest:
        highest = candidate
print(highest)

seats = [getID(line) for line in lines]
for i in range(96, 911): #lowest to highest
    if i not in seats:
        print(i)
        break