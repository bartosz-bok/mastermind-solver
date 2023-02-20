from pawns import Table, Color


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

        while chosen_player != 'human':
            chosen_player = input('this is not human! choose another player: ')

        if chosen_player == 'human':
            self.show_pawns = input('print answer (yes/no): ')

            while self.show_pawns != 'yes' and self.show_pawns != 'no':
                self.show_pawns = input('print answer (yes/no): ')

            if self.show_pawns == 'yes':
                self.show_pawns = True
            elif self.show_pawns == 'no':
                self.show_pawns = False

        self.player = chosen_player

    def prepare_game(self):
        self.table = Table(self.NUMBER_OF_PAWNS, self.color.return_colors())

        if self.player == 'human':
            self.table.select_random_pawns_colors()

            if self.show_pawns:
                self.table.print_pawns()

        # TODO ogarnąć
        elif self.player == 'computer':
            self.table.select_random_pawns_colors()

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


class ComputerPlayer(Game):
    def __init__(self):
        super().__init__()
