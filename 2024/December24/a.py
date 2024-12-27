file = open("input.txt", "r")
lines = file.readlines()
file.close()


wireToValue = {}
operations = []
for line in lines:
    line = line.strip()
    if len(line) == 0:
        continue
    if ":" in line:
        wire, value = line.split(": ")
        wireToValue[wire] = int(value)
    else:
        operationInputs = line.split(" -> ")[0].split(" ")
        operationOutput = line.split(" -> ")[1]
        operation = {
            "input1": operationInputs[0],
            "operation": operationInputs[1],
            "input2": operationInputs[2],
            "output": operationOutput
        }
        operations.append(operation)

def doOperation(input1, input2, operation):
    if operation == "AND":
        return int(input1 and input2)
    elif operation == "OR":
        return int(input1 or input2)
    elif operation == "XOR":
        return int(input1 != input2)
    raise Exception("Invalid operation")


while len(operations) > 0:
    operation = operations.pop(0)
    if operation["input1"] in wireToValue and operation["input2"] in wireToValue:
        wireToValue[operation["output"]] = doOperation(wireToValue[operation["input1"]], wireToValue[operation["input2"]], operation["operation"])
    else:
        operations.append(operation)

wireValuesStartingWithZ = [wire for wire in wireToValue.keys() if wire.startswith("z")]
wireValuesStartingWithZ.sort()
wireValuesStartingWithZ.reverse()

binaryNumber = ""
for wire in wireValuesStartingWithZ:
    print(wire, wireToValue[wire])
    binaryNumber += str(wireToValue[wire])

print(binaryNumber)
print(int(binaryNumber, 2))