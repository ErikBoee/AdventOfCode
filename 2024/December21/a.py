
numericPadPositions = [
    { "key": "7", "pos": [0, 0] },
    { "key": "8", "pos": [1, 0] },
    { "key": "9", "pos": [2, 0] },
    { "key": "4", "pos": [0, 1] },
    { "key": "5", "pos": [1, 1] },
    { "key": "6", "pos": [2, 1] },
    { "key": "1", "pos": [0, 2] },
    { "key": "2", "pos": [1, 2] },
    { "key": "3", "pos": [2, 2] },
    { "key": "0", "pos": [1, 3] },
    { "key": "A", "pos": [2, 3] },
]

navigatorPadPositions = [
    { "key": "A", "pos": [1, 0] },
    { "key": "^", "pos": [0, 0] },
    { "key": "v", "pos": [0, 1] },
    { "key": ">", "pos": [1, 1] },
    { "key": "<", "pos": [-1, 1] },
]

navigatorPriority = {
    ">": -1,
    "<": 2,
    "v": 1,
    "^": 0,
}

def priorityConcat(seqX, seqY):
    if len(seqX) == 0:
        return seqY
    if len(seqY) == 0:
        return seqX
    if navigatorPriority[seqX[0]] > navigatorPriority[seqY[0]]:
        return seqX + seqY
    return seqY + seqX

def pairPathsFromMap(padPositions, isNavigator=False):
    keyToSequence = {}
    for i in range(len(padPositions)):
        for j in range(i + 1, len(padPositions)):
            seqij=""
            seqji=""
            seqijX=""
            seqjiX=""
            seqijY=""
            seqjiY=""
            if padPositions[i]["pos"][0] > padPositions[j]["pos"][0]:
                diff = padPositions[i]["pos"][0] - padPositions[j]["pos"][0]
                seqijX = "<" * diff
                seqjiX = ">" * diff
            elif padPositions[i]["pos"][0] < padPositions[j]["pos"][0]:
                diff = padPositions[j]["pos"][0] - padPositions[i]["pos"][0]
                seqijX = ">" * diff
                seqjiX = "<" * diff
            if padPositions[i]["pos"][1] > padPositions[j]["pos"][1]:
                diff = padPositions[i]["pos"][1] - padPositions[j]["pos"][1]
                seqijY = "^" * diff
                seqjiY = "v" * diff
            elif padPositions[i]["pos"][1] < padPositions[j]["pos"][1]:
                diff = padPositions[j]["pos"][1] - padPositions[i]["pos"][1]
                seqijY = "v" * diff
                seqjiY = "^" * diff
            if not isNavigator:
                if padPositions[j]["key"] == "A" and padPositions[i]["key"] in ["1", "4", "7"]:
                    seqij += seqijX + seqijY
                    seqji += seqjiY + seqjiX
                elif padPositions[i]["key"] == "0" and padPositions[j]["key"] in ["1", "4", "7"]:
                    seqij += seqijX + seqijY
                    seqji += seqjiY + seqjiX
                else:
                    seqij += priorityConcat(seqijX, seqijY)
                    seqji += priorityConcat(seqjiY, seqjiX)
            else:
                if padPositions[j]["key"] == "<":
                    seqij += seqijY + seqijX
                    seqji += seqjiX + seqjiY
                else:
                    seqij += priorityConcat(seqijX, seqijY)
                    seqji += priorityConcat(seqjiY, seqjiX)

            seqij += "A"
            seqji += "A"
            keyToSequence[padPositions[i]["key"] + "-" + padPositions[j]["key"]] = seqij
            keyToSequence[padPositions[j]["key"] + "-" + padPositions[i]["key"]] = seqji
    return keyToSequence

numericKeyToSequence = pairPathsFromMap(numericPadPositions)
navigatorKeyToSequence = pairPathsFromMap(navigatorPadPositions, True)


def findShortestSequenceForPath(path, keyToSequence):
    totalSequence = ""
    currentLetter = "A"
    for char in path:
        if currentLetter == char:
            totalSequence += "A"
            continue
        key = currentLetter + "-" + char
        sequence = keyToSequence[key]
        totalSequence += sequence
        currentLetter = char
    return totalSequence


file = open("input.txt", "r")
lines = file.readlines()
file.close()

score = 0
for line in lines:
    number = int(line.strip().split("A")[0])
    step = findShortestSequenceForPath(line.strip(), numericKeyToSequence)
    for i in range(2):
        step = findShortestSequenceForPath(step, navigatorKeyToSequence)
    score += len(step) * number

print(score)
