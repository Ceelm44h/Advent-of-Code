def countCombinations() -> int:
    path = [1]
    for i in range(1, len(lines)):
        comb = 0
        for j in range(i):
            if lines[j] + 3 >= lines[i]:
                comb += path[j]
        path.append(comb)
    return comb

file = open("day10_input.txt", "r")
lines = [int(line) for line in file.read().splitlines()]

lines.append(0)
lines.sort()
oneDifference = threeDifference = 0
i = 1
while i < len(lines):
    diff = lines[i] - lines[i-1]
    if diff == 1:
        oneDifference += 1
    elif diff == 3:
        threeDifference += 1
    elif diff != 2:
        break
    
    i += 1

threeDifference += 1
combinations = list()
print(oneDifference * threeDifference)
print(countCombinations())