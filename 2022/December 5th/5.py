input = open('./Calendar/December 5th/input.txt', 'r')

lines = input.readlines()

#9000 mover
listsOfStacks = []
reached_break = False
for j, line in enumerate(lines):
    if not reached_break:
        for i, char in enumerate(line):
            if char != '\n':
                if i%4 == 0 and j == 0:
                    listsOfStacks.append([])
                if char == '[':
                    listsOfStacks[i//4].insert(0, line[i+1])
        if line == '\n':
            reached_break = True
    else:
        instructions = line.strip().split(' ')
        moves = int(instructions[1])
        move_from = int(instructions[3])-1
        move_to = int(instructions[5])-1
        for i in range(moves):
            element_to_move = listsOfStacks[move_from].pop()
            listsOfStacks[move_to].append(element_to_move)
print(listsOfStacks)
print(''.join([stack[-1] for stack in listsOfStacks]))

# 9001 mover
listsOfStacks = []
reached_break = False
for j, line in enumerate(lines):
    if not reached_break:
        for i, char in enumerate(line):
            if char != '\n':
                if i%4 == 0 and j == 0:
                    listsOfStacks.append([])
                if char == '[':
                    listsOfStacks[i//4].insert(0, line[i+1])
        if line == '\n':
            reached_break = True
    else:
        instructions = line.strip().split(' ')
        moves = int(instructions[1])
        move_from = int(instructions[3])-1
        move_to = int(instructions[5])-1
        elements_to_move = listsOfStacks[move_from][-moves:]
        del listsOfStacks[move_from][-moves:]
        listsOfStacks[move_to] += elements_to_move
print(listsOfStacks)
print(''.join([stack[-1] for stack in listsOfStacks]))