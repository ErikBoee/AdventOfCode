import re

file = open("input.txt", "r")
lines = file.readlines()
file.close()


fullResult = 0

currentlyMultiplying = True
for multipliers in lines:
    matches = re.findall(r"don't\(\)|mul\(\d+,\d+\)|do\(\)", multipliers)
    result = 0
    for match in matches:
        if match == "do()":
            currentlyMultiplying = True
        elif match == "don't()":
            currentlyMultiplying = False
        else:
            numbers = re.findall(r"\d+", match)
            if currentlyMultiplying:
                result += int(numbers[0])*int(numbers[1])
    fullResult += result

print(fullResult)
        