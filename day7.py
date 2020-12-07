def countContaining(entries, visited, name):
    counter = 0
    for entry in entries:
        if name in entry[1] and entry[0] not in visited:
            visited.append(entry[0])
            counter += 1 + countContaining(entries, visited, entry[0])

    return counter

def countInside(entries, values, name):
    counter = 1

    for lineIndex in range(len(entries)):
        entry = entries[lineIndex]
        if name in entry[0]:
            for bagIndex in range(len(entry[1])):
                if values[lineIndex][bagIndex] == 'n':
                    return 1
                counter += countInside(entries, values, entry[1][bagIndex]) * int(values[lineIndex][bagIndex])


    return counter

file = open("day7_input.txt", "r")
lines = file.read().splitlines()
values = list()

for i in range(len(lines)): #parse
    line = lines[i]
    lines[i] = line.replace(" bags.", "").replace(" bag.", "").replace("bag,", "bags,").split(" bags contain ")
    lines[i][1] = lines[i][1].split(" bags, ")
    values.append([ent[:1] for ent in lines[i][1]])
    lines[i][1] = [ent[2:] for ent in lines[i][1]]

print(countContaining(lines, list(), 'shiny gold'))
print(countInside(lines, values, 'shiny gold') - 1)