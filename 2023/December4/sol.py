file = open("input.txt", "r")
lines = file.readlines()
file.close()

sum_of_winning_games = 0
sum_of_cards = 0
line_number = 0
line_number_to_number_of_cards = {}
for i in range(len(lines)):
    line_number_to_number_of_cards[i] = 1
for line in lines:

    line = line.strip()
    games_string = line.split(":")[1]
    games = games_string.split("|")
    first_games = games[0].split(" ")
    second_games = games[1].split(" ")
    number_of_winning_games = 0
    winning_numbers_dict = {}
    for game in first_games:
        if game != "":
            winning_numbers_dict[game] = True
    for game in second_games:
        if game in winning_numbers_dict:
            number_of_winning_games += 1
    sum_of_winning_games += 0 if number_of_winning_games == 0 else 2 ** (number_of_winning_games - 1)
    number_of_cards_on_step = line_number_to_number_of_cards[line_number]
    for temp_line_number in range(line_number + 1, line_number + 1 + number_of_winning_games):
        line_number_to_number_of_cards[temp_line_number] += number_of_cards_on_step
    sum_of_cards += line_number_to_number_of_cards[line_number]
    line_number += 1

print(sum_of_winning_games)
print(sum_of_cards)