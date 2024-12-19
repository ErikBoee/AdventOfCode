file = open("input.txt", "r")
lines = file.readlines()
file.close()



aRegister = 0
bRegister = 0
cRegister = 0
instructionPointer = 0
instructions = []

output = ""
for line in lines:
    if line.startswith("Register A:"):
        aRegister = int(line.split(": ")[1])
    elif line.startswith("Register B:"):
        bRegister = int(line.split(": ")[1])
    elif line.startswith("Register C:"):
        cRegister = int(line.split(": ")[1])
    elif line.startswith("Program:"):
        instructions = line.split(": ")[1].split(",")


def comboOperatorValue(operand):
    operand = int(operand)
    if operand < 4:
        return operand
    elif operand == 4:
        return aRegister
    elif operand == 5:
        return bRegister
    elif operand == 6:
        return cRegister
    raise

def diviseAndWriteToA(operand):
    denominator = 2**comboOperatorValue(operand)
    global aRegister
    aRegister = aRegister // denominator

def bitwiseXorAndWriteToB(operand):
    global bRegister
    bRegister = bRegister ^ int(operand)

def moduloEigthAndWriteToB(operand):
    global bRegister
    bRegister = comboOperatorValue(operand)%8

def moveInstructionPointerIfANotZero(operand):
    global aRegister
    global instructionPointer
    if aRegister != 0:
        instructionPointer = int(operand)
    else:
        instructionPointer += 2

def bitwiseBorCToB():
    global bRegister
    bRegister = bRegister ^ cRegister

def printComboOperatorValue(operand):
    global output
    if output != "":
        output += ","
    output += str(comboOperatorValue(operand)%8)

def diviseAndWriteToB(operand):
    global aRegister
    numerator = aRegister
    denominator = (2**comboOperatorValue(operand))
    global bRegister
    bRegister = numerator // denominator

def diviseAndWriteToC(operand):
    global aRegister
    numerator = aRegister
    denominator = 2**comboOperatorValue(operand)
    global cRegister
    cRegister = numerator // denominator

def readInstructions(opCode, operand):
    global instructionPointer
    if opCode == "0":
        diviseAndWriteToA(operand)
        instructionPointer += 2
    elif opCode == "1":
        bitwiseXorAndWriteToB(operand)
        instructionPointer += 2
    elif opCode == "2":
        moduloEigthAndWriteToB(operand)
        instructionPointer += 2
    elif opCode == "3":
        moveInstructionPointerIfANotZero(operand)
    elif opCode == "4":
        bitwiseBorCToB()
        instructionPointer += 2
    elif opCode == "5":
        printComboOperatorValue(operand)
        instructionPointer += 2
    elif opCode == "6":
        diviseAndWriteToB(operand)
        instructionPointer += 2
    elif opCode == "7":
        diviseAndWriteToC(operand)
        instructionPointer += 2
    else:
        raise

while instructionPointer < len(instructions):
    opCode = instructions[instructionPointer]
    operand = instructions[instructionPointer + 1]
    readInstructions(opCode, operand)
print(output)