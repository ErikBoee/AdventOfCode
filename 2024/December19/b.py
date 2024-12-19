from a import *

knownPatternsToNumberOfWays = {}

def numberOfWaysToMakePattern(pattern, buildingBlocks):
    if len(pattern) == 0:
        return 1
    if  pattern in knownPatternsToNumberOfWays:
        return knownPatternsToNumberOfWays[pattern]
    numberOfWays = 0
    for i in range(1, longestBuildingBlock + 1):
        possibleBuildingBlocks = charsToBuildingBlocks[i]
        if pattern[:i] in possibleBuildingBlocks:
            numberOfWays += numberOfWaysToMakePattern(pattern[i:], buildingBlocks)
    knownPatternsToNumberOfWays[pattern] = numberOfWays
    return numberOfWays

totalNumberOfWaysToMakePattern = 0
for pattern in patterns:
    numberOfWays = numberOfWaysToMakePattern(pattern, charsToBuildingBlocks)
    totalNumberOfWaysToMakePattern += numberOfWays

print(totalNumberOfWaysToMakePattern)