def put_ship_on_the_board(self, ship):
    """
    :param ship:
    :return:
    """
    self.print_field()
    print('You need to add {}-deck ship\n'.format(ship.number_of_decks))

    entered_decks = 1
    while entered_decks <= ship.number_of_decks:
        try:
            position = Field.get_position(entered_decks)

            if not self.check_position(position, ship.coords):
                raise KeyError('The deck is too close to the another ship!')

            # We need to determine a direction of the ship here
            if entered_decks == 2:
                difference = fabs(ship.coords[0] - position)
                if difference == 1:
                    ship.__horizontal__ = True
                elif difference == 10:
                    ship.__horizontal__ = False
                else:
                    raise KeyError('Wrong position for the deck!')
            # check possibilty of putting a deck here
            elif entered_decks > 2:
                difference = fabs(ship.coords[entered_decks - 2] - position)
                if ship.__horizontal__:
                    difference *= 10
                if not (difference >= 10 and difference <= 30):
                    raise KeyError('You chose wrong direction for your ship!')

            # check free space

            self[position] = 'O'
            ship.coords.append(position)
            entered_decks += 1
        except KeyError as e:
            print(e)
        except ValueError:
            print('You entered invalid coords!')


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
            checklist = [w for w in start_checklist1
                         if not w in coords]  # addtional filter
            for i in checklist:
                if self[i] == 'O':
                    return False

        return True

    def get_position(number_of_deck):
        coords = input('Enter coords of {}th deck '.format(number_of_deck))
        if len(coords) == 2:
            row = (int(coords[1]) - 1) * 10
            col = DICT_OF_COORDS[coords[0]]
            return row + col
        elif len(coords) == 3:
            row = (int(coords[1] + coords[2]) - 1) * 10
            col = DICT_OF_COORDS[coords[0]]
            return row + col