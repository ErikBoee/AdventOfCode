from a import expandLine, indexFromReverse, reverseLine

file = open("input.txt", "r")
lines = file.readlines()
file.close()

line = list(lines[0])

def indexOfMultipleDots(expandedLine, desiredNumberOfDots):
    numberOfDots = 0
    for i in range(len(expandedLine)):
        if expandedLine[i] == ".":
            numberOfDots += 1
            if numberOfDots == desiredNumberOfDots:
                return i - desiredNumberOfDots + 1
        else:
            numberOfDots = 0
    return -1

def moveFiles(expandedLine):
    lineReverse = reverseLine(expandedLine)
    reverseIndex = 0
    formerChar = "."
    for char in lineReverse:
        indexFromReverseValue = indexFromReverse(reverseIndex, expandedLine) + 1
        reverseIndex += 1
        if char == formerChar:
            numberOfEqualChars += 1
            continue
        if formerChar == ".":
            numberOfEqualChars = 1
            formerChar = char
            continue
        firstDot = indexOfMultipleDots(expandedLine, numberOfEqualChars)
        if firstDot == -1 or firstDot > indexFromReverseValue:
            formerChar = char
            numberOfEqualChars = 1
            continue
        if firstDot > indexFromReverseValue:
            continue
        expandedLine[firstDot:firstDot+numberOfEqualChars] = [formerChar]*numberOfEqualChars
        expandedLine[indexFromReverseValue:indexFromReverseValue+numberOfEqualChars] = ["."]*numberOfEqualChars
        formerChar = char
        numberOfEqualChars = 1
    return expandedLine

expandedLine = expandLine(line)
newFileStorage = moveFiles(expandedLine)

score = 0
for i in range(len(newFileStorage)):
    if newFileStorage[i] == ".":
        continue
    score += i*int(newFileStorage[i])
print(score)

