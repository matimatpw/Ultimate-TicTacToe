from globals import possible_values, possible_players
from errors import (
        InvalidValueError, InvalidPlayerError,
        WrongMoveError, WrongTypeError
    )


class Field:
    """
    Umożliwia identyfikacje oraz zmiany symbolu na danej pozycji.
    :param pos: jest symbolen na tej pozycji.
    :type: str
    """
    def __init__(self) -> None:
        self._pos = '-'

    @property
    def get_pos(self):
        return self._pos

    def update_pos(self, player):
        """Ustawia znak 'X' lub 'O' na danej pozycji"""
        self._pos = player.upper()

    def mark_pos(self, player):
        """Ustawia kolorowy znak na pole"""
        self._pos = player

    def check_empty_move(self):
        """Sprawdza czy dana pozycja jest pusta"""
        if self.get_pos == '-':
            return True
        else:
            return False

    def __str__(self) -> str:
        return self._pos


class Board:
    """Służy do rozegrania rozgrywki na małej planszy.
    Klasa Board zawiera atrybuty:

    :param board: Jest listą list wierszów pozycji
    'obiektów Field()' na małej planszy
    :type: list

    :param finished: określa czy mini plansza jest skończona czy jeszcze nie
    ('Prawda lub Fałsz'), mianowicie czy na planszy można dalej grać
    :type: bool

    :param winner: określa zwycięzce lub remis mini planszy.
    początkowo None, następnie symbol zwyciezcy w przypadku wygranej
    lub 'Draw' w przypadku remisu
    :type: Nonetype, str
    """
    def __init__(self) -> None:
        self._board = [[Field() for _ in range(3)] for x in range(3)]
        self._finished = False
        self._winner = None

    @property
    def winner(self):
        return self._winner

    @property
    def finished(self):
        return self._finished

    @property
    def board(self):
        return self._board

    def get_field(self, row, column):  # -> Field()
        """
        Zwraca obiekt danej pozycji 'FIeld()' zadanej przez
        wiersz i kolumne na mini planszy
        """
        return self._board[row][column]

    def get_move(self, row, col):  # -> str
        """Zwraca symbol na zadanej przez wiersz i kolumne pozycji"""
        return self.get_field(row, col).get_pos

    def set_move(self, row: int, col: int, player):
        """
        Sprawdza czy wiersz i kolumna zostały poprawnie podane.
        Następnie ustawia symbol gracza na danej pozycji.
        """
        if type(row) != int or type(col) != int:
            raise WrongTypeError(row, col)
        if int(row) not in possible_values or int(col) not in possible_values:
            raise InvalidValueError(row, col)
        if player.upper() not in possible_players:
            raise InvalidPlayerError(player)
        if not self.check_correct_move(row, col):
            raise WrongMoveError('Wrong move error!')  # Move is occupied!
        self.get_field(row, col).update_pos(player)

    # AI
    def get_empty_fields(self):  # -> list
        """
        Zwraca liste pustych pozycji na planszy
        """
        empty_positions = []
        for row in range(3):
            for col, pos_field in enumerate(self.board[row]):
                if pos_field.check_empty_move():
                    empty_positions.append((row, col))
        return empty_positions

    def check_correct_move(self, row, col):  # -> bool
        """
        Zwraca 'True' jeśli wybrana pozycja na planszy
        jest pusta w przeciwnym razie (jeśli jest zajeta) zwraca 'False'
        """
        if self.get_field(row, col).check_empty_move():
            return True
        else:
            return False

    def check_correct_board(self):  # -> bool
        """
        Sprawdza czy na planszy można grać dalej.
        Jesli plansza jest skończona to zwraca Fałsz,
        jesli nie to zwraca Prawde
        """
        if self.finished:
            return False
        else:
            return True

    def check_row_win(self, player):  # -> bool
        """
        Sprawdza czy dany gracz 'symbol' wygrał w jakim kolwiek wierszu.
        Zwraca Prawde jeśli wygrał, a Fałsz jeśłi nie.
        """
        for row in range(3):
            tic = self.get_move(row, 0)
            tac = self.get_move(row, 1)
            toe = self.get_move(row, 2)

            if tic == tac == toe == player.upper() != '-':
                return True
        return False

    def check_diagonally_win(self, player):  # -> bool
        """
        Sprawdza czy dany gracz 'symbol' wygrał po ukośie.
        Zwraca Prawde jeśli wygrał, a Fałsz jeśłi nie.
        """
        tic = self.get_move(0, 0)
        tac = self.get_move(1, 1)
        toe = self.get_move(2, 2)

        if tic == tac == toe == player.upper() != '-':
            return True
        else:
            tic = self.get_move(0, 2)
            tac = self.get_move(1, 1)
            toe = self.get_move(2, 0)
            if tic == tac == toe == player.upper() != '-':
                return True
        return False

    def check_column_win(self, player):  # -> bool
        """
        Sprawdza czy dany gracz 'symbol' wygrał w jakiejkolwiek kolumnie.
        Zwraca Prawde jeśli wygrał, a Fałsz jeśłi nie.
        """
        for col in range(3):
            tic = self.get_move(0, col)
            tac = self.get_move(1, col)
            toe = self.get_move(2, col)

            if tic == tac == toe == player.upper() != '-':
                return True
        return False

    def check_board_win(self, player):  # -> bool
        """
        Sprawdza czy plansza została wygrana w jakikolwiek sposób
        przez danego gracza 'symbol'. Jeśli tak to ustawia
        atrybut '._finished' na Prawde, '._winner' na symbol
        wygranego gracza oraz zwraca Prawde. Jeśli nie to zwraca Fałsz.
        """
        win = [
            self.check_row_win(player),
            self.check_column_win(player),
            self.check_diagonally_win(player)]
        if any(win):
            self._finished = True
            self._winner = player.upper()
            return True
        else:
            return False

    def check_board_draw(self):  # -> bool
        """
        Sprawdza czy plansza zakonczyla sie remisem. Mianowicie,
        sprawdza czy na danej planszy istnieje pole puste.
        Jeśli istnieje to zwraca Fałsz, a jesli nie to ustawia
        paramert '._finished' na Prawde, '._winner' na 'Draw' oraz
        zwraca Prawde.
        """
        if len(self.get_empty_fields()) == 0:
            self._finished = True
            self._winner = 'Draw'
            return True
        else:
            return False
