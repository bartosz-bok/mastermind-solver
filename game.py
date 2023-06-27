from pawns import Table, Color


def is_number(string):
    return all(char.isdigit() for char in string)


class Game:
    def __init__(self):
        self.color = Color()
        self.NUMBER_OF_COLORS = 0
        self.NUMBER_OF_PAWNS = 0
        self.NUMBER_OF_ROUNDS = 0
        pass




class Host(Game):
    def __init__(self):
        super().__init__()
        self.color = Color()

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

    def prepare_game(self):
        self.table = Table(self.NUMBER_OF_PAWNS, self.color.return_colors())
        self.table.select_random_pawns_colors()
        self.table.print_pawns()

    def play_game(self):
        for round_i in range(self.NUMBER_OF_ROUNDS):
            looking_pawns = []
            for pawn_i in range(self.NUMBER_OF_PAWNS):

                guessed_color = input(f'round:{round_i + 1}/{self.NUMBER_OF_ROUNDS}:'
                                      f'choose {pawn_i + 1}th pawn color: ')

                while guessed_color not in self.color.return_colors():
                    guessed_color = input('There isn\'t that color in game! Choose another: ')

                looking_pawns.append(guessed_color)

            self.table.check_pawn_list(looking_pawns)

            print(self.table.answers)
            if self.table.answers.count('Trafione!') == self.NUMBER_OF_PAWNS:
                print('YOU WIN! CONGRATULATIONS!')
                break


class Sharer:
    def __init__(self):
        pass


class Player:
    def __init__(self):
        pass


class ComputerPlayer(Player):
    def __init__(self):
        super().__init__()


class HumanPlayer(Player):
    def __init__(self):
        super().__init__()
