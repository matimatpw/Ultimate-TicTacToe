from board import Board
from errors import (
    InvalidBoardError, BoardFinishedError,
    MoveError, BotStartGameError
    )
from globals import possible_boards


class UltimateTicTacToe:
    """Zapewnia możliwość gry w kółko i krzyżyk na sterydach na dużej planszy.
    Klasa UltimateTicTacToe zawiera atrybuty:
    :param ult_boards: zawiera liste małych plansz
    :type ult_boards: list

    :param current_board: Określa plansze na której prowadzona jest w
        danym momencie rozgrywka
    :type current_board: None, Board()

    :param finished_boards: Słuzy do printowania tabelki skonczonych
        plansz '_Board indexing_'.Posiada krotki (numer planszy, zwyciężca
        planszy) początkowo zamiast zwyciezcow jest numer planszy.
    :type finished_boards: list
    """
    def __init__(self):
        self._ult_boards = [Board() for _ in range(9)]
        self._current_board = None  # obiekt
        self._finished_boards = [(x, x) for x in range(9)]  # np. [(2, 'X'),..]

    @property
    def finished_boards(self):
        self._finished_boards.sort()
        return self._finished_boards

    @property
    def ult_boards(self):
        return self._ult_boards

    @property
    def current_board(self):  # -> Board()
        return self._current_board

    def get_index(self, cr_board: Board):  # -> int
        """
        Zwraca numer/indeks danej mini planszy
        """
        return self._ult_boards.index(cr_board)

    def get_mini_board(self, brd_num):  # -> Board()
        """
        Zwraca obiekt mini planszy o danym numerze/indeksie
        """
        return self._ult_boards[brd_num]

    def get_uboard_move(self, brd_num, brd_row, brd_col):  # -> str
        """
        Zwraca pozycje na mini planszy o danym indeksie, wierszu oraz kolumnie
        """
        return self.get_mini_board(brd_num).get_move(brd_row, brd_col)

    def set_uboard(self, brd_num: int):
        """
        Służy do sprawdzenia czy indeks planszy został podany prawidłowo
        oraz do ustawienia atrybutu '._current_board'
        na mini plansze o danym numerze/indeksie
        """
        if brd_num is None:
            raise BotStartGameError('Board is None!')
        if brd_num not in possible_boards:
            raise InvalidBoardError(brd_num)
        if not self.get_mini_board(int(brd_num)).check_correct_board():
            raise BoardFinishedError('Wrong board error!')
        self._current_board = self.get_mini_board(int(brd_num))

    def set_uboard_move(self, cr_board: Board, row, col, player):
        """
        Ustawia symbol gracza na danej pozycji na planszy.
        """
        if cr_board is None:
            raise MoveError('Set your board first!')
        cr_board.set_move(row, col, player)

    def update_finished_boards(self, brd_num, player):  # update
        """
        Aktualizuje atrybut '._finished_board' jesli plansza została wygrana
        to ustawia symbol gracza który wygrał, a jeśli remis to ustawia
        pustego stringa (na drugi element krotki)
        """
        mini_brd = self.get_mini_board(brd_num)
        if mini_brd.finished:
            if mini_brd.winner == player.upper():
                self.finished_boards[brd_num] = (brd_num, player)
            elif mini_brd.winner == 'Draw':
                self.finished_boards[brd_num] = (brd_num, " ")

    def check_mini(self, brd_num, player):
        """
        Sprawdza czy mini plansza o danym indeksie została skończona,
        a nastepnie odpowiednio aktualizuje skonczone plansze
        """
        self.get_mini_board(brd_num).check_board_draw()
        self.get_mini_board(brd_num).check_board_win(player.upper())
        self.update_finished_boards(brd_num, player)

    def next_board(self, row, col):  # -> int
        """
        Zwraca numer/indeks kolejnej planszy na której
        bedzie prowadzona rozgrywka, zgodnie z zasadami gry
        """
        boards = [_ for _ in range(9)]
        next_board = []
        for idx in range(9):
            if col == 0:  # [ 0, 3, 6 ]
                if idx % 3 == 0:
                    next_board.append(boards[idx])
            elif col == 1:  # [ 1, 4, 7 ]
                if idx % 3 == 1:
                    next_board.append(boards[idx])
            elif col == 2:  # [ 2, 5, 8 ]
                if idx % 3 == 2:
                    next_board.append(boards[idx])
        next_board.sort()
        return next_board[row]

    def player_switch(self, player):  # -> str
        """
        Słuzy do zmieniania symbolu gracza po każdej rundzie.
        """
        if player.upper() == 'X':
            return 'O'
        else:
            return 'X'

    def check_ultimate_row(self, player):  # -> bool
        """
        Sprawdza czy dany gracz wygrał jakiekolwiek 3 plansze w wierzu
        Zwraca Prawde jesli wygrał, a Fałsz jesli nie.
        """
        x = 0
        for _ in range(3):
            tic = self.get_mini_board(0+x).winner
            tac = self.get_mini_board(1+x).winner
            toe = self.get_mini_board(2+x).winner
            x += 3
            if tic == tac == toe == player is not None:
                return True
        return False

    def check_ultimate_column(self, player):  # -> bool
        """
        Sprawdza czy dany gracz wygrał jakiekolwiek 3 plansze w kolumnie
        Zwraca Prawde jesli wygrał, a Fałsz jesli nie.
        """
        x = 0
        for _ in range(3):
            tic = self.get_mini_board(0+x).winner
            tac = self.get_mini_board(3+x).winner
            toe = self.get_mini_board(6+x).winner
            x += 1
            if tic == tac == toe == player is not None:
                return True
        return False

    def check_ultimate_diagonally(self, player):  # -> bool
        """
        Sprawdza czy dany gracz ('symbol') wygrał jakiekolwiek 3 plansze
        po ukośie. Zwraca Prawde jesli wygrał, a Fałsz jesli nie.
        """
        tic = self.get_mini_board(0).winner
        tac = self.get_mini_board(4).winner
        toe = self.get_mini_board(8).winner
        if tic == tac == toe == player is not None:
            return True
        else:
            tic = self.get_mini_board(2).winner
            toe = self.get_mini_board(6).winner
            if tic == tac == toe == player is not None:
                return True
        return False

    def check_ultimate_win(self, player):  # -> bool
        """
        Sprawdza czy dany gracz ('symbol') wygrał w jakikolwiek sposób
        (w wierszy, kolumnie, lub po ukosie). Jeśłi tak to zwraca Prawde,
        w przeciwnym wypadku Fałsz.
        """
        win = [self.check_ultimate_row(player),
               self.check_ultimate_column(player),
               self.check_ultimate_diagonally(player)]
        if any(win):
            return True
        else:
            return False

    def check_ultimate_draw(self):  # -> bool
        """
        Sprawdza czy wszystkie plansze zostały skończone(nie wygraną).
        Jesli tak to zwraca 'Prawde' co oznacze ze cała gra zakończyła się
        remisem, w innym przypadku zwraca False co oznacza, że została jeszcze
        conajmniej jedna nieskonczona plansza.
        """
        for brd in self.ult_boards:
            if not brd.finished:
                return False
        return True
