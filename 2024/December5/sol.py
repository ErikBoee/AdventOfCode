
file = open("input.txt", "r")
lines = file.readlines()
file.close()

numberToNumbersAfter = {}

splitIndex = 0
for i in range(0, len(lines)):
    line = lines[i]
    line = line.strip()
    numbers = line.split("|")
    if len(numbers) != 2:
        splitIndex = i
        break
    numberBefore = int(numbers[0])
    numberAfter = int(numbers[1])
    if numberBefore in numberToNumbersAfter:
        numberToNumbersAfter[numberBefore].append(numberAfter)
    else:
        numberToNumbersAfter[numberBefore] = [numberAfter]

def numberIsApproved(number, alreadyChecked):
    if number not in numberToNumbersAfter:
        return True
    numbersThatShouldBeAfter = numberToNumbersAfter[number]
    numberApproved = True
    for numberThatShouldBeAfter in numbersThatShouldBeAfter:
        if numberThatShouldBeAfter in alreadyChecked:
            numberApproved = False
            break
    return numberApproved

middleNumberSumPart1 = 0
for i in range(splitIndex + 1, len(lines)):
    line = lines[i]
    line = line.strip()
    numbers = line.split(",")
    middleNumber = int(numbers[len(numbers)//2])
    isApproved = True
    alreadyChecked = {}
    for number in numbers:
        number = int(number)
        numberApproved = numberIsApproved(number, alreadyChecked)
        if not numberApproved:
            isApproved = False
            break
        alreadyChecked[number] = True
    if isApproved:
        middleNumberSumPart1 += middleNumber

print(middleNumberSumPart1)

                
def numberToSwap(number, alreadyChecked):
    if number not in numberToNumbersAfter:
        return [-1, -1]
    numbersThatShouldBeAfter = numberToNumbersAfter[number]
    for numberThatShouldBeAfter in numbersThatShouldBeAfter:
        if numberThatShouldBeAfter in alreadyChecked:
            index = alreadyChecked[numberThatShouldBeAfter]
            return index, numberThatShouldBeAfter
    return [-1, -1]


middleNumberSum = 0
for i in range(splitIndex + 1, len(lines)):
    line = lines[i]
    line = line.strip()
    numbers = line.split(",")
    anyNumberSwapped = True
    k = 0
    while anyNumberSwapped:
        anyNumberSwapped = False
        alreadyChecked = {}
        for i in range(len(numbers)):
            number = numbers[i]
            number = int(number)
            numberToSwapWith = numberToSwap(number, alreadyChecked)
            index = numberToSwapWith[0]
            swapNumber = numberToSwapWith[1]
            if index != -1:
                numbers[index] = numbers[i]
                numbers[i] = swapNumber
                alreadyChecked[swapNumber] = i
                alreadyChecked[number] = index
                anyNumberSwapped = True
            else:
                alreadyChecked[number] = i
        k += 1
    anyIncorrect = k > 1
    if anyIncorrect:
        middleNumber = int(numbers[len(numbers)//2])
        middleNumberSum += middleNumber

print(middleNumberSum)