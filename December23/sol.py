import copy
file = open("input.txt", "r")
lines = file.readlines()
file.close()

board = []
for line in lines:
    lineList = list(line.strip())
    board.append(lineList)

startingPos = [0, 0]
for i in range(len(board[0])):
    if board[0][i] == ".":
        startingPos = [0, i]
        break

def drawBoardWithVisitedTiles(board, visitedTiles):
    boardCopy = copy.deepcopy(board)
    for visitedTile in visitedTiles:
        positions = visitedTile.split(",")
        firstPos = int(positions[0][1:])
        secondPos = int(positions[1][:-1])
        boardCopy[firstPos][secondPos] = "O"
    for line in boardCopy:
        print("".join(line))

longestPath = 0
def followPath(board, startPos, visitedTiles):
    pos = startPos
    while True:
        if pos[0] == len(board) - 1:
            global longestPath
            if len(visitedTiles) > longestPath:
                longestPath = len(visitedTiles)
            return
        visitedTiles[str(pos)] = True
        nextPositions = []
        tile = board[pos[0]][pos[1]]
        if tile == ">":
            nextPositions.append([pos[0], pos[1] + 1])
        elif tile == "<":
            nextPositions.append([pos[0], pos[1] - 1])
        elif tile == "^":
            nextPositions.append([pos[0] - 1, pos[1]])
        elif tile == "v":
            nextPositions.append([pos[0] + 1, pos[1]])
        else:
            for (x, y) in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                if board[pos[0] + x][pos[1] + y] != "#":
                    nextPositions.append([pos[0] + x, pos[1] + y])
        approvedNextPositions = []
        for nextPos in nextPositions:
            if str(nextPos) not in visitedTiles:
                approvedNextPositions.append(nextPos)
        if len(approvedNextPositions) == 0:
            return
        elif len(approvedNextPositions) == 1:
            pos = approvedNextPositions[0]
        else:
            for nextPos in approvedNextPositions[1:]:
                copyOfVisitedTiles = copy.deepcopy(visitedTiles)
                followPath(board, nextPos, copyOfVisitedTiles)
            pos = approvedNextPositions[0]


def followPathToNewIntersection(board, startPos, visitedTiles):
    foundIntersection = False
    pos = startPos
    steps = 0
    visitedTiles[str(pos)] = True
    while not foundIntersection:
        steps += 1
        nextPositions = []
        for (x, y) in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            if board[pos[0] + x][pos[1] + y] != "#":
                nextPositions.append([pos[0] + x, pos[1] + y])
        approvedNextPositions = []
        for nextPos in nextPositions:
            if str(nextPos) not in visitedTiles:
                approvedNextPositions.append(nextPos)
        if len(approvedNextPositions) == 1:
            pos = approvedNextPositions[0]
            if pos[0] == len(board) - 1 or pos[0] == 0:
                return steps + 1, pos
        else:
            foundIntersection = True
        visitedTiles[str(pos)] = True
    return steps, pos

def connectIntersections(board, startPos):
    savedIntersections = [{"pos": startPos, "neigbors": []}]
    intersections = [{"pos": startPos, "neigbors": []}]
    visitedIntersections = {str(startPos): True}
    while len(intersections) > 0:
        intersection = intersections.pop(0)
        savedIntersection = next((x for x in savedIntersections if x["pos"] == intersection["pos"]), None)
        if intersection["pos"][0] == len(board) - 1:
            continue
        pos = intersection["pos"]
        possiblePaths =[]
        if board[pos[0]][pos[1] + 1] != "#":
            possiblePaths.append([pos[0], pos[1] + 1])
        if board[pos[0]][pos[1] - 1] != "#":
            possiblePaths.append([pos[0], pos[1] - 1])
        if pos[0] > 0 and board[pos[0] - 1][pos[1]] != "#":
            possiblePaths.append([pos[0] - 1, pos[1]])
        if board[pos[0] + 1][pos[1]] != "#":
            possiblePaths.append([pos[0] + 1, pos[1]])
        for possiblePath in possiblePaths:
            if possiblePath[0] == len(board) - 1:
                continue
            steps, newPos = followPathToNewIntersection(board, possiblePath, {str(pos): True})
            if str(newPos) not in visitedIntersections and possiblePath[0] != len(board) - 1:
                visitedIntersections[str(newPos)] = True
                savedIntersections.append({"pos": newPos, "neigbors": []})
                intersections.append({"pos": newPos, "neigbors": []})
            if newPos[0] == len(board) - 1:
                savedIntersection["neigbors"] = [{"pos": newPos, "steps": steps}]
                break
            savedIntersection["neigbors"].append({"pos": newPos, "steps": steps})
    return savedIntersections                     

numberOfIntersections = 0
intersections = [startingPos]
superIntersections = []
for i in range(len(board)):
    for j in range(len(board[0])):
        if board[i][j] == "#" or i == 0 or i == len(board) - 1 or j == 0 or j == len(board[0]) - 1:
            continue
        hits = 0
        for pos in [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]:
            if board[pos[0]][pos[1]] != "#":
                hits += 1
        if hits > 2:
            numberOfIntersections += 1
            intersections.append([i, j])
            if hits > 3:
                superIntersections.append([i, j])

longestPathIntersection = 0
def findPathFromIntersections(intersections, startingPos, visitedIntersections, pathLength):
    intersectionMap = {}
    for intersection in intersections:
        intersectionMap[str(intersection["pos"])] = intersection
    intersection = intersectionMap[str(startingPos)]
    visitedIntersections[str(intersection["pos"])] = True
    if len(intersection["neigbors"]) > 0:
        for newIntersection in intersection["neigbors"]:
            copyOfVisitedIntersections = copy.deepcopy(visitedIntersections)
            if str(newIntersection["pos"]) not in visitedIntersections:
                findPathFromIntersections(intersections, newIntersection["pos"], copyOfVisitedIntersections, pathLength + newIntersection["steps"])
    else:
        global longestPathIntersection
        if pathLength > longestPathIntersection:
            print(pathLength)
            longestPathIntersection = pathLength
    return

intersections = connectIntersections(board, startingPos)
visitedIntersections = {}
followPath(board, startingPos, {})
print("Part 1", longestPath)

findPathFromIntersections(intersections, startingPos, visitedIntersections, 0)
print("Part 2", longestPathIntersection)