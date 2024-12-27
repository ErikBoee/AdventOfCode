file = open("input.txt", "r")
lines = file.readlines()
file.close()


wireToValue = {}
operations = []
operationInputToOutput = {}
for line in lines:
    line = line.strip()
    if len(line) == 0:
        continue
    if ":" in line:
        wire, value = line.split(": ")
        wireToValue[wire] = int(value)
    else:
        operationInputs = line.split(" -> ")[0]
        operationOutput = line.split(" -> ")[1]
        operationInputToOutput[line.split(" -> ")[0]] = operationOutput

def valuesAndOperatorToOutput(xValue, yValue, operator):
    if f"{xValue} {operator} {yValue}" in operationInputToOutput:
        return operationInputToOutput[f"{xValue} {operator} {yValue}"]
    if f"{yValue} {operator} {xValue}" in operationInputToOutput:
        return operationInputToOutput[f"{yValue} {operator} {xValue}"]
    return None

switchedOutputs= []
def switchOutputs(val1, val2):
    switchedOutputs.append(val1)
    switchedOutputs.append(val2)
    keyForVal1 = None
    keyForVal2 = None
    for key in operationInputToOutput.keys():
        if operationInputToOutput[key] == val1:
            keyForVal1 = key
        elif operationInputToOutput[key] == val2:
            keyForVal2 = key
    operationInputToOutput[keyForVal1] = val2
    operationInputToOutput[keyForVal2] = val1

def findZValueKey(zValue):
    for key in operationInputToOutput.keys():
        if operationInputToOutput[key] == zValue:
            return key
    return None

def findOutputsToSwitchFromZValueKey(zValueKey, orOutputCurrent, bitWiseXORCurrent):
    firstOutPutInZValueKey = zValueKey.split(" ")[0]
    secondOutPutInZValueKey = zValueKey.split(" ")[2]
    otherKey = None
    if [firstOutPutInZValueKey, secondOutPutInZValueKey].count(orOutputCurrent) == 1:
        otherKey = firstOutPutInZValueKey if orOutputCurrent == secondOutPutInZValueKey else secondOutPutInZValueKey
        return otherKey, bitWiseXORCurrent
    else:
        otherKey = firstOutPutInZValueKey if bitWiseXORCurrent == secondOutPutInZValueKey else secondOutPutInZValueKey
    return otherKey, bitWiseXORCurrent


zeroValue = valuesAndOperatorToOutput("x00", "y00", "XOR")
if zeroValue != "z00":
    switchOutputs(zeroValue, "z00")

andOutputFormer = valuesAndOperatorToOutput("x00", "y00", "AND")

bitWiseXORCurrent = valuesAndOperatorToOutput("x01", "y01", "XOR")
advancedXORCurrentOutput = valuesAndOperatorToOutput(bitWiseXORCurrent, andOutputFormer, "XOR")
if not (advancedXORCurrentOutput == "z01"):
        switchOutputs(advancedXORCurrentOutput, "z01")
        bitWiseXORCurrent = valuesAndOperatorToOutput("x01", "y01", "XOR")
        advancedXORCurrentOutput = valuesAndOperatorToOutput(bitWiseXORCurrent, andOutputFormer, "XOR")

advancedAndOutputFormer = valuesAndOperatorToOutput(bitWiseXORCurrent, andOutputFormer, "AND")
andOutputFormer = valuesAndOperatorToOutput("x01", "y01", "AND")

for i in range(2, 45):
    xValue = f"x{i < 10 and '0' or ''}{i}"
    yValue = f"y{i < 10 and '0' or ''}{i}"
    zValue = f"z{i < 10 and '0' or ''}{i}"

    bitWiseXORCurrent = valuesAndOperatorToOutput(xValue, yValue, "XOR")
    orOutputCurrent = valuesAndOperatorToOutput(andOutputFormer, advancedAndOutputFormer, "OR")
    advancedXORCurrentOutput = valuesAndOperatorToOutput(bitWiseXORCurrent, orOutputCurrent, "XOR")

    if advancedXORCurrentOutput == None:
        zValueKey = findZValueKey(zValue)
        outPutsToSwitch = findOutputsToSwitchFromZValueKey(zValueKey, orOutputCurrent, bitWiseXORCurrent)
        switchOutputs(outPutsToSwitch[0], outPutsToSwitch[1])
        bitWiseXORCurrent = valuesAndOperatorToOutput(xValue, yValue, "XOR")
        orOutputCurrent = valuesAndOperatorToOutput(andOutputFormer, advancedAndOutputFormer, "OR")
        advancedXORCurrentOutput = valuesAndOperatorToOutput(bitWiseXORCurrent, orOutputCurrent, "XOR")
    
    elif not (advancedXORCurrentOutput == zValue):
        switchOutputs(advancedXORCurrentOutput, zValue)
        bitWiseXORCurrent = valuesAndOperatorToOutput(xValue, yValue, "XOR")
        orOutputCurrent = valuesAndOperatorToOutput(andOutputFormer, advancedAndOutputFormer, "OR")
        advancedXORCurrentOutput = valuesAndOperatorToOutput(bitWiseXORCurrent, orOutputCurrent, "XOR")
    
    advancedAndOutputFormer = valuesAndOperatorToOutput(bitWiseXORCurrent, orOutputCurrent, "AND")
    andOutputFormer = valuesAndOperatorToOutput(xValue, yValue, "AND")
            
switchedOutputs.sort()
print(",".join(switchedOutputs))