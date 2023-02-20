from utils import Host



if __name__ == '__main__':

    print('Yo!\nWelcome to MasterMind game.')

    host = Host()
    host.choose_color()
    host.choose_number_of_pawns()
    host.choose_number_of_rounds()
    host.prepare_game()
    host.play_game()