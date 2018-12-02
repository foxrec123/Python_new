import random

EMPTY_MARK = 'X'

MOVES = {
    'w': -4,
    'd':  1,
    's':  4,
    'a': -1
}

def create_field():

    """
    creates and shuffles new field
    :return: created field
    """

    field = list(range(1, 17))
    random.shuffle(field)
    field[-1] = EMPTY_MARK

    appropriate_move = 0
    while appropriate_move <= 100:
        try:
            move = random.choice(list(MOVES.keys()))
            perform_move(field, move)
            appropriate_move += 1
        except IndexError:
            continue

    return field


def print_field(field):

    """
    This function prints field
    :param field:
    :return: None
    """

    for i in range(0, 16, 4):
        print(field[i:i + 4])
    print('\n')


def get_users_move():
    while True:
        user_move = input('Please, input your move: ')
        if user_move in MOVES.keys():
            return user_move


def perform_move(field, move):

    """
    This function performs taken move
    :param field, move
    :return: nothing
    """

    old_position = field.index(EMPTY_MARK)


    if move == 'w' and old_position <= 3:
        raise IndexError('Cannot move up')
    if move == 's' and old_position >= 12:
        raise IndexError('Cannot move down')
    if move == 'a' and old_position % 4 == 0:
        raise IndexError('Cannot move left')
    if move == 'd' and (old_position + 1) % 4 == 0:
        raise  IndexError('Cannot move right')

    new_position = old_position + MOVES[move]
    field[new_position], field[old_position] = field[old_position], field[new_position]


def is_game_finished(field):

    """
    Checks end of the game
    :param field:
    :return: flag of the end of the game
    """

    etalon = [i for i in range(1, 16)]
    etalon.append(EMPTY_MARK)

    return etalon == field

def main():

    """
    The main function
    :return:
    """
    field = create_field()
    print_field(field)

    while not is_game_finished(field):
        try:
            shift = get_users_move()
            perform_move(field, shift)
            print_field(field)
        except IndexError as e:
            print(e)
    print('The game is finished!')

if __name__ == '__main__':
    main()