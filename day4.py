import string

def isValid(line):
    arg, op = line[:3], line[4:]
    if arg == 'byr':
        return len(op) == 4 and op.isdigit() and int(op) >= 1920 and int(op) <= 2002
    elif arg == 'iyr':
        return len(op) == 4 and op.isdigit() and int(op) >= 2010 and int(op) <= 2020
    elif arg == 'eyr':
        return len(op) == 4 and op.isdigit() and int(op) >= 2020 and int(op) <= 2030
    elif arg == 'hgt':
        return (op[len(op)-2:] == 'cm' and (int(op[:len(op)-2]) >= 150 and int(op[:len(op)-2]) <= 193)) or (op[len(op)-2:] == 'in' and (int(op[:len(op)-2]) >= 59 and int(op[:len(op)-2]) <= 76))
    elif arg == 'hcl':
        return op[0] == '#' and len(op[1:]) == 6 and all(c in string.hexdigits for c in op[1:]) == True
    elif arg == 'ecl':
        return op in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
    elif arg == 'pid':
        return len(op) == 9 and op.isnumeric()

def checkArgs(args):
    argCounter = 0
    for arg in args:
        if arg[:3] in {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}:
            argCounter += 1

    if argCounter >= 7:
        return True
    else:
        return False

def checkValidity(args):
    for arg in args:
        if isValid(arg) == False:
            return False
    
    return True

file = open("day4_input.txt", "r")
lines = file.read().split('\n\n')

counterPartOne, counterPartTwo = 0, 0
for line in lines:
    line = line.replace('\n', ' ').split(' ')
    
    if checkArgs(line) == True:
        counterPartOne += 1
    if checkArgs(line) == True and checkValidity(line) == True:
        counterPartTwo += 1

print(counterPartOne)
print(counterPartTwo)