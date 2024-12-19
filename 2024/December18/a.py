file = open("input.txt", "r")
lines = file.readlines()
file.close()

map = []

maxX = 71
maxY = 71
startingPos = [0, 0]
endingPos = [maxX - 1, maxY - 1]


for y in range(maxY):
    map.append(["."]*maxX)

for line in lines[0:1]:
    blockPos = line.strip().split(",")
    if len(blockPos) == 2:
        x = int(blockPos[0])
        y = int(blockPos[1])
        map[y][x] = "#"

def prettyPrintMap(map):
    for line in map:
        print("".join(line))


def minimalPointsToEnd(x, y):
    return abs(x - maxX + 1) + abs(y - maxY + 1)


def nodeFromPosition(x, y, points, path):
    pathCopy = path.copy()
    pathCopy.append([x, y])
    return {
        "x": x,
        "y": y,
        "points": points,
        "score": minimalPointsToEnd(x, y) + points,
        "path": pathCopy
    }



pointToMinimalScore = {}
def registerNodeIfNewBest(node):
    key = str(node["x"]) + "-" + str(node["y"])
    if key in pointToMinimalScore:
        if pointToMinimalScore[key] > node["score"]:
            pointToMinimalScore[key] = node["score"]
            return True
        return False
    pointToMinimalScore[key] = node["score"]
    return True

startNode = nodeFromPosition(0, 0, 0, [])
registerNodeIfNewBest(startNode)
nodes = [startNode]

currentBestScore = 1e30
currentBestPath = []

def insertNode(node):
    newBest = registerNodeIfNewBest(node)
    if not newBest:
        return
    for i in range(len(nodes)):
        if nodes[i]["score"] > node["score"]:
            nodes.insert(i, node)
            return
    nodes.append(node)

def findNextNodes(node):
    testNodes = []
    newPositions = [[node["x"] + 1, node["y"]], [node["x"] - 1, node["y"]], [node["x"], node["y"] + 1], [node["x"], node["y"] - 1]]
    for newPos in newPositions:
        if newPos[0] >= 0 and newPos[0] < maxX and newPos[1] >= 0 and newPos[1] < maxY:
            if map[newPos[1]][newPos[0]] != "#":
                testNodes.append(nodeFromPosition(newPos[0], newPos[1], node["points"] + 1, node["path"]))
    for testNode in testNodes:
        insertNode(testNode)

def drawMapWithPath(path):
    newMap = []
    for line in map:
        newMap.append(list(line))
    for i in range(0, len(path)):
        newMap[path[i][1]][path[i][0]] = "O"
    for line in newMap:
        print("".join(line))
    print()

def prettyPrintNodes(nodes):
    for node in nodes:
        print(f"({node['x']}, {node['y']}), {node['points']},{node['score']}")
    print()


currentLineNumber = 1
foundAPath = True
while foundAPath:
    pointToMinimalScore = {}
    startNode = nodeFromPosition(0, 0, 0, [])
    registerNodeIfNewBest(startNode)
    nodes = [startNode]
    currentBestScore = 1e30
    currentBestPath = []
    line = lines[currentLineNumber].strip()
    blockPos = line.strip().split(",")
    if len(blockPos) == 2:
        x = int(blockPos[0])
        y = int(blockPos[1])
        map[y][x] = "#"
    
    while len(nodes) > 0:
        currentNode = nodes.pop(0)
        if currentNode["score"] > currentBestScore:
            continue
        if currentNode["x"] == endingPos[0] and currentNode["y"] == endingPos[1]:
            currentBestScore = currentNode["score"]
            currentBestPath = currentNode["path"]
            continue
        findNextNodes(currentNode)
    if currentBestScore == 1e30:
        foundAPath = False
        break
    drawMapWithPath(currentBestPath)
    print(currentLineNumber, currentBestScore, x, y)
    currentLineNumber += 1

print(currentBestScore)