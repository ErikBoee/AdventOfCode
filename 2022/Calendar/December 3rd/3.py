input = open('./Calendar/December 3rd/input.txt', 'r')

lines = input.readlines()
sum_of_chars = 0
for line in lines:
    stripped_line = line.strip()
    part_one = stripped_line[0:len(stripped_line)//2]
    part_two = stripped_line[len(stripped_line)//2:]
    print(part_one, part_two)
    for char in part_one:
        if char in part_two:
            value = ord(char)
            if value >= 97:
                value -= 96
                sum_of_chars += value
            else:
                value -= 38
                sum_of_chars += value
            print(char, value)
            break
print(sum_of_chars)
        
sum_of_chars = 0
linesToCompare = []
for line in lines:
    stripped_line = line.strip()
    linesToCompare.append(stripped_line)
    if len(linesToCompare) == 3:
        for char in linesToCompare[0]:
            if char in linesToCompare[1] and char in linesToCompare[2]:
                value = ord(char)
                if value >= 97:
                    value -= 96
                    sum_of_chars += value
                else:
                    value -= 38
                    sum_of_chars += value
                print(char, value)
                break
        linesToCompare = []
print(sum_of_chars)
