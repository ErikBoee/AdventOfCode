file = open("input.txt", "r")
lines = file.readlines()
file.close()

trenches = [["." for _ in range(490)] for _ in range(430)]

pos = [357, 201]

def keyFromPos(pos):
    return "H" + str(pos[0]) + "-" + "V" + str(pos[1])

horizontalDirs = {}
verticalDirs = {}
trenches[pos[0]][pos[1]] = "#"
for i in range(len(lines)):
    currentLine = lines[i]
    if i == len(lines) - 1:
        nextLine = "L 0"
    else:
        nextLine = lines[i + 1]
    nextDir = nextLine.split()[0]
    dirAndSteps = currentLine.split()
    dir = dirAndSteps[0]
    steps = int(dirAndSteps[1])
    for i in range(steps):
        if dir == "U":
            pos[0] -= 1
            verticalDirs[keyFromPos(pos)] = "U"
            if i == steps - 1:
                if nextDir == "L":
                    horizontalDirs[keyFromPos(pos)] = "L"
                elif nextDir == "R":
                    horizontalDirs[keyFromPos(pos)] = "R"
        elif dir == "D":
            pos[0] += 1
            verticalDirs[keyFromPos(pos)] = "D"
            if i == steps - 1:
                if nextDir == "L":
                    horizontalDirs[keyFromPos(pos)] = "L"
                elif nextDir == "R":
                    horizontalDirs[keyFromPos(pos)] = "R"
        elif dir == "L":
            pos[1] -= 1
            horizontalDirs[keyFromPos(pos)] = "L"
            if i == steps - 1:
                if nextDir == "U":
                    verticalDirs[keyFromPos(pos)] = "U"
                elif nextDir == "D":
                    verticalDirs[keyFromPos(pos)] = "D"
        elif dir == "R":
            pos[1] += 1
            horizontalDirs[keyFromPos(pos)] = "R"
            if i == steps - 1:
                if nextDir == "U":
                    verticalDirs[keyFromPos(pos)] = "U"
                elif nextDir == "D":
                    verticalDirs[keyFromPos(pos)] = "D"
        trenches[pos[0]][pos[1]] = "#"


for i in range(len(trenches)):
    currentHorizontal = 0
    formerDir = ""
    for j in range(len(trenches[0])):
        if verticalDirs.get(keyFromPos([i, j])) == "U":
            if formerDir != "U":
                currentHorizontal += 1
                formerDir = "U"
        elif verticalDirs.get(keyFromPos([i, j])) == "D":
            if formerDir != "D":
                currentHorizontal -= 1
                formerDir = "D"
        if trenches[i][j] == ".":
            if currentHorizontal != 0:
                trenches[i][j] = "#"

totalDug = 0
for i in range(len(trenches)):
    for j in range(len(trenches[0])):
        if trenches[i][j] == "#":
            totalDug += 1

print(totalDug)

# write to file
file = open("output.txt", "w")
for i in range(len(trenches)):
    file.write("".join(trenches[i]) + "\n")


        

    