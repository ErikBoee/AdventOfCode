file = open("input.txt", "r")
lines = file.readlines()
file.close()

def unsafeOccurence(currentNumber, formerNumber, increasingSeries, decreasingSeries):
    difference = currentNumber - formerNumber
    return (increasingSeries and (difference <= 0 or difference > 3)) or (decreasingSeries and (difference >= 0 or difference < -3))


def sequenceIsSafe(numbers, usedRemoval):
    increasingSeries = False
    decreasingSeries = False
    formerNumber = int(numbers[0])
    isSafe = False
    for i in range(1, len(numbers)):
        currentNumber = int(numbers[i])
        if i == 1:
            if currentNumber > formerNumber:
                increasingSeries = True
            elif currentNumber < formerNumber:
                decreasingSeries = True
            else:
                if not usedRemoval:
                    return (sequenceIsSafe(numbers[1:], True) or sequenceIsSafe(numbers[0:1] + numbers[2:], True))
                else:
                    return False
        isUnsafeOccurence = unsafeOccurence(currentNumber, formerNumber, increasingSeries, decreasingSeries)
        if isUnsafeOccurence:
            if usedRemoval:
                return False
            if i == len(numbers) - 1:
                # If the last number is removed, the sequence is safe
                return True
            if i == 1:
                return (sequenceIsSafe(numbers[1:], True) or sequenceIsSafe(numbers[0:1] + numbers[2:], True))
            isSafe = sequenceIsSafe(numbers[0:i] + numbers[i+1:], True) or sequenceIsSafe(numbers[0:i-1] + numbers[i:], True) 
            if isSafe:
                return True
            if i == 2:
                # Edge case if the series reverses after the first number
                additionalIsSafe = sequenceIsSafe(numbers[1:], True)
                if additionalIsSafe:
                    return True
            return False
        formerNumber = currentNumber
        if i == len(numbers) - 1:
            isSafe = True
    return isSafe

numberOfSafeSequences = 0
for line in lines:
    line = line.strip()
    numbers = line.split(" ")
    originalIsSafe = sequenceIsSafe(numbers, False)
    if originalIsSafe:
            numberOfSafeSequences += 1
        
print(numberOfSafeSequences)