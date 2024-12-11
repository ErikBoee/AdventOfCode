
file = open("input.txt", "r")
lines = file.readlines()
file.close()

mapOfField = []
mapOfVisited = []
guardPosition = [0, 0, "N"]

for y in range(0, len(lines)):
    line = lines[y]
    line = line.strip()
    mapOfField.append([])
    mapOfVisited.append([])
    for x in range(0, len(line)):
        mapOfField[y].append(line[x])
        mapOfVisited[y].append(line[x])
        if line[x] == "^":
            guardPosition = [x, y, "N"]

maxValueY = len(mapOfField)
maxValueX = len(mapOfField[0])

def isOutOfBounds(x, y):
    return x < 0 or x >= maxValueX or y < 0 or y >= maxValueY

def makeMove(x, y, direction, mapOfField):
    if direction == "N":
        if not isOutOfBounds(x, y - 1) and mapOfField[y - 1][x] == "#":
            return [x, y, "E"]
        return [x, y - 1, "N"]
    if direction == "E":
        if not isOutOfBounds(x + 1, y) and mapOfField[y][x + 1] == "#":
            return [x, y, "S"]
        return [x + 1, y, "E"]
    if direction == "S":
        if not isOutOfBounds(x, y + 1) and mapOfField[y + 1][x] == "#":
            return [x, y, "W"]
        return [x, y + 1, "S"]
    if direction == "W":
        if not isOutOfBounds(x-1, y) and mapOfField[y][x - 1] == "#":
            return [x, y, "N"]
        return [x - 1, y, "W"]

def positionWithDirectionKey(x, y, direction):
    return "-".join([str(x), str(y), direction])

def isInfiniteLoop(guardPosition, mapOfField):
    registeredPosition = { positionWithDirectionKey(guardPosition[0], guardPosition[1], guardPosition[2]): True }
    while not isOutOfBounds(guardPosition[0], guardPosition[1]):
        guardPosition = makeMove(guardPosition[0], guardPosition[1], guardPosition[2], mapOfField)
        key = positionWithDirectionKey(guardPosition[0], guardPosition[1], guardPosition[2])
        if key in registeredPosition:
            return True
        registeredPosition[key] = True
    return False

def positionsAreDifferent(position1, position2):
    return position1[0] != position2[0] or position1[1] != position2[1]

def positionTestedForInfinityKey(x, y):
    return "-".join([str(x), str(y)])

numberOfInfiniteLoops = 0
testedPositions = {}

i = 0
while not isOutOfBounds(guardPosition[0], guardPosition[1]):
    nextPosition = makeMove(guardPosition[0], guardPosition[1], guardPosition[2], mapOfField)
    if positionsAreDifferent(guardPosition, nextPosition) and not isOutOfBounds(nextPosition[0], nextPosition[1]) and not positionTestedForInfinityKey(nextPosition[0], nextPosition[1]) in testedPositions:
        mapOfField[nextPosition[1]][nextPosition[0]] = "#"
        isInfinite = isInfiniteLoop(guardPosition, mapOfField)
        if isInfinite:
            numberOfInfiniteLoops += 1
        mapOfField[nextPosition[1]][nextPosition[0]] = "."
        testedPositions[positionTestedForInfinityKey(nextPosition[0], nextPosition[1])] = True

    guardPosition = makeMove(guardPosition[0], guardPosition[1], guardPosition[2], mapOfField)

    i += 1
    if i % 100 == 0:
        print(f"Found {numberOfInfiniteLoops} of {i} infinite loops")

print(f"Found {numberOfInfiniteLoops} of {i} infinite loops")
