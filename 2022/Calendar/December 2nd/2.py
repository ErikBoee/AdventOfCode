input = open('./Calendar/December 2nd/input.txt', 'r')
pairsToScore = {
    'A X': 4,
    'B X': 1,
    'C X': 7,
    'A Y': 8,
    'B Y': 5,
    'C Y': 2,
    'A Z': 3,
    'B Z': 9,
    'C Z': 6,
}
flipPairs = {
    'A X': 'A Z',
    'B X': 'B X',
    'C X': 'C Y',
    'A Y': 'A X',
    'B Y': 'B Y',
    'C Y': 'C Z',
    'A Z': 'A Y',
    'B Z': 'B Z',
    'C Z': 'C X',
}
lines = input.readlines();
original_score = sum([pairsToScore[line.strip()] for line in lines])
print(original_score)
flipped_score = sum([pairsToScore[flipPairs[line.strip()]] for line in lines])
print(flipped_score)