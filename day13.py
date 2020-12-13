from functools import reduce

def findBus(busses, timestamp):
    bestTime = float('inf')
    result = 0
    for bus in busses:
        if bus == 'x':
            continue
        times = timestamp // bus
        timeOfBus = bus*times + bus
        if timeOfBus < bestTime:
            bestTime = timeOfBus
            result = (timeOfBus - timestamp) * bus
    
    return result

def findTimestamp(busses):
    busIDs, busTimes = [], []
    for i, time in enumerate(busses):
        if time != 'x':
            busIDs.append(time)
            busTimes.append(time - i)
    return chinese_remainder(busIDs, busTimes)

def chinese_remainder(n, a): #stolen from rosettacode
    sum = 0
    prod = reduce(lambda a, b: a*b, n)

    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p

    return sum % prod
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

file = open("day13_input.txt", "r")
lines = file.read().splitlines()
timestamp = int(lines[0])
busses = lines[1].split(",")
for i in range(len(busses)):
    if busses[i] != 'x':
       busses[i] = int(busses[i])

print(findBus(busses, timestamp))
print(findTimestamp(busses))