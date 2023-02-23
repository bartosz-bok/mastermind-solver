import itertools
import random
import math
import pandas as pd

x = [1, 2, 3, 4, 5, 6, 7, 8]

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



def entrophy(possible_pawns_combinations, number_of_pawns, all_possible_combinations):
    combinations_with_entrophy = pd.DataFrame()
    possible_answers = ['black', 'white', None]
    # possible_answers_combinations = [p for p in itertools.product(possible_answers, repeat=number_of_pawns)]

    comb = itertools.combinations_with_replacement(possible_answers, number_of_pawns)
    comb = list(comb)
    possible_answers_combinations = comb[2:]

    for iter, possible_pawn_i_combination in enumerate(all_possible_combinations):
        possible_pawn_i_combination = list(possible_pawn_i_combination)

        sum_entrophy = 0
        for possible_answers_combination_i in possible_answers_combinations:
            possible_answers_combination_i = list(possible_answers_combination_i)
            NUMBER_OF_BLACK = possible_answers_combination_i.count('black')
            NUMBER_OF_WHITE = possible_answers_combination_i.count('white')


            combination = check_answer(possible_pawns_combinations, possible_pawn_i_combination, NUMBER_OF_BLACK, NUMBER_OF_WHITE, x)
            p = len(combination)/len(possible_pawns_combinations)
            if p >0 and p<1:
                sum_entrophy += count_entrophy(p)

        d = {'col1': [possible_pawn_i_combination], 'col2': sum_entrophy}
        df = pd.DataFrame(data=d)
        if (iter+1)%100==0:
            print(f'{iter+1}/{len(all_possible_combinations)}')
        combinations_with_entrophy = pd.concat([combinations_with_entrophy,df])

    return combinations_with_entrophy

def count_entrophy(p):
    return p*math.log2(1/p)

n = int(input('ile pionkow:'))

all_possible_combinations = [p for p in itertools.product(x, repeat=n)]
correct_combinations = all_possible_combinations

while True:

    answers_pawns = []

    for iter in range(n):
        answers_pawns.append(int(input(f'{iter + 1}-ta odpowiedz (pionek):')))

    NUMBER_OF_BLACK = int(input('liczba czarnych: '))
    NUMBER_OF_WHITE = int(input('liczba białych: '))

    correct_combinations = check_answer(correct_combinations, answers_pawns, NUMBER_OF_BLACK, NUMBER_OF_WHITE, x)

    combinations_with_entrophy = entrophy(correct_combinations, n, all_possible_combinations)


    if combinations_with_entrophy.sort_values(by='col2',ascending = False).iloc[0][1] > 0:
        print(f"proponuję: {combinations_with_entrophy.sort_values(by='col2',ascending = False).iloc[0]}")
    else:
        print(f"ostateczna odpowiedź to: {correct_combinations}")

