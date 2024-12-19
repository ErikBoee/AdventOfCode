file = open("input.txt", "r")
lines = file.readlines()
file.close()

charsToBuildingBlocks = {}
patterns = []

buildingBlocks = lines[0].strip().split(", ")
for buildingBlock in buildingBlocks:
    if len(buildingBlock) in charsToBuildingBlocks:
        charsToBuildingBlocks[len(buildingBlock)].append(buildingBlock)
    else:
        charsToBuildingBlocks[len(buildingBlock)] = [buildingBlock]

for line in lines[2:]:
    patterns.append(line.strip())

longestBuildingBlock = max(charsToBuildingBlocks.keys())

knownPatternsToCanBeMade = {}

def canMakePattern(pattern, buildingBlocks):
    if len(pattern) == 0:
        return True
    if pattern in knownPatternsToCanBeMade:
        return knownPatternsToCanBeMade[pattern]
    for i in range(1, longestBuildingBlock + 1):
        possibleBuildingBlocks = charsToBuildingBlocks[i]
        if pattern[:i] in possibleBuildingBlocks:
            if canMakePattern(pattern[i:], buildingBlocks):
                knownPatternsToCanBeMade[pattern] = True
                return True
    knownPatternsToCanBeMade[pattern] = False
    return False

numberOfPatternsThatCanBeMade = 0
for pattern in patterns:
    if canMakePattern(pattern, charsToBuildingBlocks):
        numberOfPatternsThatCanBeMade += 1

print(numberOfPatternsThatCanBeMade)