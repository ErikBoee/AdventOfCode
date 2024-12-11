import os

file = open("input.txt", "r")
lines = file.readlines()
file.close()

def add_gear(gears, key, value):
    if key in gears:
        gears[key].append(value)
    else:
        gears[key] = [value]

def char_is_symbol(char):
    return not (char.isdigit() or char == ".")

def checkCurrentNumber(k, i, currentNumber, sum_of_numbers, gears):
     # Look for a symbol that is not a number or . in the surrounding tiles
    minIndex = max(i-len(currentNumber)-1, 0)
    maxIndex = i
    have_registered_number = False
    for j in range(minIndex, maxIndex + 1):
        current_line_approved = char_is_symbol(line[j])
        former_line_approved = k > 0 and char_is_symbol(former_line[j])
        next_line_approved = k < len(lines)-1 and  char_is_symbol(next_line[j])
        if current_line_approved or former_line_approved or next_line_approved:
            if not have_registered_number:
                have_registered_number = True
                sum_of_numbers += int(currentNumber)
            if line[j] == "*":
                add_gear(gears, f"{k},{j}", currentNumber)
            if k > 0 and former_line[j] == "*":
                add_gear(gears, f"{k-1},{j}", currentNumber)
            if k < len(lines) - 1 and next_line[j] == "*":
                add_gear(gears, f"{k+1},{j}", currentNumber)
    return sum_of_numbers

sum_of_numbers = 0
former_line = ""
next_line = ""
gears = {}
for k in range(len(lines)):
    line = lines[k]
    if k != len(lines)-1:
        next_line = lines[k+1]
    currentNumber = ""
    for i in range(len(line)):
        character = line[i]
        if character.isdigit():
            currentNumber += character
        elif currentNumber != "":
            sum_of_numbers = checkCurrentNumber(k, i, currentNumber, sum_of_numbers, gears)
            currentNumber = ""
    if currentNumber != "":
        sum_of_numbers = checkCurrentNumber(k, i, currentNumber, sum_of_numbers, gears)
        currentNumber = ""
    former_line = line

sum_gears = 0
for key in gears:
    if len(gears[key]) == 2:
        product = int(gears[key][0]) * int(gears[key][1])
        sum_gears += product
print("Sum of numbers:", sum_of_numbers)
print("Sum of product of gears:", sum_gears)






