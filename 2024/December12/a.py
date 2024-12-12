file = open("input.txt", "r")
lines = file.readlines()
file.close()

map = []
for line in lines:
    map.append(list(line.strip()))

def positionToString(x, y):
    return str(x) + "-" + str(y)

alreadyAccountedAreas = {}

def tileAboveIsSameCharacter(x, y, char):
    return y > 0 and map[y - 1][x] == char

def tileBelowIsSameCharacter(x, y, char):
    return y < len(map) - 1 and map[y + 1][x] == char

def tileLeftIsSameCharacter(x, y, char):
    return x > 0 and map[y][x - 1] == char

def tileRightIsSameCharacter(x, y, char):
    return x < len(map[0]) - 1 and map[y][x + 1] == char


def findCurrentArea(x,y, char, alreadyVisited, currentPerimeter = 0, currentArea = 0):
    if positionToString(x, y) in alreadyVisited:
        return currentArea, currentPerimeter
    alreadyVisited[positionToString(x, y)] = True
    alreadyAccountedAreas[positionToString(x, y)] = True
    currentArea += 1
    if tileAboveIsSameCharacter(x, y, char):
        currentArea, currentPerimeter = findCurrentArea(x, y - 1, char, alreadyVisited, currentPerimeter, currentArea)
    else:
        currentPerimeter += 1
    
    if tileBelowIsSameCharacter(x, y, char):
         currentArea, currentPerimeter = findCurrentArea(x, y + 1, char, alreadyVisited, currentPerimeter, currentArea)
    else:
        currentPerimeter += 1

    if tileLeftIsSameCharacter(x, y, char):
        currentArea, currentPerimeter = findCurrentArea(x - 1, y, char, alreadyVisited, currentPerimeter, currentArea)
    else:
        currentPerimeter += 1

    if tileRightIsSameCharacter(x, y, char):
        currentArea, currentPerimeter = findCurrentArea(x + 1, y, char, alreadyVisited, currentPerimeter, currentArea)
    else:
        currentPerimeter += 1
    
    return currentArea, currentPerimeter

totalPrice = 0
for y in range(len(map)):
    line = map[y]
    for x in range(len(line)):
        if positionToString(x, y) not in alreadyAccountedAreas:
            currentArea, currentPerimeter = findCurrentArea(x, y, map[y][x], {})
            totalPrice += currentArea * currentPerimeter

print(totalPrice)