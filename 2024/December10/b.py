from a import *

file = open("input.txt", "r")
lines = file.readlines()
file.close()

map = []
for line in lines:
    map.append(list(line.strip()))

positionToNumberOfTrailHeads = {}

def distinctPathsFromPosition(x, y):
    number = int(map[y][x])
    if number == 9:
        return 1
    if positionToString(x, y) in positionToNumberOfTrailHeads:
        return positionToNumberOfTrailHeads[positionToString(x, y)]
    
    northResults = 0
    southResults = 0
    eastResults = 0
    westResults = 0

    if northIsOk(x, y, number):
        northResults = distinctPathsFromPosition(x, y - 1)
    if southIsOk(x, y, number):
        southResults = distinctPathsFromPosition(x, y + 1)
    if eastIsOk(x, y, number):
        eastResults = distinctPathsFromPosition(x + 1, y)
    if westIsOk(x, y, number):
        westResults = distinctPathsFromPosition(x - 1, y)
    
    result = northResults + southResults + eastResults + westResults
    positionToNumberOfTrailHeads[positionToString(x, y)] = result
    return result



totalTrailHeads = 0
for y in range(len(map)):
    line = map[y]
    for x in range(len(line)):
        if line[x] == "0":
            totalTrailHeads += distinctPathsFromPosition(x, y)

print(totalTrailHeads)