file = open("input.txt", "r")
lines = file.readlines()
file.close()

pos = [0,0]
positions = [pos]

formerDir = "U"

intToDir = {0: "R", 1: "D", 2: "L", 3: "U"}

def hexToDec(hex):
    return int(hex, 16)

for i in range(len(lines)):
    dir = intToDir[int(lines[i].split("#")[1][5])]
    steps = hexToDec(lines[i].split("#")[1][0:5])
    if i == len(lines) - 1:
        nextDir = "L"
    else:
        nextDir = intToDir[int(lines[i + 1].split("#")[1][5])]
    if dir == "U":
        if nextDir == formerDir:
            pos = [pos[0] - steps, pos[1]]
        elif nextDir == "L":
            pos = [pos[0] - steps + 1, pos[1]]
        elif nextDir == "R":
            pos = [pos[0] - steps - 1, pos[1]]
    elif dir == "D":
        if nextDir == formerDir:
            pos = [pos[0] + steps, pos[1]]
        elif nextDir == "L":
            pos = [pos[0] + steps + 1, pos[1]]
        elif nextDir == "R":
            pos = [pos[0] + steps - 1, pos[1]]
    elif dir == "L":
        if nextDir == formerDir:
            pos = [pos[0], pos[1] - steps]
        elif nextDir == "U":
            pos = [pos[0], pos[1] - steps - 1]
        elif nextDir == "D":
            pos = [pos[0], pos[1] - steps + 1]
    elif dir == "R":
        if nextDir == formerDir:
            pos = [pos[0], pos[1] + steps]
        elif nextDir == "U":
            pos = [pos[0], pos[1] + steps - 1]
        elif nextDir == "D":
            pos = [pos[0], pos[1] + steps + 1]
    formerDir = dir
    positions.append(pos)

area = 0
for i in range(len(positions) - 1):
    currentPos = positions[i]
    nextPos = positions[i + 1]
    area += currentPos[0] * nextPos[1] - currentPos[1] * nextPos[0]

print(int(abs(area)/2))