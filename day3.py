input = open("day3_input.txt", "r")
lines = input.read().splitlines()

def countTrees(xOffset, yOffset):
    counter = xPos = 0
    for i in range(0, len(lines), yOffset):
        line = lines[i]
        if line[xPos] == '#':
            counter += 1
    
        xPos = (xPos+xOffset)%len(line)
    return counter

print(countTrees(1, 1) * countTrees(3, 1) * countTrees(5, 1) * countTrees(7, 1) * countTrees(1, 2))