import random

X = 'X'
O = 'O'

EMPTY = ' '

APPROPRIATE_STEPS = tuple(range(1, 10))

def create_board():

    '''
    paints empty board
    :return: created board
    '''

    board = []
    for _ in range(1, 10):
        board.append(EMPTY)

    return board

def print_board(board):

    '''
    prints board
    :return:
    '''

    for i in range(0, 9, 3):
        print(board[i:i + 3])
    print('\n')

def my_step(board):

    '''
    performs human's step
    :param board: current board
    :return:
    '''

    while True:
        try:
            position = int(input('Enter your step (1-9) '))
            if position in APPROPRIATE_STEPS and board[position - 1] == EMPTY:
                board[position - 1] = X
                break
            elif board[position - 1] != EMPTY:
                print('Entered position is not empty. Please, choose a different one.')
        except ValueError:
            print('Entered posttion is incorrect. Try again!')
        except IndexError:
            print('Eneter position is out of index. Try again!')
    print_board(board)


def computer_step(board):

    '''
    performs computer's step
    :param board: current board
    :return:
    '''

    while True:
        random_position = random.choice(range(0, 9))
        if board[random_position] == EMPTY:
            board[random_position] = O
            break
    print_board(board)

def is_game_finished(board):

    '''
    checks the end of the game
    :param board: current board
    :return: flag of finishing the game
    '''

    win_combinations = (
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 4, 8),
        (2, 4, 6),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
    )

    for i in win_combinations:
        if board[i[0]] == board[i[1]] == board[i[2]] and board[i[0]] != EMPTY:
            if board[i[0]] == X:
                print('Human wins!')
            if board[i[0]] == O:
                print('Computer wins!')
            return True

        if EMPTY not in board:
            print('This is draw')
            return True

    return False


def main():
    board = create_board()
    print_board(board)

    while True:
        my_step(board)
        if is_game_finished(board):
            break
        computer_step(board)
        if is_game_finished(board):
            break


if __name__ == '__main__':
    main()