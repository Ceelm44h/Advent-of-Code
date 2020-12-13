def moveShip(lines) -> int:
    shipTurn = 2
    x = y = 0

    directionsX = {"N": 0, "S": 0, "E": 1, "W": -1}
    directionsY = {"N": 1, "S": -1, "E": 0, "W": 0}

    for line in lines:
        op, arg = line[0], int(line[1:])
        if op in "NSEW":
            x += directionsX[op]*arg
            y += directionsY[op]*arg

        elif op == 'L':
            shipTurn = (shipTurn - arg/90)%4
        elif op == 'R':
            shipTurn = (shipTurn + arg/90)%4

        elif shipTurn == 0: #w
            x -= arg
        elif shipTurn == 1: #n
            y += arg
        elif shipTurn == 2: #e
            x += arg
        elif shipTurn == 3: #s
            y -= arg

    return abs(x) + abs(y)

def moveShipWithWaypoint(waypointX, waypointY):
    x = y = 0

    directionsX = {"N": 0, "S": 0, "E": 1, "W": -1}
    directionsY = {"N": 1, "S": -1, "E": 0, "W": 0}

    for line in lines:
        op, arg = line[0], int(line[1:])

        if op in "NSEW":
            waypointX += directionsX[op]*arg
            waypointY += directionsY[op]*arg
        elif op == "L":
            for i in range(int(arg/90)):
                waypointX, waypointY = -waypointY, waypointX
        elif op == "R":
            for i in range(int(arg/90)):
                waypointX, waypointY = waypointY, -waypointX
        elif op == "F":
            x += waypointX * arg
            y += waypointY * arg

    return abs(x) + abs(y)

file = open("day12_input.txt", "r")
lines = file.read().splitlines()

print(moveShip(lines))
print(moveShipWithWaypoint(10, 1))