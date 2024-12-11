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
        newPosTop = [pos1[0] + diffX, pos1[1] + diffY]
        newPosBottom = [pos2[0] - diffX, pos2[1] - diffY]
        return [newPosTop, newPosBottom]
    if pos1[0] >= pos2[0] and pos1[1] < pos2[1]:
        diffX = pos1[0] - pos2[0]
        diffY = pos2[1] - pos1[1]
        newPosTop = [pos1[0] + diffX, pos1[1] - diffY]
        newPosBottom = [pos2[0] - diffX, pos2[1] + diffY]
        return [newPosTop, newPosBottom]
    if pos1[0] < pos2[0] and pos1[1] >= pos2[1]:
        diffX = pos2[0] - pos1[0]
        diffY = pos1[1] - pos2[1]
        newPosTop = [pos1[0] - diffX, pos1[1] + diffY]
        newPosBottom = [pos2[0] + diffX, pos2[1] - diffY]
        return [newPosTop, newPosBottom]
    diffX = pos2[0] - pos1[0]
    diffY = pos2[1] - pos1[1]
    newPosTop = [pos1[0] - diffX, pos1[1] - diffY]
    newPosBottom = [pos2[0] + diffX, pos2[1] + diffY]
    return [newPosTop, newPosBottom]
    

mapWithNewPositions = map.copy()
uniqueNewPositions = {}
numberOfNewPositions = 0
for symbol in groupOfPairs:
    pairs = groupOfPairs[symbol]
    for i in range(len(pairs)):
        currentPair = pairs[i]
        for j in range(i + 1, len(pairs)):
            nextPair = pairs[j]
            newPositions = findNewPositions(currentPair, nextPair)
            if isInBounds(newPositions[0][0], newPositions[0][1]):
                mapWithNewPositions[newPositions[0][1]][newPositions[0][0]] = "#"
                if str(newPositions[0]) not in uniqueNewPositions:
                    numberOfNewPositions += 1
                uniqueNewPositions[str(newPositions[0])] = True
            if isInBounds(newPositions[1][0], newPositions[1][1]):
                mapWithNewPositions[newPositions[1][1]][newPositions[1][0]] = "#"
                if str(newPositions[1]) not in uniqueNewPositions:
                    numberOfNewPositions += 1
                uniqueNewPositions[str(newPositions[1])] = True

print(numberOfNewPositions)


