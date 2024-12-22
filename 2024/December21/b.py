from a import *

sequenceAndDepthToTotal = {}
def recursivelyFindShortestSequenceForPath(path, keyToSequence, depth):
    if depth == 0:
        return len(path)
    if path + "-" + str(depth) in sequenceAndDepthToTotal:
        return sequenceAndDepthToTotal[path + "-" +  str(depth)]
    totalSequenceLength = 0
    currentLetter = "A"
    for i in range(len(path)):
        char = path[i]
        if currentLetter == char:
            sequence = "A"
        else:
            key = currentLetter + "-" + char
            sequence = keyToSequence[key]
        currentSequenceContrib = recursivelyFindShortestSequenceForPath(sequence, keyToSequence, depth - 1)
        totalSequenceLength += currentSequenceContrib
        currentLetter = char
    sequenceAndDepthToTotal[path + "-" + str(depth)] = totalSequenceLength
    return totalSequenceLength

score = 0
for line in lines:
    number = int(line.strip().split("A")[0])
    step = findShortestSequenceForPath(line.strip(), numericKeyToSequence)
    sequenceLength = recursivelyFindShortestSequenceForPath(step, navigatorKeyToSequence, 25)
    score += sequenceLength * number
print(score)
