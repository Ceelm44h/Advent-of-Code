r = open("day1_input.txt", "r")
numbers = [int(line) for line in r.read().splitlines()]

def findTwo():
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if numbers[i] + numbers[j] + numbers[k] == 2020:
                return numbers[i] * numbers[j] * numbers[k]

def findThree():
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            for k in range(len(numbers)):
                if numbers[i] + numbers[j] + numbers[k] == 2020:
                    return numbers[i] * numbers[j] * numbers[k]

print(findThree())