input = open('./Calendar/December 6th/input.txt', 'r')

lines = input.readlines()
first_line = lines[0].strip()
for i, char in enumerate(first_line):
    if i > 13 and len(set(first_line[i-13:i+1])) == 14:
        print(char, i + 1)
        break