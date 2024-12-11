import copy

file = open("input.txt", "r")
lines = file.readlines()
file.close()

bricks = []

for line in lines:
    line = line.strip()
    firstPositions = line.split("~")[0].split(",")
    secondPositions = line.split("~")[1].split(",")
    bricks.append([int(firstPositions[0]), int(firstPositions[1]), int(firstPositions[2]), 
                   int(secondPositions[0]), int(secondPositions[1]), int(secondPositions[2])])



def overlappingBricks(brick1, brick2):
    if brick1[0] > brick2[3] or brick1[3] < brick2[0]:
        return False
    if brick1[1] > brick2[4] or brick1[4] < brick2[1]:
        return False
    return True

# sort bricks by bottom z
bricks.sort(key=lambda x: x[2])

# let bricks fall into place
placedBricks = []
for brick in bricks: 
    lowestPossibleZ = 1
    for placedBrick in placedBricks:
        if overlappingBricks(brick, placedBrick):
            if placedBrick[5] + 1 > lowestPossibleZ:
                lowestPossibleZ = placedBrick[5] + 1
    newBrick = [brick[0], brick[1], lowestPossibleZ, brick[3], brick[4], brick[5] - brick[2] + lowestPossibleZ]
    placedBricks.append(newBrick)

def brickToKey(brick):
    return str(brick[0]) + "," + str(brick[1]) + "," + str(brick[2]) + "," + str(brick[3]) + "," + str(brick[4]) + "," + str(brick[5])

def investigatedToKey(brickKeys):
    listOfKeys = list(brickKeys)
    listOfKeys.sort()
    return ",".join(listOfKeys)

def findFallingBricks(brick, placedBricks, currentlyAlsoFalling):
    brickKey = brickToKey(brick)
    otherBricksPotentiallySupporting = []
    for j in range(len(placedBricks)):
        otherBrick = placedBricks[j]
        otherBrickKey = brickToKey(otherBrick)
        if otherBrickKey == brickKey:
            continue
        if otherBrick[5] == brick[5] and currentlyAlsoFalling.get(brickToKey(otherBrick)) is None:
            otherBricksPotentiallySupporting.append(otherBrick)

    supportedBricks = []
    for j in range(len(placedBricks)):
        potentiallySupportedBrick = placedBricks[j]
        key = brickToKey(potentiallySupportedBrick)
        if key == brickKey:
            continue
        if potentiallySupportedBrick[2] == brick[5] + 1 and overlappingBricks(brick, potentiallySupportedBrick):
            supportedBricks.append(potentiallySupportedBrick)

    fallingBricks = []
    for supBrick in supportedBricks:
        otherSupport = False
        for otherBrick in otherBricksPotentiallySupporting:
            if overlappingBricks(supBrick, otherBrick):
                otherSupport = True
                break
        if not otherSupport:
            fallingBricks.append(supBrick)
    return fallingBricks



# part 1
numberOfPossibleToDisintegrate = 0
for i in range(len(placedBricks)):
    brick = placedBricks[i]
    fallingBricks = findFallingBricks(brick, placedBricks, {})
    if len(fallingBricks) == 0:
        numberOfPossibleToDisintegrate += 1
    if i % 50 == 0:
        print(i*50/len(placedBricks), "%")

# part 2
totalNumberOfFallingBricks = 0
savedResults = {}
for i in range(len(placedBricks) - 1, -1, -1):
    currentlyFallingOnLevel = {}
    fallingBrickMap = {}

    brick = placedBricks[i]
    brickKey = brickToKey(brick)
    fallingBricks = findFallingBricks(brick, placedBricks, {})
    savedResults[investigatedToKey([brickKey])] = copy.deepcopy(fallingBricks)

    level = brick[5]
    currentlyFallingOnLevel[level] = {brickKey: True}

    while len(fallingBricks) > 0:
        fallingBrick = fallingBricks.pop(0)
        level = fallingBrick[5]
        fallingBrickKey = brickToKey(fallingBrick)
        if currentlyFallingOnLevel.get(level) is None:
            currentlyFallingOnLevel[level] = {fallingBrickKey: True}
        else:
            currentlyFallingOnLevel[level][fallingBrickKey] = True
        fallingBrickMap[fallingBrickKey] = True
        investigatedKey = investigatedToKey(currentlyFallingOnLevel[level].keys())
        if investigatedKey in savedResults:
            fallingBricks += savedResults[investigatedKey]
        else:
            currentFallingBricks = findFallingBricks(fallingBrick, placedBricks, currentlyFallingOnLevel[level])
            fallingBricks += currentFallingBricks
            savedResults[investigatedKey] = copy.deepcopy(currentFallingBricks)
    if i % 50 == 0:
        print((len(placedBricks) - i)*50/len(placedBricks) + 50, "%")
    totalNumberOfFallingBricks += len(fallingBrickMap.keys())

print("Part 1", numberOfPossibleToDisintegrate)
print("Part 2", totalNumberOfFallingBricks)
