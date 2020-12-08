class Machine:
    def __init__(self, code):
        self.name = code
        self.index = self.acc = 0

    def run(self) -> tuple:
        visitedIndexes = list()

        while self.index < len(code):
            if self.index in visitedIndexes:
                return -1, self.acc

            visitedIndexes.append(self.index)
            line = code[self.index]

            if line[0] == "acc":
                self.acc += int(line[1])
            
            if line[0] == "jmp":
                self.index += int(line[1])
            else:
                self.index += 1

        return self.index, self.acc

def swapInstruction(instr):
    if instr == "jmp":
        return "nop"
    elif instr == "nop":
        return "jmp"
    else:
        return "acc"
    
def tryToRepair(code):
    index = acc = -1
    for i in range(len(code)):
        code[i][0] = swapInstruction(code[i][0])
        machine = Machine(code)
        index, acc = machine.run()
        code[i][0] = swapInstruction(code[i][0])

        if index != -1:
            return acc


file = open("day8_input.txt", "r")
code = file.read().splitlines()

for i in range(len(code)):
    code[i] = code[i].split(" ")

machine = Machine(code)
print(machine.run()[1])
print(tryToRepair(code))