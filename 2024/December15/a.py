file = open("input.txt", "r")
lines = file.readlines()
file.close()

def prettyPrintMap(map):
    for line in map:
        print("".join(line))

map = []
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
        
    for x in range(len(line)):
        char = line[x]
        if char == "@":
            pos = [x, y]
    map.append(list(line))


def moveUp(map, pos):
    blocksToMove = 1
    while map[pos[1] - blocksToMove][pos[0]] != ".":
        if map[pos[1] - blocksToMove][pos[0]] == "#":
            return map, pos
        blocksToMove += 1
    for i in range(blocksToMove + 1):
        if i == 0:
            map[pos[1] - i][pos[0]] = "."
            continue
        if i == 1:
            map[pos[1] - i][pos[0]] = "@"
            continue
        map[pos[1] - i][pos[0]] = "O"
    return map, [pos[0], pos[1] - 1]

def moveDown(map, pos):
    blocksToMove = 1
    while map[pos[1] + blocksToMove][pos[0]] != ".":
        if map[pos[1] + blocksToMove][pos[0]] == "#":
            return map, pos
        blocksToMove += 1
    for i in range(blocksToMove + 1):
        if i == 0:
            map[pos[1] + i][pos[0]] = "."
            continue
        if i == 1:
            map[pos[1] + i][pos[0]] = "@"
            continue
        map[pos[1] + i][pos[0]] = "O"
    return map, [pos[0], pos[1] + 1]

def moveLeft(map, pos):
    blocksToMove = 1
    while map[pos[1]][pos[0] - blocksToMove] != ".":
        if map[pos[1]][pos[0] - blocksToMove] == "#":
            return map, pos
        blocksToMove += 1
    for i in range(blocksToMove + 1):
        if i == 0:
            map[pos[1]][pos[0] - i] = "."
            continue
        if i == 1:
            map[pos[1]][pos[0] - i] = "@"
            continue
        map[pos[1]][pos[0] - i] = "O"
    return map, [pos[0] - 1, pos[1]]

def moveRight(map, pos):
    blocksToMove = 1
    while map[pos[1]][pos[0] + blocksToMove] != ".":
        if map[pos[1]][pos[0] + blocksToMove] == "#":
            return map, pos
        blocksToMove += 1
    for i in range(blocksToMove + 1):
        if i == 0:
            map[pos[1]][pos[0] + i] = "."
            continue
        if i == 1:
            map[pos[1]][pos[0] + i] = "@"
            continue
        map[pos[1]][pos[0] + i] = "O"
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
    map, pos = followInstruction(map, instruction, pos)
prettyPrintMap(map)

totalScore = 0
for y in range(len(map)):
    for x in range(len(map[y])):
        if map[y][x] == "O":
            totalScore += 100*y + x

print(totalScore)
    

