
file = open("input.txt", "r")
lines = file.readlines()
file.close()

mapOfField = []
mapOfVisited = []
initialPositionGuard = [0, 0, "N"]

for y in range(0, len(lines)):
    line = lines[y]
    line = line.strip()
    mapOfField.append([])
    mapOfVisited.append([])
    for x in range(0, len(line)):
        mapOfField[y].append(line[x])
        mapOfVisited[y].append(line[x])
        if line[x] == "^":
            initialPositionGuard = [x, y, "N"]

maxValueY = len(mapOfField)
maxValueX = len(mapOfField[0])

def isOutOfBounds(x, y):
    return x < 0 or x >= maxValueX or y < 0 or y >= maxValueY

def makeMove(x, y, direction):
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
    
    
def registerVisit(x, y):
    mapOfVisited[y][x] = "X"

guardPosition = initialPositionGuard
it = 0
while not isOutOfBounds(guardPosition[0], guardPosition[1]):
    registerVisit(guardPosition[0], guardPosition[1])
    guardPosition = makeMove(guardPosition[0], guardPosition[1], guardPosition[2])

numberOfVisited = 0
for y in range(0, maxValueY):
    for x in range(0, maxValueX):
        if mapOfVisited[y][x] == "X":
            numberOfVisited += 1

print("numberOfVisited", numberOfVisited)