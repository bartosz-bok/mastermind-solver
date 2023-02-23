from pawns import Table, Color

import numpy as np
import pandas as pd
import itertools
import math


def is_number(string):
    return all(char.isdigit() for char in string)


class Game:
    def __init__(self):
        self.color = Color()
        self.player = None
        self.show_pawns = None


class Host(Game):
    def __init__(self):
        super().__init__()
        self.table = None
        self.ComputerPlayer = None
        self.NUMBER_OF_ROUNDS = None
        self.NUMBER_OF_PAWNS = None
        self.NUMBER_OF_COLORS = None

    def choose_color(self):
        while True:
            chosen_color = input('choose color: ')

            while not chosen_color.isalpha():
                chosen_color = input('this word isn\'t alphabetical! choose another color: ')

            if chosen_color == 'stop':
                self.NUMBER_OF_COLORS = len(self.color.colors_list)
                break
            else:
                self.color.add_color(chosen_color)

    def choose_number_of_pawns(self):
        number = input('choose number of pawns: ')

        while not is_number(number):
            number = input('this is not integer! choose another number of pawns: ')

        self.NUMBER_OF_PAWNS = int(number)

    def choose_number_of_rounds(self):
        number = input('choose number of rounds: ')

        while not is_number(number):
            number = input('this is not integer! choose another number of rounds: ')

        self.NUMBER_OF_ROUNDS = int(number)

    def choose_player(self):
        chosen_player = input('choose who is the player: ')

        while chosen_player != 'human' and chosen_player != 'computer':
            chosen_player = input('this is not human or computer! choose another player: ')

        if chosen_player == 'human':
            self.show_pawns = input('print answer (yes/no): ')

            while self.show_pawns != 'yes' and self.show_pawns != 'no':
                self.show_pawns = input('print answer (yes/no): ')

            if self.show_pawns == 'yes':
                self.show_pawns = True
            elif self.show_pawns == 'no':
                self.show_pawns = False
        elif chosen_player == 'computer':
            self.init_computer_player()

        self.player = chosen_player

    def prepare_game(self):
        self.table = Table(self.NUMBER_OF_PAWNS, self.color.return_colors())

        if self.player == 'human':
            self.table.select_random_pawns_colors()

            if self.show_pawns:
                self.table.print_pawns()

        # TODO trzeba ogarnąć?
        elif self.player == 'computer':
            pass

    def play_game(self):
        for round_i in range(self.NUMBER_OF_ROUNDS):

            if self.player == 'human':
                looking_pawns = HumanPlayer.guess_color(round_i, self.NUMBER_OF_PAWNS,
                                                        self.NUMBER_OF_ROUNDS, self.color)

                self.table.check_pawn_list(looking_pawns)

                print(self.table.answers)

                if self.table.answers.count('BLACK!') == self.NUMBER_OF_PAWNS:
                    print('YOU WIN! CONGRATULATIONS!')
                    break

            elif self.player == 'computer':
                answers_pawns = []

                for iter in range(self.NUMBER_OF_PAWNS):
                    guessed_color = input(f'{iter + 1}-th color of pawn:')

                    while guessed_color not in self.color.return_colors():
                        guessed_color = input('There isn\'t that color in game! Choose another: ')

                    answers_pawns.append(guessed_color)

                NUMBER_OF_BLACK = int(input('number of blacks: '))
                NUMBER_OF_WHITE = int(input('number of whites: '))

                self.ComputerPlayer.possible_combinations = self.ComputerPlayer.check_answer(answers_pawns,
                                                                                             NUMBER_OF_BLACK,
                                                                                             NUMBER_OF_WHITE)
                self.ComputerPlayer.entrophy()

                if self.ComputerPlayer.combinations_with_entrophy.sort_values(by='col2', ascending=False).iloc[0][
                    1] > 0:
                    print(
                        f"I suggest you: {self.ComputerPlayer.combinations_with_entrophy.sort_values(by='col2',ascending=False).iloc[0][0]} "
                        f" with entrophy estimator: {self.ComputerPlayer.combinations_with_entrophy.sort_values(by='col2',ascending=False).iloc[0][1]}")
                else:
                    print(f"the answer is: {self.ComputerPlayer.possible_combinations}")
                    exit()

    def init_computer_player(self):
        self.ComputerPlayer = ComputerPlayer(self.NUMBER_OF_PAWNS, self.color.colors_list)


class HumanPlayer:
    def __init__(self):
        pass

    @staticmethod
    def guess_color(round_i, number_of_pawns, number_of_rounds, color):
        looking_pawns = []

        for pawn_i in range(number_of_pawns):

            guessed_color = input(f'round:{round_i + 1}/{number_of_rounds}:'
                                  f'choose {pawn_i + 1}th pawn color: ')

            while guessed_color not in color.return_colors():
                guessed_color = input('There isn\'t that color in game! Choose another: ')

            looking_pawns.append(guessed_color)

        return looking_pawns


class ComputerPlayer:
    def __init__(self, number_of_pawns, colors):
        self.number_of_pawns = number_of_pawns
        self.colors = colors
        self.all_combinations = [p for p in itertools.product(self.colors, repeat=self.number_of_pawns)]
        self.possible_combinations = self.all_combinations
        self.combinations_with_entrophy = None

        possible_answers = ['black', 'white', None]
        comb = list(itertools.combinations_with_replacement(possible_answers, self.number_of_pawns))
        self.possible_answers_combinations = comb[2:]

    def print_initial_possibilities(self):
        print(self.all_combinations)

    def print_all_existing_possibilities(self):
        print(self.possible_combinations)

    def check_answer(self, guessed_combination, answer_black, answer_white):
        correct_combinations = []

        for combination_i in self.possible_combinations:
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

                for possible_number_i in self.colors:
                    count_white += min(guessed_combinations_copy.count(possible_number_i),
                                       combination_i_copy.count(possible_number_i))

                if count_white == answer_white:
                    correct_combinations.append(combination_i)

        return correct_combinations

    def entrophy(self):
        combinations_with_entrophy = pd.DataFrame()

        for iter, possible_pawn_i_combination in enumerate(self.all_combinations):
            possible_pawn_i_combination = list(possible_pawn_i_combination)

            sum_entrophy = 0
            for possible_answers_combination_i in self.possible_answers_combinations:
                possible_answers_combination_i = list(possible_answers_combination_i)
                NUMBER_OF_BLACK = possible_answers_combination_i.count('black')
                NUMBER_OF_WHITE = possible_answers_combination_i.count('white')

                combination = self.check_answer(possible_pawn_i_combination, NUMBER_OF_BLACK, NUMBER_OF_WHITE)
                p = len(combination) / len(self.possible_combinations)
                if 0 < p < 1:
                    sum_entrophy += self.count_entrophy(p)

            d = {'col1': [possible_pawn_i_combination], 'col2': sum_entrophy}
            df = pd.DataFrame(data=d)

            print(f'{iter + 1}/{len(self.all_combinations)}')
            combinations_with_entrophy = pd.concat([combinations_with_entrophy, df])

        self.combinations_with_entrophy = combinations_with_entrophy

    @staticmethod
    def count_entrophy(p):
        return p * math.log2(1 / p)
