import itertools

x = [0, 1, 2]

possible_combinations = [p for p in itertools.product(x, repeat=4)]

# print(combinations)

previous_guessed_combination = [0, 1, 2, 1]

answer = ['black', 'black', None, None]

NUMBER_OF_BLACK = answer.count('black')
NUMBER_OF_WHITE = answer.count('white')


def check_answer(guessed_combination, answer_black, answer_white, possible_numbers):
    correct_combinations = []

    for combination_i in possible_combinations:
        combination_i = list(combination_i)
        count_black = 0
        count_white = 0

        for idx, value_i in enumerate(combination_i):
            if value_i == guessed_combination[idx]:
                count_black += 1

        if count_black == answer_black:
            indexes = []
            guessed_combinations_copy = guessed_combination.copy()
            combination_i_copy = combination_i.copy()
            for idx, value_i in enumerate(combination_i):
                if value_i == guessed_combination[idx]:
                    indexes.append(idx)

            pops = 0
            for index_i in indexes:
                combination_i_copy.pop(index_i - pops)
                guessed_combinations_copy.pop(index_i - pops)
                pops +=1

            for possible_number_i in possible_numbers:
                count_white += min(guessed_combinations_copy.count(possible_number_i),
                                   combination_i_copy.count(possible_number_i))

            if count_white == answer_white:
                correct_combinations.append(combination_i)

    return correct_combinations


print(check_answer(previous_guessed_combination, NUMBER_OF_BLACK, NUMBER_OF_WHITE, x))

print(len(check_answer(previous_guessed_combination, NUMBER_OF_BLACK, NUMBER_OF_WHITE, x)) / len(possible_combinations))
