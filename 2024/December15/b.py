file = open("input.txt", "r")
lines = file.readlines()
file.close()

def prettyPrintMap(map):
    for line in map:
        print("".join(line))

expandedMap = []
instructions = ""
pos = [0, 0]

hasReachedBreak = False
for y in range(len(lines)):
    line = lines[y].strip()
    if line == "":
        hasReachedBreak = True
        continue
    if hasReachedBreak:
        instructions += line
        continue
    stringline = ""
    for x in range(len(line)):
        char = line[x]
        if char == "@":
            pos = [2*x, y]
            stringline += "@."
            continue
        if char == "O":
            stringline += "[]"
            continue
        stringline += char + char
    expandedMap.append(list(stringline))


def canMoveUp(map, pos):
    if map[pos[1] - 1][pos[0]] == ".":
        return True
    if map[pos[1] - 1][pos[0]] == "[":
        return canMoveUp(map, [pos[0], pos[1] - 1]) and canMoveUp(map, [pos[0] + 1, pos[1] - 1])
    if map[pos[1] - 1][pos[0]] == "]":
        return canMoveUp(map, [pos[0], pos[1] - 1]) and canMoveUp(map, [pos[0] - 1, pos[1] - 1])
    return False

def moveBoxOneUp(map, pos):
    map[pos[1] - 1][pos[0]] = map[pos[1]][pos[0]]
    map[pos[1]][pos[0]] = "."
    return map

def moveBoxesUp(map, pos):
    if map[pos[1] - 1][pos[0]] == ".":
        return moveBoxOneUp(map, pos)
    elif map[pos[1] - 1][pos[0]] == "[":
        map = moveBoxesUp(map, [pos[0], pos[1] - 1])
        map = moveBoxesUp(map, [pos[0] + 1, pos[1] - 1])
        return moveBoxOneUp(map, pos)
    elif map[pos[1] - 1][pos[0]] == "]":
        map = moveBoxesUp(map, [pos[0], pos[1] - 1])
        map = moveBoxesUp(map, [pos[0] - 1, pos[1] - 1])
        return moveBoxOneUp(map, pos)
    return map
    

def moveUp(map, pos):
    if not canMoveUp(map, pos):
        return map, pos
    if map[pos[1] - 1][pos[0]] == ".":
        map[pos[1] - 1][pos[0]] = "@"
        map[pos[1]][pos[0]] = "."
        return map, [pos[0], pos[1] - 1]
    if map[pos[1] - 1][pos[0]] == "[":
        map = moveBoxesUp(map, [pos[0], pos[1] - 1])
        map = moveBoxesUp(map, [pos[0] + 1, pos[1] - 1])
        map[pos[1] - 1][pos[0]] = "@"
        map[pos[1]][pos[0]] = "."
        return map, [pos[0], pos[1] - 1]
    if map[pos[1] - 1][pos[0]] == "]":
        map = moveBoxesUp(map, [pos[0], pos[1] - 1])
        map = moveBoxesUp(map, [pos[0] - 1, pos[1] - 1])
        map[pos[1] - 1][pos[0]] = "@"
        map[pos[1]][pos[0]] = "."
        return map, [pos[0], pos[1] - 1]
    return map, pos

def canMoveDown(map, pos):
    if map[pos[1] + 1][pos[0]] == ".":
        return True
    if map[pos[1] + 1][pos[0]] == "[":
        return canMoveDown(map, [pos[0], pos[1] + 1]) and canMoveDown(map, [pos[0] + 1, pos[1] + 1])
    if map[pos[1] + 1][pos[0]] == "]":
        return canMoveDown(map, [pos[0], pos[1] + 1]) and canMoveDown(map, [pos[0] - 1, pos[1] + 1])
    return False

def moveBoxOneDown(map, pos):
    map[pos[1] + 1][pos[0]] = map[pos[1]][pos[0]]
    map[pos[1]][pos[0]] = "."
    return map

def moveBoxesDown(map, pos):
    if map[pos[1] + 1][pos[0]] == ".":
        return moveBoxOneDown(map, pos)
    elif map[pos[1] + 1][pos[0]] == "[":
        map = moveBoxesDown(map, [pos[0], pos[1] + 1])
        map = moveBoxesDown(map, [pos[0] + 1, pos[1] + 1])
        return moveBoxOneDown(map, pos)
    elif map[pos[1] + 1][pos[0]] == "]":
        map = moveBoxesDown(map, [pos[0], pos[1] + 1])
        map = moveBoxesDown(map, [pos[0] - 1, pos[1] + 1])
        return moveBoxOneDown(map, pos)
    return map

def moveDown(map, pos):
    if not canMoveDown(map, pos):
        return map, pos
    if map[pos[1] + 1][pos[0]] == ".":
        map[pos[1] + 1][pos[0]] = "@"
        map[pos[1]][pos[0]] = "."
        return map, [pos[0], pos[1] + 1]
    if map[pos[1] + 1][pos[0]] == "[":
        map = moveBoxesDown(map, [pos[0], pos[1] + 1])
        map = moveBoxesDown(map, [pos[0] + 1, pos[1] + 1])
        map[pos[1] + 1][pos[0]] = "@"
        map[pos[1]][pos[0]] = "."
        return map, [pos[0], pos[1] + 1]
    if map[pos[1] + 1][pos[0]] == "]":
        map = moveBoxesDown(map, [pos[0], pos[1] + 1])
        map = moveBoxesDown(map, [pos[0] - 1, pos[1] + 1])
        map[pos[1] + 1][pos[0]] = "@"
        map[pos[1]][pos[0]] = "."
        return map, [pos[0], pos[1] + 1]
    return map, pos



def moveLeft(map, pos):
    blocksToMove = 1
    while map[pos[1]][pos[0] - blocksToMove] != ".":
        if map[pos[1]][pos[0] - blocksToMove] == "#":
            return map, pos
        blocksToMove += 1
    
    for i in range(blocksToMove, -1, -1):
        if i == 0:
            map[pos[1]][pos[0] - i] = "."
            continue
        if i == 1:
            map[pos[1]][pos[0] - i] = "@"
            continue
        char = map[pos[1]][pos[0] - i + 1]
        map[pos[1]][pos[0] - i] = char
    return map, [pos[0] - 1, pos[1]]

def moveRight(map, pos):
    blocksToMove = 1
    while map[pos[1]][pos[0] + blocksToMove] != ".":
        if map[pos[1]][pos[0] + blocksToMove] == "#":
            return map, pos
        blocksToMove += 1
    
    for i in range(blocksToMove, -1, -1):
        if i == 0:
            map[pos[1]][pos[0] + i] = "."
            continue
        if i == 1:
            map[pos[1]][pos[0] + i] = "@"
            continue
        char = map[pos[1]][pos[0] + i - 1]
        map[pos[1]][pos[0] + i] = char
    return map, [pos[0] + 1, pos[1]]
        


def followInstruction(map, instruction, pos):
    if instruction == "^":
        map, pos = moveUp(map, pos)
    if instruction == "v":
        map, pos = moveDown(map, pos)
    if instruction == "<":
        map, pos = moveLeft(map, pos)
    if instruction == ">":
        map, pos = moveRight(map, pos)
    return map, pos

for instruction in instructions:
    expandedMap, pos = followInstruction(expandedMap, instruction, pos)

totalScore = 0
for y in range(len(expandedMap)):
    for x in range(len(expandedMap[y])):
        if expandedMap[y][x] == "[":
            totalScore += 100*y + x

print(totalScore)
    

