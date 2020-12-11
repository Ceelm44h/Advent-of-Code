def getNumberOfAdjacent(x, y) -> int:
    sum = 0
    neighbours = [(x-1, y), (x, y-1), (x+1, y), (x, y+1), (x-1, y-1), (x+1, y-1), (x+1, y+1), (x-1, y+1)]
    for point in neighbours:
        if point[0] >= 0 and point[1] >= 0 and point[0] < len(lines) and point[1] < len(lines[x]) and lines[point[0]][point[1]] == OCCUPIED:
                sum += 1
            
    return sum

def getNumberOfSeen(x, y) -> int:
    sum = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue

            indexX, indexY = x + i, y + j
            while indexX >= 0 and indexY >= 0 and indexX < len(lines) and indexY < len(lines[x]):
                if lines[indexX][indexY] == EMPTY:
                    break

                if lines[indexX][indexY] == OCCUPIED:
                    sum += 1
                    break

                indexX += i
                indexY += j
    return sum

file = open("day11_input.txt", "r")
lines = file.read().splitlines()
copy = list(lines)

FLOOR, EMPTY, OCCUPIED = '.', 'L', '#'
nextMap = list(lines)

numberOfOccupied = prevOccupied = 0

while True:
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            neighbours = getNumberOfAdjacent(i, j)
            if lines[i][j] != FLOOR:
                if neighbours == 0 and lines[i][j] != OCCUPIED:
                    nextMap[i] = nextMap[i][:j] + OCCUPIED + nextMap[i][j+1:]
                    numberOfOccupied += 1
                elif neighbours >= 4 and lines[i][j] != EMPTY:
                    nextMap[i] = nextMap[i][:j] + EMPTY + nextMap[i][j+1:]
                    numberOfOccupied -= 1
    if numberOfOccupied == prevOccupied:
        break
    prevOccupied = numberOfOccupied
    lines = list(nextMap)

print(numberOfOccupied)

lines = list(copy)
nextMap = list(lines)
numberOfOccupied = prevOccupied = 0

while True:
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            neighbours = getNumberOfSeen(i, j)
            if lines[i][j] != FLOOR:
                if neighbours == 0 and lines[i][j] != OCCUPIED:
                    nextMap[i] = nextMap[i][:j] + OCCUPIED + nextMap[i][j+1:]
                    numberOfOccupied += 1

                elif neighbours >= 5 and lines[i][j] != EMPTY:
                    nextMap[i] = nextMap[i][:j] + EMPTY + nextMap[i][j+1:]
                    numberOfOccupied -= 1
    if numberOfOccupied == prevOccupied:
        break
    prevOccupied = numberOfOccupied
    lines = list(nextMap)
    
print(numberOfOccupied)
