input = open('./Calendar/December 4th/input.txt', 'r')

lines = input.readlines()
number_of_pairs_full_overlap = 0
number_of_pairs_some_overlap = 0
for line in lines:
    stripped_line = line.strip()
    pairs = stripped_line.split(',')
    pair_one_extremals = pairs[0].split('-')
    pair_one_min = int(pair_one_extremals[0])
    pair_one_max = int(pair_one_extremals[1])
    pair_two_extremals = pairs[1].split('-')
    pair_two_min = int(pair_two_extremals[0])
    pair_two_max = int(pair_two_extremals[1])
    if pair_one_min <= pair_two_min and pair_one_max >= pair_two_max:
        number_of_pairs_full_overlap += 1
    elif pair_one_min >= pair_two_min and pair_one_max <= pair_two_max:
        number_of_pairs_full_overlap += 1
    if (pair_one_max >= pair_two_min and  pair_one_min <= pair_two_min )or (pair_one_min <= pair_two_max and pair_one_min >= pair_two_min):
        number_of_pairs_some_overlap += 1
print(number_of_pairs_full_overlap)
print(number_of_pairs_some_overlap)


