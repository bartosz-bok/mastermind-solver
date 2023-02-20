import random


def find_indices(list_to_check, item_to_find):
    indices = []
    for idx, value in enumerate(list_to_check):
        if value == item_to_find:
            indices.append(idx)
    return indices

class Color:
    def __init__(self):
        self.colors_list = []

    def add_color(self,new_color):
        if new_color in self.colors_list:
            print('given color already exists!')
        else:
            self.colors_list.append(new_color)

    def return_colors(self):
        return self.colors_list

class Table:
    def __init__(self,NUMBER_OF_PAWNS,colors):
        self.NUMBER_OF_PAWNS = NUMBER_OF_PAWNS
        self.NUMBER_OF_COLORS = len(colors)
        self.colors = colors
        self.pawns = []

    def select_random_pawns_colors(self):
        for pawn_i in range(self.NUMBER_OF_PAWNS):
            color_idx = random.randrange(0, self.NUMBER_OF_COLORS, 1)
            self.pawns.append(self.colors[color_idx])

    def print_pawns(self):
        print(self.pawns)

    def check_pawn_list(self,guessed_list):
        self.answers = []
        self.exactly_indexes = []
        self.guessed_try = self.pawns.copy()
        for pawn_index, guessed_pawn in enumerate(guessed_list):
            self.check_exactly_pawn(guessed_pawn,pawn_index)

        guessed_list = [element for idx,element in enumerate(guessed_list) if idx not in self.exactly_indexes]

        for guessed_pawn in guessed_list:
            self.check_not_exactly_pawn(guessed_pawn)

        self.fill_answers()


    def check_exactly_pawn(self,guessed_pawn,pawn_index):
        if guessed_pawn in self.guessed_try:
            color_indexes = find_indices(self.guessed_try, guessed_pawn)
            if pawn_index in color_indexes:
                self.answers.append('BLACK!')
                self.guessed_try[pawn_index] = None
                self.exactly_indexes.append(pawn_index)

    def check_not_exactly_pawn(self,guessed_pawn):
        if guessed_pawn in self.guessed_try:
            self.answers.append('white :)')
            self.guessed_try.remove(guessed_pawn)

    def fill_answers(self):
        for iter in range (self.NUMBER_OF_PAWNS-len(self.answers)):
            self.answers.append(None)

