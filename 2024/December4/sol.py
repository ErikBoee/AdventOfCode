
file = open("input.txt", "r")
lines = file.readlines()
file.close()

maxY = len(lines)
maxX = len(lines[0])

def foundUpwards(x, y, lines):
    if y < 3:
        return False
    return lines[y-1][x] == "M" and lines[y-2][x] == "A" and lines[y-3][x] == "S"

def foundDownwards(x, y, lines):
    if y > maxY - 4:
        return False
    return lines[y+1][x] == "M" and lines[y+2][x] == "A" and lines[y+3][x] == "S"

def foundLeft(x, y, lines):
    if x < 3:
        return False
    return lines[y][x-1] == "M" and lines[y][x-2] == "A" and lines[y][x-3] == "S"

def foundRight(x, y, lines):
    if x > maxX - 4:
        return False
    return lines[y][x+1] == "M" and lines[y][x+2] == "A" and lines[y][x+3] == "S"

def foundUpwardsRight(x, y, lines):
    if y < 3 or x > maxX - 4:
        return False
    return lines[y-1][x+1] == "M" and lines[y-2][x+2] == "A" and lines[y-3][x+3] == "S"

def foundUpwardsLeft(x, y, lines):
    if y < 3 or x < 3:
        return False
    return lines[y-1][x-1] == "M" and lines[y-2][x-2] == "A" and lines[y-3][x-3] == "S"

def foundDownwardsRight(x, y, lines):
    if y > maxY - 4 or x > maxX - 4:
        return False
    return lines[y+1][x+1] == "M" and lines[y+2][x+2] == "A" and lines[y+3][x+3] == "S"

def foundDownwardsLeft(x, y, lines):
    if y > maxY - 4 or x < 3:
        return False
    return lines[y+1][x-1] == "M" and lines[y+2][x-2] == "A" and lines[y+3][x-3] == "S"


def numberOfFoundXmas(x, y, lines):
    numberOfFound = 0
    if foundUpwards(x, y, lines):
        numberOfFound += 1
    if foundDownwards(x, y, lines):
        numberOfFound += 1
    if foundLeft(x, y, lines):
        numberOfFound += 1
    if foundRight(x, y, lines):
        numberOfFound += 1
    if foundUpwardsRight(x, y, lines):
        numberOfFound += 1
    if foundUpwardsLeft(x, y, lines):
        numberOfFound += 1
    if foundDownwardsRight(x, y, lines):
        numberOfFound += 1
    if foundDownwardsLeft(x, y, lines):
        numberOfFound += 1
    return numberOfFound

numnberOfXMAS = 0
for y in range(len(lines)):
    line = lines[y]
    for x in range(len(line)):
        if line[x] == "X":
            numnberOfXMAS += numberOfFoundXmas(x, y, lines)

print(numnberOfXMAS)

def foundDiagonalCrossMas(x, y, lines):
    if y < 1 or y > maxY - 2 or x < 1 or x > maxX - 2:
        return False
    yDirectionCorrect = (lines[y-1][x-1] == "M" and lines[y+1][x+1] == "S") or (lines[y-1][x-1] == "S" and lines[y+1][x+1] == "M")
    xDirectionCorrect = (lines[y-1][x+1] == "M" and lines[y+1][x-1] == "S") or (lines[y-1][x+1] == "S" and lines[y+1][x-1] == "M")
    return yDirectionCorrect and xDirectionCorrect

numnberOfCrossMAS = 0
for y in range(len(lines)):
    line = lines[y]
    for x in range(len(line)):
        if line[x] == "A" and foundDiagonalCrossMas(x, y, lines):
            numnberOfCrossMAS += 1

print(numnberOfCrossMAS)                
        