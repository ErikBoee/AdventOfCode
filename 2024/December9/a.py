file = open("input.txt", "r")
lines = file.readlines()
file.close()

line = list(lines[0])

def expandLine(line):
    expandedLine = []
    for i in range(len(line)):
        number = line[i]
        for j in range(int(number)):
            id = i//2
            if i%2 == 0:
                expandedLine.append(str(id))
            else: 
                expandedLine.append(".")
    return expandedLine

def reverseLine(line):
    lineReverse = line.copy()
    lineReverse.reverse()
    return lineReverse

def indexFromReverse(index, expandedLine):
    return len(expandedLine) - index - 1


def moveFiles(expandedLine):
    lineReverse = reverseLine(expandedLine)
    reverseIndex = 0
    for char in lineReverse:
        if char == ".":
            reverseIndex += 1
            continue
        firstDot = expandedLine.index(".")
        indexFromReverseValue = indexFromReverse(reverseIndex, expandedLine)
        if firstDot > indexFromReverseValue:
            break
        expandedLine[firstDot] = char
        expandedLine[indexFromReverseValue] = "."
        reverseIndex += 1
    return expandedLine


expandedLine = expandLine(line)
newFileStorage = moveFiles(expandedLine)

score = 0
for i in range(len(newFileStorage)):
    if newFileStorage[i] == ".":
        break
    score += i*int(newFileStorage[i])
print(score)

