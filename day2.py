def formatInput(policy):
    policy = policy.replace(': ', ' ').replace('-', ':')
    return policy.replace(' ', ':').split(':')

def isValidOne(policy):
    policy, counter = formatInput(policy), 0
    for ch in policy[3]:
        if ch == policy[2]:
            counter += 1
        
        if counter > int(policy[1]):
            return False
    
    if counter < int(policy[0]):
        return False
    else:
        return True

def isValidTwo(policy):
    policy = formatInput(policy)
    minPos, maxPos = int(policy[0])-1, int(policy[1])-1

    if (policy[3][minPos] == policy[2] and policy[3][maxPos] != policy[2]) or (policy[3][minPos] != policy[2] and policy[3][maxPos] == policy[2]): #xor
        return True
    else:
        return False

file = open("day2_input.txt", "r")
lines = file.read().splitlines()

lineCounterFirst = lineCounterSecond = 0
for line in lines:
    if isValidOne(line):
        lineCounterFirst += 1
    if isValidTwo(line):
        lineCounterSecond += 1

print(lineCounterFirst)
print(lineCounterSecond)