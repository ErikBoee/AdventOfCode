file = open("input.txt", "r")
lines = file.readlines()
file.close()

map = []
for line in lines:
    map.append(list(line.strip()))

def northIsOk(x, y, number):
    return y > 0 and map[y - 1][x] != "." and int(map[y - 1][x]) - number == 1

def southIsOk(x, y, number):
    return y < len(map) - 1 and map[y + 1][x] != "." and int(map[y + 1][x]) - number == 1

def eastIsOk(x, y, number):
    return x < len(map[0]) - 1 and map[y][x + 1] != "." and int(map[y][x + 1]) - number == 1

def westIsOk(x, y, number):
    return x > 0 and map[y][x - 1] != "." and int(map[y][x - 1]) - number == 1

def positionToString(x, y):
    return str(x) + "-" + str(y)


def trailHeadsFromPosition(x, y, alreadyVisited):
    if positionToString(x, y) in alreadyVisited:
        return 0
    number = int(map[y][x])
    if number == 9:
        alreadyVisited[positionToString(x, y)] = True
        return 1
    
    northResults = 0
    southResults = 0
    eastResults = 0
    westResults = 0

    if northIsOk(x, y, number):
        northResults = trailHeadsFromPosition(x, y - 1, alreadyVisited)
    if southIsOk(x, y, number):
        southResults = trailHeadsFromPosition(x, y + 1, alreadyVisited)
    if eastIsOk(x, y, number):
        eastResults = trailHeadsFromPosition(x + 1, y, alreadyVisited)
    if westIsOk(x, y, number):
        westResults = trailHeadsFromPosition(x - 1, y, alreadyVisited)
    
    result = northResults + southResults + eastResults + westResults
    return result



totalTrailHeads = 0
for y in range(len(map)):
    line = map[y]
    for x in range(len(line)):
        if line[x] == "0":
            totalTrailHeads += trailHeadsFromPosition(x, y, {})

print(totalTrailHeads)