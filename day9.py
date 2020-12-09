def findSumOfTwo(lines, right, preamble):
    number = lines[right]

    for i in range(1, preamble + 1):
        for j in range(1, i):
            if int(lines[right - i]) + int(lines[right - j]) == int(number):
                return True
    return False

def findComponents(lines, number):
    for i in range(len(lines)):
        smallest = int(number) + 1
        largest = -1
        sum = j = 0
        while sum < int(number):
            sum += int(lines[i+j])

            if int(lines[i+j]) < smallest:
                smallest = int(lines[i+j])
            elif int(lines[i+j]) > largest:
                largest = int(lines[i+j])
            j += 1
        
        if sum == int(number):
            return smallest + largest

    return None

file = open("day9_input.txt", "r")
lines = file.read().splitlines()

PREAMBLE = 25
wrongNumber = None

for i in range(PREAMBLE, len(lines)):
    if findSumOfTwo(lines, i, PREAMBLE) == False:
        wrongNumber = lines[i]
        break

print(wrongNumber)
print(findComponents(lines, wrongNumber))
   