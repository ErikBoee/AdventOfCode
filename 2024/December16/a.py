file = open("input.txt", "r")
lines = file.readlines()
file.close()

map = []

startingPos = [0, 0]
endingPos = [0, 0]

for y in range(len(lines)):
    line = lines[y]
    for x in range(len(line)):
        char = line[x]
        if char == "S":
            startingPos = [x, y]
        if char == "E":
            endingPos = [x, y]
    map.append(list(line.strip()))


def minimalTurns(x, y, direction):
    if direction == "N":
        if endingPos[1] <= y:
            if endingPos[0] == x:
                return 0
            return 1
        else:
            return 2
    if direction == "S":
        if endingPos[1] >= y:
            if endingPos[0] == x:
                return 0
            return 1
        else:
            return 2
    if direction == "W":
        if endingPos[0] <= x:
            if endingPos[1] == y:
                return 0
            return 1
        else:
            return 2
    if direction == "E":
        if endingPos[0] >= x:
            if endingPos[1] == y:
                return 0
            return 1
        else:
            return 2

def minimalPointsToEnd(x, y, direction):
    minimalDistance = abs(x - endingPos[0]) + abs(y - endingPos[1])
    if minimalDistance == 0:
        return 0
    minimalTurnsToEnd = minimalTurns(x, y, direction)
    return minimalDistance + minimalTurnsToEnd*1000


def nodeFromPosition(x, y, direction, points, path):
    pathCopy = path.copy()
    pathCopy.append([x, y, direction])
    return {
        "x": x,
        "y": y,
        "direction": direction,
        "points": points,
        "score": minimalPointsToEnd(x, y, direction) + points,
        "path": pathCopy
    }
    

startNode = nodeFromPosition(startingPos[0], startingPos[1], "E", 0, [])

pointAndDirectionToMinimalScore = {}
def registerNodeIfNewBest(node):
    key = str(node["x"]) + "-" + str(node["y"]) + "-" + node["direction"]
    if key in pointAndDirectionToMinimalScore:
        if pointAndDirectionToMinimalScore[key] > node["score"]:
            pointAndDirectionToMinimalScore[key] = node["score"]
            return True
        return False
    pointAndDirectionToMinimalScore[key] = node["score"]
    return True

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


def checkForNodeInCurrentDirection(node):
    x = node["x"]
    y = node["y"]
    direction = node["direction"]
    points = node["points"]
    path = node["path"]
    newPos = [x, y]
    if direction == "N":
        newPos[1] -= 1
    if direction == "S":
        newPos[1] += 1
    if direction == "W":
        newPos[0] -= 1
    if direction == "E":
        newPos[0] += 1
    if map[newPos[1]][newPos[0]] == "#":
        return None
    return nodeFromPosition(newPos[0], newPos[1], direction, points + 1, path)

def isSameOrOppositeDirection(direction1, direction2):
    if direction1 == direction2:
        return True
    if direction1 == "N" and direction2 == "S":
        return True
    if direction1 == "S" and direction2 == "N":
        return True
    if direction1 == "W" and direction2 == "E":
        return True
    if direction1 == "E" and direction2 == "W":
        return True
    return False

def checkForNodesInOtherDirections(node):
    x = node["x"]
    y = node["y"]
    direction = node["direction"]
    points = node["points"]
    path = node["path"]
    nodes = []
    for testDirection in ["N", "S", "W", "E"]:
        if isSameOrOppositeDirection(testDirection, direction):
            continue
        if testDirection == "N" and map[y - 1][x] != "#":
            nodes.append(nodeFromPosition(x, y, testDirection, points + 1000, path))
        if testDirection == "S" and map[y + 1][x] != "#":
            nodes.append(nodeFromPosition(x, y, testDirection, points + 1000, path))
        if testDirection == "W" and map[y][x - 1] != "#":
            nodes.append(nodeFromPosition(x, y, testDirection, points + 1000, path))
        if testDirection == "E" and map[y][x + 1] != "#":
            nodes.append(nodeFromPosition(x, y, testDirection, points + 1000, path))
    return nodes

def findNextNodes(node):
    testNodes = [checkForNodeInCurrentDirection(node)] + checkForNodesInOtherDirections(node)
    for testNode in testNodes:
        if testNode != None:
            insertNode(testNode)

def drawMapWithPath(path):
    newMap = []
    for line in map:
        newMap.append(list(line))
    for i in range(0, len(path)):
        direction = path[i][2]
        if direction == "N":
            newMap[path[i][1]][path[i][0]] = "^"
        if direction == "S":
            newMap[path[i][1]][path[i][0]] = "v"
        if direction == "W":
            newMap[path[i][1]][path[i][0]] = "<"
        if direction == "E":
            newMap[path[i][1]][path[i][0]] = ">"
    for line in newMap:
        print("".join(line))
    print()

def prettyPrintNodes(nodes):
    for node in nodes:
        print(f"({node['x']}, {node['y']}), {node['direction']}, {node['points']},{node['score']}")
        print(node["path"])
    print()

j= 0
while len(nodes) > 0:
    currentNode = nodes.pop(0)
    if currentNode["score"] > currentBestScore:
        continue
    if currentNode["x"] == endingPos[0] and currentNode["y"] == endingPos[1]:
        currentBestScore = currentNode["score"]
        currentBestPath = currentNode["path"]
        drawMapWithPath(currentBestPath)
        print(currentBestScore)
        continue
    findNextNodes(currentNode)
    #prettyPrintNodes(nodes)
    j += 1

print(currentBestScore)