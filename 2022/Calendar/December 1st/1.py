input = open('./Calendar/December 1st/input.txt', 'r')
top_three = [0,0,0]
current_value = 0
for line in input.readlines():
    if line != '\n':
        current_value += int(line.strip())
    else:
        if current_value > min(top_three):
            top_three[top_three.index(min(top_three))] = current_value
        current_value = 0

print(max(top_three))
print(sum(top_three))
print(top_three)

input = open('./Calendar/December 1st/input.txt', 'r')
max_value = 0
current_value = 0
for line in input.readlines():
    if line != '\n':
        current_value += int(line.strip())
    else:
        if current_value > max_value:
            max_value = current_value
        current_value = 0

print(max_value)
