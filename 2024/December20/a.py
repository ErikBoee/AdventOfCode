file = open("input.txt", "r")
lines = file.readlines()
file.close()

map = []
startPos = [0, 0]
for y in range(len(lines)):
    line = lines[y]
    map.append(list(line.strip()))
    for x in range(len(line)):
        if line[x] == "S":
            startPos = [x, y]

def prettyPrintMap(map):
    for line in map:
        print("".join(line))

def posInMap(x, y):
    return y >= 0 and y < len(map) and x >= 0 and x < len(map[0])

def posInMapAndNotBlocked(x, y):
    return posInMap(x, y) and map[y][x] != "#"

def nextPosition(x, y):
    if map[y][x] == "E":
        return None
    for pos in [[x, y - 1], [x, y + 1], [x - 1, y], [x + 1, y]]:
        if posInMap(pos[0], pos[1]) and map[pos[1]][pos[0]] == "." or map[pos[1]][pos[0]] == "E":
            return pos
    return None

def walkPath(map):
    pos = startPos
    i = 0
    while pos != None:
        map[pos[1]][pos[0]] = str(i)
        pos = nextPosition(pos[0], pos[1])
        i += 1
    return map

map = walkPath(map)
prettyPrintMap(map)
def findShortCuts(map, minShortCutLength):
    pos = startPos
    numberOfGoodShortCuts = 0
    currentNumber = int(map[pos[1]][pos[0]])
    while pos != None:
        nextPos = None
        for direction in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
            posOneAway = [pos[0] + direction[0], pos[1] + direction[1]]
            posTwoAway = [pos[0] + 2 * direction[0], pos[1] + 2 * direction[1]]
            if posInMapAndNotBlocked(posOneAway[0], posOneAway[1]) and int(map[posOneAway[1]][posOneAway[0]]) == currentNumber + 1:
                nextPos = posOneAway
            elif posInMapAndNotBlocked(posTwoAway[0], posTwoAway[1]):
                nextNumber = int(map[posTwoAway[1]][posTwoAway[0]])
                if nextNumber - currentNumber >= (minShortCutLength + 2):
                    numberOfGoodShortCuts += 1
        currentNumber += 1
        pos = nextPos
    
    return numberOfGoodShortCuts
        
numberOfGoodShortCuts = findShortCuts(map, 100)

print(numberOfGoodShortCuts)