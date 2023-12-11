from copy import deepcopy
import numpy as np
input = open('./Calendar/December 9th/input.txt', 'r')

lines = input.readlines()

T = [0,0]
H = [0,0]
T_positions = set()
T_positions.add((0,0))
for line in lines:
    stripped_line = line.strip()
    directionandnumber = stripped_line.split(' ')
    direction = directionandnumber[0]
    number = int(directionandnumber[1])
    if direction == 'R':
        for i in range(number):
            H[0] += 1
            if abs(H[0] - T[0]) > 1:
                T[0] += 1
                T[1] = H[1]
                T_positions.add((T[0], T[1]))
    elif direction == 'L':
        for i in range(number):
            H[0] -= 1
            if abs(H[0] - T[0]) > 1:
                T[0] -= 1
                T[1] = H[1]
                T_positions.add((T[0], T[1]))
    elif direction == 'U':
        for i in range(number):
            H[1] += 1
            if abs(H[1] - T[1]) > 1:
                T[1] += 1
                T[0] = H[0]
                T_positions.add((T[0], T[1]))
    elif direction == 'D':
        for i in range(number):
            H[1] -= 1
            if abs(H[1] - T[1]) > 1:
                T[1] -= 1
                T[0] = H[0]
                T_positions.add((T[0], T[1]))
print(len(T_positions))


def move_positions(positions, T_positions):
    for k in range(1, 10):
        if positions[k][0] - positions[k-1][0] > 1:
            if abs(positions[k-1][1] - positions[k][1]) <=1:
                positions[k] = (positions[k-1][0] + 1, positions[k-1][1])
            elif positions[k-1][1] - positions[k][1] > 1:
                positions[k] = (positions[k-1][0] + 1, positions[k-1][1] - 1)
            else:
                positions[k] = (positions[k-1][0] + 1, positions[k-1][1] + 1)
            if k == 9:
                T_positions.add((positions[k]))
        elif positions[k-1][0] - positions[k][0] > 1:
            if abs(positions[k-1][1] - positions[k][1]) <=1:
                positions[k] = (positions[k-1][0] - 1, positions[k-1][1])
            elif positions[k-1][1] - positions[k][1] > 1:
                positions[k] = (positions[k-1][0] - 1, positions[k-1][1] - 1)
            else:
                positions[k] = (positions[k-1][0] - 1, positions[k-1][1] + 1)
            if k == 9:
                T_positions.add((positions[k]))
        elif positions[k][1] - positions[k-1][1] > 1:
            if abs(positions[k-1][0] - positions[k][0]) <=1:
                positions[k] = (positions[k-1][0], positions[k-1][1] + 1)
            elif positions[k-1][0] - positions[k][0] > 1:
                positions[k] = (positions[k-1][0] - 1, positions[k-1][1] + 1)
            else:
                positions[k] = (positions[k-1][0] + 1, positions[k-1][1] + 1)
            if k == 9:
                T_positions.add((positions[k]))
        elif positions[k-1][1] - positions[k][1] > 1:
            if abs(positions[k-1][0] - positions[k][0]) <=1:
                positions[k] = (positions[k-1][0], positions[k-1][1] - 1)
            elif positions[k-1][0] - positions[k][0] > 1:
                positions[k] = (positions[k-1][0] - 1, positions[k-1][1] - 1)
            else:
                positions[k] = (positions[k-1][0] + 1, positions[k-1][1] - 1)
            if k == 9:
                T_positions.add((positions[k]))
        # Vizualize the positions
        """
        if k==9:
            matrix = np.zeros((10,10))
            max_row = max([positions[0] for positions in positions])
            min_row = min([positions[0] for positions in positions])
            max_col = max([positions[1] for positions in positions])
            min_col = min([positions[1] for positions in positions])
            temp_positions = deepcopy(positions)
            normalize_row = 0
            if abs(max_row) > abs(min_row):
                normalize_row = max_row - 9
            else:
                normalize_row = min_row
            if abs(max_col) > abs(min_col):
                normalize_col = max_col - 9
            else:
                normalize_col = min_col 
            for i in range(10):
                temp_positions[i] = (positions[i][0] - normalize_row, positions[i][1] - normalize_col)
            for i, pos in enumerate(temp_positions):
                matrix[pos[0]][pos[1]] = i + 1
        """

    return positions, T_positions



positions = [(0,0)]*10
T_positions = set()
T_positions.add((0,0))
for i, line in enumerate(lines):
    stripped_line = line.strip()
    directionandnumber = stripped_line.split(' ')
    direction = directionandnumber[0]
    number = int(directionandnumber[1])
    if direction == 'D':
        for _ in range(number):
            positions[0] = (positions[0][0] + 1, positions[0][1])
            positions, T_positions = move_positions(positions, T_positions)
                    
    elif direction == 'U':
        for i in range(number):
            positions[0] = (positions[0][0] - 1, positions[0][1])
            positions, T_positions = move_positions(positions, T_positions)
            
    elif direction == 'R':
        for i in range(number):
            positions[0] = (positions[0][0], positions[0][1] + 1)
            positions, T_positions = move_positions(positions, T_positions)

    elif direction == 'L':
        for i in range(number):
            positions[0] = (positions[0][0], positions[0][1] - 1)
            positions, T_positions = move_positions(positions, T_positions)

print(len(T_positions))