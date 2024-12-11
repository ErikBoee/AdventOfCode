file = open("input.txt", "r")
lines = file.readlines()
file.close()


leftListNumbers = []
rightListNumbers = []
for line in lines:
    line = line.strip()
    print(line.split(" "))
    leftListNumbers.append(int(line.split("   ")[0]))
    rightListNumbers.append(int(line.split("   ")[1]))

sortedLeftListNumbers = sorted(leftListNumbers)
sortedRightListNumbers = sorted(rightListNumbers)

diffList = []
for i in range(len(sortedLeftListNumbers)):
    diffList.append(abs(sortedRightListNumbers[i] - sortedLeftListNumbers[i]))

totalDiff = sum(diffList)

print(totalDiff)


occurrencesInRightList = {}
for number in rightListNumbers:
    if number in occurrencesInRightList:
        occurrencesInRightList[number] += 1
    else:
        occurrencesInRightList[number] = 1

similarityScore = 0
for number in leftListNumbers:
    if number in occurrencesInRightList and occurrencesInRightList[number] > 0:
        similarityScore += occurrencesInRightList[number]*number

print(similarityScore)