file = open("input.txt", "r")
lines = file.readlines()
file.close()

stones = lines[0].split(" ")


def trimLeadingZeroes(stone):
    while len(stone) > 1 and stone[0] == "0":
        stone = stone[1:]
    return stone

stoneAndDepthToNumberOfStones = {}

def stoneAndDepthToString(stone, depth):
    return stone + "-" + str(depth)

def stoneToNumberOfStones(stone, depth, maxDepth):
    if depth == maxDepth:
        return 1
    if stoneAndDepthToString(stone, depth) in stoneAndDepthToNumberOfStones:
        return stoneAndDepthToNumberOfStones[stoneAndDepthToString(stone, depth)]
    if stone == "0":
        result = stoneToNumberOfStones("1", depth + 1, maxDepth)
        stoneAndDepthToNumberOfStones[stoneAndDepthToString(stone, depth)] = result
        return result
    elif len(stone)%2 == 0:
        firstHalf = stone[:len(stone)//2]
        secondHalf = trimLeadingZeroes(stone[len(stone)//2:])
        result = stoneToNumberOfStones(firstHalf, depth + 1, maxDepth) + stoneToNumberOfStones(secondHalf, depth + 1, maxDepth)
        stoneAndDepthToNumberOfStones[stoneAndDepthToString(stone, depth)] = result
        return result
    else:
        newStone = str(int(stone)*2024)
        result = stoneToNumberOfStones(newStone, depth + 1, maxDepth)
        stoneAndDepthToNumberOfStones[stoneAndDepthToString(stone, depth)] = result
        return result

def getNumberOfConvertedStones(stones, maxDepth):
    newStones = 0
    for i in range(len(stones)):
        newStones += stoneToNumberOfStones(stones[i], 0, maxDepth)
    return newStones

totalNumberOfStones = getNumberOfConvertedStones(stones, 75)
print(totalNumberOfStones)