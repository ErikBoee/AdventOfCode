from a import *
file = open("input.txt", "r")
lines = file.readlines()
file.close()

map = []
for line in lines:
    map.append(list(line.strip()))

def posAndDirToString(x, y, direction):
    return str(x) + "-" + str(y) + "-" + direction

positionAndPerimeterPosRegistered = {}

def lookLeftForDiscount(x, y, char, direction):
    posX = x
    posY = y
    foundDiscount = False
    while True:
        if not tileLeftIsSameCharacter(posX, posY, char):
            break
        if posAndDirToString(posX-1, posY, direction) in positionAndPerimeterPosRegistered:
            foundDiscount = True
            break
        if direction == "up" and tileAboveIsSameCharacter(posX - 1, posY, char):
            break
        if direction == "down" and tileBelowIsSameCharacter(posX - 1, posY, char):
            break
        posX -= 1
    return foundDiscount

def lookRightForDiscount(x, y, char, direction):
    posX = x
    posY = y
    foundDiscount = False
    while True: 
        if not tileRightIsSameCharacter(posX, posY, char):
            break
        if posAndDirToString(posX+1, posY, direction) in positionAndPerimeterPosRegistered:
            foundDiscount = True
            break
        if direction == "up" and tileAboveIsSameCharacter(posX + 1, posY, char):
            break
        if direction == "down" and tileBelowIsSameCharacter(posX + 1, posY, char):
            break
        posX += 1
    return foundDiscount

def lookUpForDiscount(x, y, char, direction):
    posX = x
    posY = y
    foundDiscount = False
    while True:
        if not tileAboveIsSameCharacter(posX, posY, char):
            break
        if posAndDirToString(posX, posY-1, direction) in positionAndPerimeterPosRegistered:
            foundDiscount = True
            break
        if direction == "left" and tileLeftIsSameCharacter(posX, posY - 1, char):
            break
        if direction == "right" and tileRightIsSameCharacter(posX, posY - 1, char):
            break
        posY -= 1
    return foundDiscount

def lookDownForDiscount(x, y, char, direction):
    posX = x
    posY = y
    foundDiscount = False
    while True:
        if not tileBelowIsSameCharacter(posX, posY, char):
            break
        if posAndDirToString(posX, posY+1, direction) in positionAndPerimeterPosRegistered:
            foundDiscount = True
            break
        if direction == "left" and tileLeftIsSameCharacter(posX, posY + 1, char):
            break
        if direction == "right" and tileRightIsSameCharacter(posX, posY + 1, char):
            break
        posY += 1
    return foundDiscount

        

def getPerimeterValueAfterDiscount(x, y, char, direction):
    positionAndPerimeterPosRegistered[posAndDirToString(x, y, direction)] = True
    if direction == "up" or direction == "down":
        if lookLeftForDiscount(x, y, char, direction) or lookRightForDiscount(x, y, char, direction):
            return 0
        else:
            return 1
    if direction == "left" or direction == "right":
        if lookUpForDiscount(x, y, char, direction) or lookDownForDiscount(x, y, char, direction):
            return 0
        else:
            return 1
        
def findCurrentAreaAfterDiscount(x,y, char, alreadyVisited, currentPerimeter = 0, currentArea = 0):
    if positionToString(x, y) in alreadyVisited:
        return currentArea, currentPerimeter
    alreadyVisited[positionToString(x, y)] = True
    alreadyAccountedAreas[positionToString(x, y)] = True
    currentArea += 1
    if tileAboveIsSameCharacter(x, y, char):
        currentArea, currentPerimeter = findCurrentAreaAfterDiscount(x, y - 1, char, alreadyVisited, currentPerimeter, currentArea)
    else:
        currentPerimeter += getPerimeterValueAfterDiscount(x, y, char, "up")
    
    if tileBelowIsSameCharacter(x, y, char):
         currentArea, currentPerimeter = findCurrentAreaAfterDiscount(x, y + 1, char, alreadyVisited, currentPerimeter, currentArea)
    else:
        currentPerimeter += getPerimeterValueAfterDiscount(x, y, char, "down")

    if tileLeftIsSameCharacter(x, y, char):
        currentArea, currentPerimeter = findCurrentAreaAfterDiscount(x - 1, y, char, alreadyVisited, currentPerimeter, currentArea)
    else:
        currentPerimeter += getPerimeterValueAfterDiscount(x, y, char, "left")

    if tileRightIsSameCharacter(x, y, char):
        currentArea, currentPerimeter = findCurrentAreaAfterDiscount(x + 1, y, char, alreadyVisited, currentPerimeter, currentArea)
    else:
        currentPerimeter += getPerimeterValueAfterDiscount(x, y, char, "right")
    
    return currentArea, currentPerimeter

alreadyAccountedAreas = {}
totalPrice = 0
for y in range(len(map)):
    line = map[y]
    for x in range(len(line)):
        if positionToString(x, y) not in alreadyAccountedAreas:
            char = map[y][x]
            currentArea, currentPerimeter = findCurrentAreaAfterDiscount(x, y, map[y][x], {})
            totalPrice += currentArea * currentPerimeter

print(totalPrice)