from a import *

pointAndDirectionToMinimalScore = {}
pointAndDirectionFromPaths= {}


def nodeFromPosition(x, y, direction, points, paths):
    pathCopies = []
    for path in paths:
        pathCopy = path.copy()
        pathCopy.append([x, y, direction])
        pathCopies.append(pathCopy)
    return {
        "x": x,
        "y": y,
        "direction": direction,
        "points": points,
        "score": minimalPointsToEnd(x, y, direction) + points,
        "paths": pathCopies
    }

def checkForNodeInCurrentDirection(node):
    x = node["x"]
    y = node["y"]
    direction = node["direction"]
    points = node["points"]
    paths = node["paths"]
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
    return nodeFromPosition(newPos[0], newPos[1], direction, points + 1, paths)

def checkForNodesInOtherDirections(node):
    x = node["x"]
    y = node["y"]
    direction = node["direction"]
    points = node["points"]
    paths = node["paths"]
    nodes = []
    for testDirection in ["N", "S", "W", "E"]:
        if isSameOrOppositeDirection(testDirection, direction):
            continue
        if testDirection == "N" and map[y - 1][x] != "#":
            nodes.append(nodeFromPosition(x, y, testDirection, points + 1000, paths))
        if testDirection == "S" and map[y + 1][x] != "#":
            nodes.append(nodeFromPosition(x, y, testDirection, points + 1000, paths))
        if testDirection == "W" and map[y][x - 1] != "#":
            nodes.append(nodeFromPosition(x, y, testDirection, points + 1000, paths))
        if testDirection == "E" and map[y][x + 1] != "#":
            nodes.append(nodeFromPosition(x, y, testDirection, points + 1000, paths))
    return nodes

def registerNodeIfNewBest(node):
    key = str(node["x"]) + "-" + str(node["y"]) + "-" + node["direction"]
    if key in pointAndDirectionToMinimalScore:
        if pointAndDirectionToMinimalScore[key] >= node["score"]:
            pointAndDirectionToMinimalScore[key] = node["score"]
            return True
        return False
    pointAndDirectionToMinimalScore[key] = node["score"]
    return True

startNode = nodeFromPosition(startingPos[0], startingPos[1], "E", 0, [[]])

registerNodeIfNewBest(startNode)
nodes = [startNode]

currentBestScore = 130537
currentBestPath = []

def insertNode(node):
    key = str(node["x"]) + "-" + str(node["y"]) + "-" + node["direction"]
    newBest = registerNodeIfNewBest(node)
    if not newBest:
        return
    for i in range(len(nodes)):
        newNodeKey = str(nodes[i]["x"]) + "-" + str(nodes[i]["y"]) + "-" + nodes[i]["direction"]
        if key == newNodeKey:
            for path in node["paths"]:
                nodes[i]["paths"].append(path)
            return
        if nodes[i]["score"] > node["score"]:
            nodes.insert(i, node)
            return
    nodes.append(node)

def findNextNodes(node):
    testNodes = [checkForNodeInCurrentDirection(node)] + checkForNodesInOtherDirections(node)
    for testNode in testNodes:
        if testNode != None:
            insertNode(testNode)

def drawMapWithPaths(paths):
    newMap = []
    for line in map:
        newMap.append(list(line))
    for path in paths:
        for i in range(0, len(path)):
            x = path[i][0]
            y = path[i][1]
            newMap[y][x] = "O"
    for line in newMap:
        print("".join(line))
    print()

def prettyPrintNodes(nodes):
    for node in nodes:
        print(f"({node['x']}, {node['y']}), {node['direction']}, {node['points']},{node['score']}")
        #print(node["path"])
    print()

currentBestPaths = []
j = 0
while len(nodes) > 0:
    currentNode = nodes.pop(0)
    if currentNode["score"] > currentBestScore:
        continue
    if currentNode["x"] == endingPos[0] and currentNode["y"] == endingPos[1]:
        if currentNode["score"] == currentBestScore:
            for path in currentNode["paths"]:
                currentBestPaths.append(path)
            continue
        currentBestScore = currentNode["score"]
        currentBestPaths = currentNode["paths"]
        print(currentBestScore, j)
        print(len(currentNode["paths"]))
        continue
    findNextNodes(currentNode)
    j += 1
    if j % 1000 == 0:
        print(j)
        print(currentBestScore)
        print(len(nodes))

drawMapWithPaths(currentBestPaths)

pointsOnAnyBestPath = {}
numberOfPointsOnAnyBestPath = 0
for path in currentBestPaths:
    for point in path:
        key = str(point[0]) + "-" + str(point[1])
        if key in pointsOnAnyBestPath:
            continue
        pointsOnAnyBestPath[key] = True
        numberOfPointsOnAnyBestPath += 1
print(numberOfPointsOnAnyBestPath)