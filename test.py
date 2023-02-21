import itertools
x = [0, 1, 2]

possible_combinations = [p for p in itertools.product(x, repeat=4)]

# print(combinations)

previous_guessed_combination = [0,1,2,1]

answer = ['black','black',None,None]

answer_black = answer.count('black')
answer_white = answer.count('white')

def check_black(guessed_combination,answer_black):

    correct_black = []

    for combination_i in possible_combinations:
        count = 0
        for idx,value_i in enumerate(combination_i):
            if value_i == guessed_combination[idx]:
                count += 1

        if count == answer_black:
            correct_black.append(combination_i)

    return correct_black

print(check_black(previous_guessed_combination,answer_black))

print(len(check_black(previous_guessed_combination,answer_black))/len(possible_combinations))