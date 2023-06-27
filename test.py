import itertools
import random
import math
import pandas as pd

x = [1, 2, 3, 4, 5, 6, 7, 8]



# print(all_possible_combinations)

previous_guessed_combination = [1, 2, 3, 4]

answer = ['white', None, None, None]

NUMBER_OF_BLACK = answer.count('black')
NUMBER_OF_WHITE = answer.count('white')




def check_answer(possible_combinations, guessed_combination, answer_black, answer_white, possible_numbers):
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

            for idx, value_i in enumerate(combination_i):
                if value_i == guessed_combination[idx]:
                    indexes.append(idx)

            guessed_combinations_copy = guessed_combination.copy()
            combination_i_copy = combination_i.copy()

            pops = 0
            for index_i in indexes:
                combination_i_copy.pop(index_i - pops)
                guessed_combinations_copy.pop(index_i - pops)
                pops += 1

            for possible_number_i in possible_numbers:
                count_white += min(guessed_combinations_copy.count(possible_number_i),
                                   combination_i_copy.count(possible_number_i))

            if count_white == answer_white:
                correct_combinations.append(combination_i)

    return correct_combinations



def entrophy(possible_pawns_combinations, number_of_pawns):
    combinations_with_entrophy = pd.DataFrame()
    possible_answers = ['black', 'white', None]
    possible_answers_combinations = [p for p in itertools.product(possible_answers, repeat=number_of_pawns)]


    for possible_pawn_combination_i in possible_pawns_combinations:

        sum_entrophy = 0
        for possible_answers_combination_i in possible_answers_combinations:
            NUMBER_OF_BLACK = possible_answers_combination_i.count('black')
            NUMBER_OF_WHITE = possible_answers_combination_i.count('white')


            combination = check_answer(possible_pawns_combinations, possible_pawn_combination_i, NUMBER_OF_BLACK, NUMBER_OF_WHITE, x)
            p = len(combination)/len(possible_pawns_combinations)
            sum_entrophy += count_entrophy(p)
        df = pd.DataFrame([possible_pawn_combination_i,sum_entrophy])
        combinations_with_entrophy = pd.concat([combinations_with_entrophy,df])

    return combinations_with_entrophy

def count_entrophy(p):
    return p*math.log2(1/p)


# answer1 = check_answer(all_possible_combinations, previous_guessed_combination, NUMBER_OF_BLACK, NUMBER_OF_WHITE, x)
#
# print(answer1)
#
# print(len(answer1)/len(all_possible_combinations))


n = int(input('ile pionkow:'))

all_possible_combinations = [p for p in itertools.product(x, repeat=n)]
correct_combinations = all_possible_combinations

while True:

    answers_pawns, answers_color = [], []

    for iter in range(n):
        answers_pawns.append(int(input(f'{iter + 1}-ta odpowiedz (pionek):')))


    NUMBER_OF_BLACK = int(input('liczba czarnych: '))
    NUMBER_OF_WHITE = int(input('liczba białych: '))

    correct_combinations = check_answer(correct_combinations, answers_pawns, NUMBER_OF_BLACK, NUMBER_OF_WHITE, x)

    print('możliwe opcje:')
    print(correct_combinations)
    print('ja proponuję: ')
    print(random.choice(correct_combinations))

    print('siema')