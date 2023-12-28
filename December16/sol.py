
file = open("input.txt", "r")
lines = file.readlines()
file.close()

tiles = []
for line in lines:
    lineList = list(line.strip())
    tiles.append(lineList)


def posInBounds(pos):
    return pos[0] >= 0 and pos[0] < len(tiles) and pos[1] >= 0 and pos[1] < len(tiles[0])

def followBeam(pos, dir, energizedTiles, visitedTilesAndDirections):
    while posInBounds(pos):
        energizedTiles[pos[0]][pos[1]] = "#"
        tile = tiles[pos[0]][pos[1]]
        key = str(pos[0]) + "," + str(pos[1]) + "-" + dir
        if key in visitedTilesAndDirections:
            return
        visitedTilesAndDirections[key] = True
        if dir == "right":
            if tile == "." or tile == "-":
                pos = [pos[0], pos[1] + 1]
                dir = "right"

            elif tile == "/":
                pos = [pos[0] - 1, pos[1]]
                dir = "up"
            elif tile == "\\":
                pos = [pos[0] + 1, pos[1]]
                dir = "down"
            elif tile == "|":
                pos = [pos[0] + 1, pos[1]]
                dir = "down"
                followBeam([pos[0] - 1, pos[1]], "up", energizedTiles, visitedTilesAndDirections)
        elif dir == "left":
            if tile == "." or tile == "-":
                pos = [pos[0], pos[1] - 1]
                dir = "left"
            elif tile == "/":
                pos = [pos[0] + 1, pos[1]]
                dir = "down"
            elif tile == "\\":
                pos = [pos[0] - 1, pos[1]]
                dir = "up"
            elif tile == "|":
                pos = [pos[0] + 1, pos[1]]
                dir = "down"
                followBeam([pos[0] - 1, pos[1]], "up", energizedTiles, visitedTilesAndDirections)
        elif dir == "up":
            if tile == "." or tile == "|":
                pos = [pos[0] - 1, pos[1]]
                dir = "up"
            elif tile == "/":
                pos = [pos[0], pos[1] + 1]
                dir = "right"
            elif tile == "\\":
                pos = [pos[0], pos[1] - 1]
                dir = "left"
            elif tile == "-":
                pos = [pos[0], pos[1] + 1]
                dir = "right"
                followBeam([pos[0], pos[1] - 1], "left", energizedTiles, visitedTilesAndDirections)
        elif dir == "down":
            if tile == "." or tile == "|":
                pos = [pos[0] + 1, pos[1]]
                dir = "down"
            elif tile == "/":
                pos = [pos[0], pos[1] - 1]
                dir = "left"
            elif tile == "\\":
                pos = [pos[0], pos[1] + 1]
                dir = "right"
            elif tile == "-":
                pos = [pos[0], pos[1] + 1]
                dir = "right"
                followBeam([pos[0], pos[1] - 1], "left", energizedTiles, visitedTilesAndDirections)


def findEnergy(initialPos, dir):
    energizedTiles = []
    visitedTilesAndDirections = {}
    for i in range(len(tiles)):
        energizedTiles.append([])
        for j in range(len(tiles[i])):
            energizedTiles[i].append(".")
    followBeam(initialPos, dir, energizedTiles, visitedTilesAndDirections)

    count = 0
    for i in range(len(energizedTiles)):
        for j in range(len(energizedTiles[i])):
            if energizedTiles[i][j] == "#":
                count += 1

    return count

maxCount = 0
for i in range(len(tiles)):
    energyRight = findEnergy([i, 0], "right")
    if energyRight > maxCount:
        maxCount = energyRight
    energyLeft = findEnergy([i, len(tiles[0]) - 1], "left")
    if energyLeft > maxCount:
        maxCount = energyLeft

for i in range(len(tiles[0])):
    energyDown = findEnergy([0, i], "down")
    if energyDown > maxCount:
        maxCount = energyDown
    energyUp = findEnergy([len(tiles) - 1, i], "up")
    if energyUp > maxCount:
        maxCount = energyUp

print(maxCount)