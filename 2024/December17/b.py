file = open("input.txt", "r")
lines = file.readlines()
file.close()

requiredBvalues = lines[4].split("Program: ")[1].split(",")
requiredBvalues.reverse()

def bFromAin(a):
    tmp = (a%8)^6
    return tmp^(a//(2**tmp))^7

def aFromAin(a):
    return a//8

def findMinAvalue(requiredAValue, requiredBvalues):
    if len(requiredBvalues) == 0:
        return requiredAValue
    requiredBvalue = int(requiredBvalues[0])
    approvedAValuesToTest = range(requiredAValue*8, requiredAValue*8 + 8)
    candidates = []
    for a in approvedAValuesToTest:
        if bFromAin(a)%8 == requiredBvalue:
            candidates.append(a)
    if len(candidates) == 0:
        return -1
    minAValues = []
    for candidate in candidates:
        value = findMinAvalue(candidate, requiredBvalues[1:])
        if value != -1:
            minAValues.append(value)
    if len(minAValues) == 0:
        return -1
    return min(minAValues)

minAValue = findMinAvalue(0, requiredBvalues)
minBValue=0
print(minAValue)
        

            
