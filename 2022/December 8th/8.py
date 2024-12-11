import numpy as np
input = open('./Calendar/December 8th/input.txt', 'r')

lines = input.readlines()

tree_matrix = np.zeros((len(lines),len(lines[0].strip())), dtype=int)

for i, line in enumerate(lines):
    stripped_line = line.strip()
    for j, char in enumerate(stripped_line):
        tree_matrix[i, j] = int(char)

num_visible_trees = 0
row, cols = tree_matrix.shape
max_scenic_value = 0
for i in range(row):
    for j in range(cols):
        current_value = tree_matrix[i, j]
        if i == 0 or j == 0 or i == (row-1) or j == (cols - 1):
            num_visible_trees += 1
        else:
            left = max(tree_matrix[:i, j])
            right = max(tree_matrix[i+1:, j])
            above = max(tree_matrix[i, :j])
            below = max(tree_matrix[i, j+1:])
            absolute_min = min(left, right, above, below)
            if absolute_min < current_value:
                num_visible_trees += 1
        scenic_left_value = 0
        k = i
        while k > 0:
            k -= 1
            if k >= 0 and tree_matrix[k, j] < current_value:
                scenic_left_value += 1
            else:
                if k != 0:
                    scenic_left_value += 1
                break
        k = i
        scenic_right_value = 0
        while k < (row -1):
            k += 1
            if k <= (cols - 1) and tree_matrix[k, j] < current_value:
                scenic_right_value += 1
            else:
                if k != (row -1):
                    scenic_right_value += 1
                break
        k = j
        scenic_top_value = 0
        while k > 0:
            k -= 1
            if k >= 0 and tree_matrix[i, k] < current_value:
                scenic_top_value += 1
            else:
                if k != 0:
                   scenic_top_value += 1
                break
        k = j
        sceenic_bottom_value = 0
        while k < (cols -1):
            k += 1
            if k <= (cols -1) and tree_matrix[i, k] < current_value:
                sceenic_bottom_value += 1
            else:
                if k != (cols -1):
                    sceenic_bottom_value += 1
                break
        scenic_value = scenic_top_value*scenic_left_value*sceenic_bottom_value*scenic_right_value
        if scenic_value > max_scenic_value:
            max_scenic_value = scenic_value

print(num_visible_trees)
print(max_scenic_value)
    