import heapq

file = open("input.txt", "r")
lines = file.readlines()
file.close()


counter = 0

board = []
for line in lines:
    lineList = list(line.strip())
    board.append(lineList)
def h(board, pos):
    return (abs(pos[0] - len(board) + 1) + abs(pos[1] - len(board[0]) + 1))

def addNeighborsDirRight(board, pos, numberOfStepsDir, pathLength, neighbors):
    global counter
    formerVisitedKey = str(pos) + "right" + str(numberOfStepsDir)
    if numberOfStepsDir < 10 and pos[1] + 1 < len(board[0]):
        newPos = [pos[0], pos[1] + 1]
        newPathLength = pathLength + int(board[newPos[0]][newPos[1]])
        aStarValue = newPathLength + h(board, newPos)
        heapq.heappush(neighbors, [aStarValue, counter, {"pos": newPos, "dir": "right", "numberOfStepsDir": numberOfStepsDir + 1, "pathLength": newPathLength, "from": pos, "formerKey": formerVisitedKey}])
        counter = counter + 1
    if numberOfStepsDir >= 4:
        if pos[0] + 1 < len(board):
            newPos = [pos[0] + 1, pos[1]]
            newPathLength = pathLength + int(board[newPos[0]][newPos[1]])
            aStarValue = newPathLength + h(board, newPos)
            heapq.heappush(neighbors, [aStarValue, counter, {"pos": newPos, "dir": "down", "numberOfStepsDir": 1, "pathLength": newPathLength, "from": pos, "formerKey": formerVisitedKey}])
            counter = counter + 1

        if pos[0] - 1 >= 0:
            newPos = [pos[0] - 1, pos[1]]
            newPathLength = pathLength + int(board[newPos[0]][newPos[1]])
            aStarValue = newPathLength + h(board, newPos)
            heapq.heappush(neighbors, [aStarValue, counter, {"pos": newPos, "dir": "up", "numberOfStepsDir": 1, "pathLength": newPathLength, "from": pos, "formerKey": formerVisitedKey}])
            counter = counter + 1
    return neighbors

def addNeighborsDirDown(board, pos, numberOfStepsDir, pathLength, neighbors):
    global counter
    formerVisitedKey = str(pos) + "down" + str(numberOfStepsDir)
    if numberOfStepsDir < 10 and pos[0] + 1 < len(board):
        newPos = [pos[0] + 1, pos[1]]
        newPathLength = pathLength + int(board[newPos[0]][newPos[1]])
        aStarValue = newPathLength + h(board, newPos)
        heapq.heappush(neighbors, [aStarValue, counter, {"pos": newPos, "dir": "down", "numberOfStepsDir": numberOfStepsDir + 1, "pathLength": newPathLength, "from": pos, "formerKey": formerVisitedKey}])
        counter = counter + 1

    if numberOfStepsDir >= 4:
        if pos[1] + 1 < len(board[0]):
            newPos = [pos[0], pos[1] + 1]
            newPathLength = pathLength + int(board[newPos[0]][newPos[1]])
            aStarValue = newPathLength + h(board, newPos)
            heapq.heappush(neighbors, [aStarValue, counter, {"pos": newPos, "dir": "right", "numberOfStepsDir": 1, "pathLength": newPathLength, "from": pos, "formerKey": formerVisitedKey}])
            counter = counter + 1

        if pos[1] - 1 >= 0:
            newPos = [pos[0], pos[1] - 1]
            newPathLength = pathLength + int(board[newPos[0]][newPos[1]])
            aStarValue = newPathLength + h(board, newPos)
            heapq.heappush(neighbors, [aStarValue, counter, {"pos": newPos, "dir": "left", "numberOfStepsDir": 1, "pathLength": newPathLength, "from": pos, "formerKey": formerVisitedKey}])
            counter = counter + 1
    return neighbors

def addNeighborsDirLeft(board, pos, numberOfStepsDir, pathLength, neighbors):
    global counter
    formerVisitedKey = str(pos) + "left" + str(numberOfStepsDir)
    if numberOfStepsDir < 10 and pos[1] - 1 >= 0:
        newPos = [pos[0], pos[1] - 1]
        newPathLength = pathLength + int(board[newPos[0]][newPos[1]])
        aStarValue = newPathLength + h(board, newPos)
        heapq.heappush(neighbors, [aStarValue, counter, {"pos": newPos, "dir": "left", "numberOfStepsDir": numberOfStepsDir + 1, "pathLength": newPathLength, "from": pos, "formerKey": formerVisitedKey}])
        counter = counter + 1

    if numberOfStepsDir >= 4:
        if pos[0] + 1 < len(board):
            newPos = [pos[0] + 1, pos[1]]
            newPathLength = pathLength + int(board[newPos[0]][newPos[1]])
            aStarValue = newPathLength + h(board, newPos)
            heapq.heappush(neighbors, [aStarValue, counter, {"pos": newPos, "dir": "down", "numberOfStepsDir": 1, "pathLength": newPathLength, "from": pos, "formerKey": formerVisitedKey}])
            counter = counter + 1

        if pos[0] - 1 >= 0:
            newPos = [pos[0] - 1, pos[1]]
            newPathLength = pathLength + int(board[newPos[0]][newPos[1]])
            aStarValue = newPathLength + h(board, newPos)
            heapq.heappush(neighbors, [aStarValue, counter, {"pos": newPos, "dir": "up", "numberOfStepsDir": 1, "pathLength": newPathLength, "from": pos, "formerKey": formerVisitedKey}])
            counter = counter + 1
    return neighbors

def addNeighborsDirUp(board, pos, numberOfStepsDir, pathLength, neighbors):
    global counter
    formerVisitedKey = str(pos) + "up" + str(numberOfStepsDir)
    if numberOfStepsDir < 10 and pos[0] - 1 >= 0:
        newPos = [pos[0] - 1, pos[1]]
        newPathLength = pathLength + int(board[newPos[0]][newPos[1]])
        aStarValue = newPathLength + h(board, newPos)
        heapq.heappush(neighbors, [aStarValue, counter, {"pos": newPos, "dir": "up", "numberOfStepsDir": numberOfStepsDir + 1, "pathLength": newPathLength, "from": pos, "formerKey": formerVisitedKey}])
        counter = counter + 1

    if numberOfStepsDir >= 4:
        if pos[1] + 1 < len(board[0]):
            newPos = [pos[0], pos[1] + 1]
            newPathLength = pathLength + int(board[newPos[0]][newPos[1]])
            aStarValue = newPathLength + h(board, newPos)
            heapq.heappush(neighbors, [aStarValue, counter, {"pos": newPos, "dir": "right", "numberOfStepsDir": 1, "pathLength": newPathLength, "from": pos, "formerKey": formerVisitedKey}])
            counter = counter + 1

        if pos[1] - 1 >= 0:
            newPos = [pos[0], pos[1] - 1]
            newPathLength = pathLength + int(board[newPos[0]][newPos[1]])
            aStarValue = newPathLength + h(board, newPos)
            heapq.heappush(neighbors, [aStarValue, counter, {"pos": newPos, "dir": "left", "numberOfStepsDir": 1, "pathLength": newPathLength, "from": pos, "formerKey": formerVisitedKey}])
            counter = counter + 1
    return neighbors



def addNeighbors(board, neighbor, neighbors):
    pos = neighbor["pos"]
    dir = neighbor["dir"]
    numberOfStepsDir = neighbor["numberOfStepsDir"]
    pathLength = neighbor["pathLength"]
    if dir == "right":
        return addNeighborsDirRight(board, pos, numberOfStepsDir, pathLength, neighbors)  
    if dir == "down":
        return addNeighborsDirDown(board, pos, numberOfStepsDir, pathLength, neighbors)
    if dir == "left":
        return addNeighborsDirLeft(board, pos, numberOfStepsDir, pathLength, neighbors)
    
    return addNeighborsDirUp(board, pos, numberOfStepsDir, pathLength, neighbors)

def printBoardPath(board, visited, visitedKey):
    pos = [len(board) - 1, len(board[0]) - 1]
    path = []
    while visitedKey in visited:
        if pos == [0, 0]:
            break
        path.append([pos[0], pos[1], visited[visitedKey]["pathLength"]])
        pos = visited[visitedKey]["formerPos"]
        visitedKey = visited[visitedKey]["formerKey"]
    path.append([0, 0, 0])
    path.reverse()
    for t in path:
        pos = t[0:2]
        pathLength = t[2]
        board[pos[0]][pos[1]] = str(pathLength)
    for line in board:
        print(line)
    print("")

    for t in path:
        pos = t[0:2]
        board[pos[0]][pos[1]] = "*"
    for line in board:
        print("".join(line))

def findShortestPath(board, startPos):
    global counter
    pathLength = 0
    aStarValue = pathLength + h(board, startPos)
    neighbors = [[aStarValue, counter, {"pos": startPos, "dir": "right", "numberOfStepsDir": 0, "pathLength": pathLength}], [aStarValue, counter, {"pos": startPos, "dir": "down", "numberOfStepsDir": 0, "pathLength": pathLength}]]
    counter = counter + 1
    visited = {}
    while len(neighbors) > 0:
        neighbor = heapq.heappop(neighbors)
        visitedKey = str(neighbor[2]["pos"]) + str(neighbor[2]["dir"]) + str(neighbor[2]["numberOfStepsDir"])
        if visitedKey in visited:
            continue
        if neighbor[2]["pos"] == [len(board) - 1, len(board[0]) - 1] and neighbor[2]["numberOfStepsDir"] >= 4:
            visited[visitedKey] = {"formerPos": neighbor[2].get("from"), "formerKey": neighbor[2].get("formerKey"), "pathLength": neighbor[2].get("pathLength")}
            printBoardPath(board, visited, visitedKey)
            return neighbor[2]["pathLength"]
        neighbors = addNeighbors(board, neighbor[2], neighbors)
        visited[visitedKey] = {"formerPos": neighbor[2].get("from"), "formerKey": neighbor[2].get("formerKey"), "pathLength": neighbor[2].get("pathLength")}
    return None      
        

print(findShortestPath(board, [0, 0]))

        

    