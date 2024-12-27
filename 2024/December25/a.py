file = open("input.txt", "r")
lines = file.readlines()
file.close()


keys = []
currentKey = [0, 0, 0, 0, 0]
locks = []
currentLock = [0, 0, 0, 0, 0]

rowInPattern = 0
currentlyLookingAtKey = True
for line in lines:
    if line.strip() == "":
        if currentlyLookingAtKey:
            keys.append(currentKey)
        else:
            locks.append(currentLock)
        currentLock = [0, 0, 0, 0, 0]
        currentKey = [0, 0, 0, 0, 0]
        rowInPattern = 0
        continue
    if rowInPattern == 0:
        if line.strip() == "#####":
            currentlyLookingAtKey = False
        else:
            currentlyLookingAtKey = True
    for i in range(5):
        char = line[i]
        if char == "#":
            if currentlyLookingAtKey:
                currentKey[i] += 1
            else:
                currentLock[i] += 1
    rowInPattern += 1

if currentlyLookingAtKey:
    keys.append(currentKey)
else:
    locks.append(currentLock)

print(len(keys), len(locks))

numberOfLockKeyPairsThatFitTogether = 0
for key in keys:
    for lock in locks:
        fitTogether = True
        for i in range(5):
            if key[i] + lock[i] > 7:
                fitTogether = False
                break
        if fitTogether:
            numberOfLockKeyPairsThatFitTogether += 1
print(numberOfLockKeyPairsThatFitTogether)