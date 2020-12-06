def countAnyone(line):
    line = line.replace("\n", "")
    counter = 0
    for i in range(0, len(line)):
        if line[i] not in line[:i]:
            counter += 1
    return counter

def countEveryone(lines):
    lines = lines.split("\n")
    base = lines[0]
    for ch in base:
        for line in lines[1:]:
            if ch not in line:
                base = base.replace(ch, "")

    return len(base)

file = open("day6_input.txt", "r")
lines = file.read().split("\n\n")
counterOne = counterTwo = 0

for line in lines:
    counterOne += countAnyone(line)
    counterTwo += countEveryone(line)

print(counterOne)
print(counterTwo)