import copy
import matplotlib.pyplot as plt

file = open("input.txt", "r")
lines = file.readlines()
file.close()

board = [[c for c in line.strip()] for line in lines]

startingPos = [0, 0]
for i in range(len(board)):
    for j in range(len(board[0])):
        if board[i][j] == "S":
            startingPos = [i, j]

def positionOnBoardRow(i):
    if i >= 0 and i < len(board):
        return i
    elif i < 0:
        rest = (abs(i) - 1) % len(board)
        return len(board) - 1 - rest
    elif i >= len(board):
        return i % len(board)

def positionOnBoardColumn(j):
    if j >= 0 and j < len(board[0]):
        return j
    elif j < 0:
        rest = (abs(j) - 1) % len(board[0])
        return len(board[0]) - 1 - rest
    elif j >= len(board[0]):
        return j % len(board[0])

def quad(y, n):
    a = (y[2] - 2 * y[1] + y[0]) // 2
    b = y[1] - y[0] - a
    c = y[0]
    return a * n * n + b * n + c

def numberOfPossibleEndSteps(startPos, numberOfSteps):
    visitedTiles = {}
    points = [(startPos, 0)]
    numberOfEndTiles = {}
    while len(points) > 0:
        currentPoint = points.pop(0)
        pos = currentPoint[0]
        dist = currentPoint[1]
        if (str(pos)) in visitedTiles or dist > numberOfSteps:
            continue
        else:
            visitedTiles[str(pos)] = True
        formerEndTiles = numberOfEndTiles.get(dist, 0)
        numberOfEndTiles[dist] = formerEndTiles + 1
        if board[positionOnBoardRow(pos[0] + 1)][positionOnBoardColumn(pos[1])] != "#":
            points.append(([pos[0] + 1, pos[1]], dist + 1))
        if board[positionOnBoardRow(pos[0] - 1)][positionOnBoardColumn(pos[1])] != "#":
            points.append(([pos[0] - 1, pos[1]], dist + 1))
        if board[positionOnBoardRow(pos[0])][positionOnBoardColumn(pos[1] + 1)] != "#":
            points.append(([pos[0], pos[1] + 1], dist + 1))
        if board[positionOnBoardRow(pos[0])][positionOnBoardColumn(pos[1] - 1)] != "#":
            points.append(([pos[0], pos[1] - 1], dist + 1))
    originalNumberOfEndTiles = copy.deepcopy(numberOfEndTiles)
    for key in originalNumberOfEndTiles:
        numberOfEndTiles[key] = sum(amount for _key, amount in originalNumberOfEndTiles.items() if _key <= key and key % 2 == _key % 2)
    return numberOfEndTiles
size = len(board)
distToEdge = size//2


tiles = numberOfPossibleEndSteps(startingPos, 459)

y = [tiles[distToEdge], tiles[distToEdge + size], tiles[distToEdge + 2*size]]
finalDest = 26501365
print(quad(y, 3) == tiles[distToEdge + 3*size])
print(quad(y, (26501365 - distToEdge)//size))
