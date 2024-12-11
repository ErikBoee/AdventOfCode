file = open("input.txt", "r")
lines = file.readlines()
file.close()

map = []
for line in lines:
    map.append(list(line.strip()))

def prettyPrint(map):
    for line in map:
        print("".join(line))
    print()


groupOfPairs = {}

for y in range(len(map)):
    line = map[y]
    for x in range(len(line)):
        if line[x] != ".":
            if line[x] in groupOfPairs:
                groupOfPairs[line[x]].append([x, y])
            else:
                groupOfPairs[line[x]] = [[x, y]]

def isInBounds(x, y):
    return x >= 0 and x < len(map[0]) and y >= 0 and y < len(map)

def findNewPositions(pos1, pos2):
    if pos1[0] >= pos2[0] and pos1[1] >= pos2[1]:
        diffX = pos1[0] - pos2[0]
        diffY = pos1[1] - pos2[1]

        newpositions = []
        newXTop = pos1[0] + diffX
        newYTop = pos1[1] + diffY
        while isInBounds(newXTop, newYTop):
            newpositions.append([newXTop, newYTop])
            newXTop += diffX
            newYTop += diffY
            
        newXBottom = pos2[0] - diffX
        newYBottom = pos2[1] - diffY
        while isInBounds(newXBottom, newYBottom):
            newpositions.append([newXBottom, newYBottom])
            newXBottom -= diffX
            newYBottom -= diffY
        return newpositions
    if pos1[0] >= pos2[0] and pos1[1] < pos2[1]:
        diffX = pos1[0] - pos2[0]
        diffY = pos2[1] - pos1[1]

        newpositions = []
        newXTop = pos1[0] + diffX
        newYTop = pos1[1] - diffY
        while isInBounds(newXTop, newYTop):
            newpositions.append([newXTop, newYTop])
            newXTop += diffX
            newYTop -= diffY
            
        newXBottom = pos2[0] - diffX
        newYBottom = pos2[1] + diffY
        while isInBounds(newXBottom, newYBottom):
            newpositions.append([newXBottom, newYBottom])
            newXBottom -= diffX
            newYBottom += diffY
        return newpositions
    if pos1[0] < pos2[0] and pos1[1] >= pos2[1]:
        diffX = pos2[0] - pos1[0]
        diffY = pos1[1] - pos2[1]

        newpositions = []
        newXTop = pos1[0] - diffX
        newYTop = pos1[1] + diffY
        while isInBounds(newXTop, newYTop):
            newpositions.append([newXTop, newYTop])
            newXTop -= diffX
            newYTop += diffY
            
        newXBottom = pos2[0] + diffX
        newYBottom = pos2[1] - diffY
        while isInBounds(newXBottom, newYBottom):
            newpositions.append([newXBottom, newYBottom])
            newXBottom += diffX
            newYBottom -= diffY
        return newpositions
    diffX = pos2[0] - pos1[0]
    diffY = pos2[1] - pos1[1]

    newpositions = []
    newXTop = pos1[0] - diffX
    newYTop = pos1[1] - diffY
    while isInBounds(newXTop, newYTop):
        newpositions.append([newXTop, newYTop])
        newXTop -= diffX
        newYTop -= diffY

    newXBottom = pos2[0] + diffX
    newYBottom = pos2[1] + diffY
    while isInBounds(newXBottom, newYBottom):
        newpositions.append([newXBottom, newYBottom])
        newXBottom += diffX
        newYBottom += diffY
    return newpositions

    

mapWithNewPositions = map.copy()
uniqueNewPositions = {}
numberOfNewPositions = 0
for symbol in groupOfPairs:
    pairs = groupOfPairs[symbol]
    for i in range(len(pairs)):
        currentPair = pairs[i]
        if str(currentPair) not in uniqueNewPositions:
            numberOfNewPositions += 1
        uniqueNewPositions[str(currentPair)] = True
        for j in range(i + 1, len(pairs)):
            nextPair = pairs[j]
            if str(nextPair) not in uniqueNewPositions:
                numberOfNewPositions += 1
            uniqueNewPositions[str(nextPair)] = True
            newPositions = findNewPositions(currentPair, nextPair)
            for newPos in newPositions:
                if isInBounds(newPos[0], newPos[1]):
                    mapWithNewPositions[newPos[1]][newPos[0]] = "#"
                    if str(newPos) not in uniqueNewPositions:
                        numberOfNewPositions += 1
                    uniqueNewPositions[str(newPos)] = True

print(numberOfNewPositions)
prettyPrint(mapWithNewPositions)

