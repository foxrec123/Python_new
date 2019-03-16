
from math import fabs

DICT_OF_COORDS = {
   'a':0,
   'b':1,
   'c':2,
   'd':3,
   'e':4,
   'f':5,
   'g':6,
   'h':7,
   'i':8,
   'j':9,
}

DICT_OF_DIRECTIONS = {
    'left' : -1,
    'right': 1,
    'up'   : -10,
    'down' : 10,
}

DECK = 'O'

class Player(object):
    def __init__(self):
        self.field = Field()
        self.opponents__field = Field()


class Ship(object):
    def __init__(self, number_of_decks):
        self.number_of_decks = number_of_decks
        self.__horizontal__ = True
        self.coords = []


class Field(list):
    def __init__(self):
        for i in range(0, 100):
            self.append(' ')

    def print_field(self):

        print('      a    b    c    d    e    f    g    h    i    j')
        for i in range(0, 100, 10):
            if i != 90:
                extra_space = ' '
            else:
                extra_space = ''
            print(int((i + 10) / 10), extra_space, self[i: i + 10])
        print('\n')


    @staticmethod
    def get_position(coords):
        if len(coords) == 2:
            row = (int(coords[1]) - 1) * 10
            col = DICT_OF_COORDS[coords[0]]
        elif len(coords) == 3:
            row = (int(coords[1] + coords[2]) - 1) * 10
            col = DICT_OF_COORDS[coords[0]]
        return row, col

    def check_position(self, pos, coords):
        """
        This method checks the position of the deck in order not to put it out of range
        :return: Bool - Possibiity of putting the deck
        """
        # left up corner
        if pos == 0:
            start_checklist = [1, 10, 11]
            checklist = [w for w in start_checklist if not w in coords] #addtional filter
            for i in checklist:
                if self[i] == 'O':
                    return False
        #up line
        elif pos >= 1 and pos <= 8:
            start_checklist = [pos + 1, pos - 1, pos + 9, pos + 10, pos + 11]
            checklist = [w for w in start_checklist if not w in coords]  # addtional filter
            for i in checklist:
                if self[i] == 'O':
                    return False
        #right up corner
        elif pos == 9:
            start_checklist = [8, 18, 19]
            checklist = [w for w in start_checklist if not w in coords]  # addtional filter
            for i in checklist:
                if self[i] == 'O':
                    return False
        #left down corner
        elif pos == 90:
            start_checklist = [80, 81, 91]
            checklist = [w for w in start_checklist if not w in coords]  # addtional filter
            for i in checklist:
                if self[i] == 'O':
                    return False
        #left line
        elif pos % 10 == 0:
            start_checklist = [pos - 10, pos - 9, pos + 1, pos + 11, pos + 10]
            checklist = [w for w in start_checklist if not w in coords]  # addtional filter
            for i in checklist:
                if self[i] == 'O':
                    return False
        #right down corner
        elif pos == 99:
            start_checklist = [98, 88, 89]
            checklist = [w for w in start_checklist if not w in coords]  # addtional filter
            for i in checklist:
                if self[i] == 'O':
                    return False
        #down line
        elif pos >= 91 and pos <= 98:
            start_checklist = [pos - 1, pos - 11, pos - 10, pos - 9, pos + 1]
            checklist = [w for w in start_checklist if not w in coords]  # addtional filter
            for i in checklist:
                if self[i] == 'O':
                    return False
        #right line
        elif pos % 10 == 0:
            start_checklist = [pos - 10, pos - 9, pos + 1, pos + 11, pos + 10]
            checklist = [w for w in start_checklist if not w in coords]  # addtional filter
            for i in checklist:
                if self[i] == 'O':
                    return False
        #right line
        elif (pos - 9) % 10 == 0:
            start_checklist = [pos - 10, pos - 9, pos - 1, pos + 9, pos + 10]
            checklist = [w for w in start_checklist
                         if not w in coords]  # addtional filter
            for i in checklist:
                if self[i] == DECK:
                    return False

        return True

    def put_ship_on_the_board(self, ship):
        """
        :param ship:
        :return:
        """
        self.print_field()
        print('You need to add {}-deck ship'.format(ship.number_of_decks))

        Field_for_check = self.copy()
        while True:
            try:
                coords = input('Enter coords of the first deck (for example a1 or b2) ' \
                               .format(ship.number_of_decks))

                row, col = Field.get_position(coords)
                position = row + col

                if position > 99 or position < 0:
                    raise ValueError

                if ship.number_of_decks > 1:
                    direction = input('Enter direction of the ship (left/right/up/down) ')
                    step = DICT_OF_DIRECTIONS[direction]
                else:
                    step = 0

                next_position = position

                ship_for_check = Ship(ship.number_of_decks)
                for i in range(0, ship.number_of_decks):

                    if i != ship.number_of_decks - 1:
                        next_position += step

                        if next_position > 99 or next_position < 0:
                            raise IndexError('Some parts of the ship are out of range! Try again. col\n!')

                        if (direction == 'left' or direction == 'right') \
                                and next_position // 10 != row / 10:
                            raise IndexError('Some parts of the ship are out of range! Try again. row!\n')

                    if not Field_for_check.check_position(next_position, ship_for_check):
                        print('The deck is too close to the another ship!')
                        raise KeyError

                    ship_for_check.coords.append(position)
                    position += step
                break
            except IndexError as e:
                print(e)
            except: #(KeyError, ValueError):
                print('You entered invalid coords or direction! Try again.\n')

        for deck in ship_for_check.coords:
            self[deck] = DECK
            ship.coords.append(deck)


def main():
    #pass
    f = Field()

    number_of_decks = 4
    while number_of_decks >= 1:
        if number_of_decks == 4:
            f.put_ship_on_the_board(Ship(number_of_decks))
        elif number_of_decks == 3:
            for _ in range(0, 2):
                f.put_ship_on_the_board(Ship(number_of_decks))
        elif number_of_decks == 2:
            for _ in range(0, 3):
                f.put_ship_on_the_board(Ship(number_of_decks))
        elif number_of_decks == 1:
            for _ in range(0, 4):
                f.put_ship_on_the_board(Ship(number_of_decks))

        number_of_decks -= 1

main()