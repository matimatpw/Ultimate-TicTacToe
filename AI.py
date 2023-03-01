from ultimate_board import UltimateTicTacToe
from random import choice


class RandomAI:
    """
    Zapewnia możliwość prowadzenia rozgrywki przez komputer
    Klasa RandomAI zawiera atrybuty:
    :param boards: Jest listą 9 małych plansz (obiektów Board())
    :type: list

    :param game: Jest obiektem klasy 'UltimateTicTacToe()'
    :type: UltimateTicTacToe()
    """
    def __init__(self, Ultimate: UltimateTicTacToe) -> None:
        self._boards = Ultimate.ult_boards
        self._game = Ultimate

    @property
    def game(self):
        return self._game

    def AI_get_playable_boards(self):  # -> list
        """
        Zwraca liste numerów/indeksów nieskończonych plansz
        """
        playable_boards = []
        for board in self._boards:
            if not board.finished:
                playable_boards.append(self.game.get_index(board))
        playable_boards.sort()
        return playable_boards

    def Ai_get_random_board(self):  # -> int
        """
        Zapewnia możliwość wybrania losowego numeru/indeksu planszy
        z możliwych przez komputer. Zwraca całkowitą wartość
        wylosowanego numeru planszy
        """
        chosen_board = choice(self.AI_get_playable_boards())
        return int(chosen_board)

    def AI_get_playable_moves(self, brd_num):  # -> list
        """
        Zwraca liste krotek '(wiersz, kolumna)' możliwych ruchów
        (tzn. pustych pozycji) na planszy o danym indeksie
        """
        playable_moves = self.game.get_mini_board(brd_num).get_empty_fields()
        return playable_moves

    def Ai_get_random_move(self, brd_num):  # -> tuple
        """
        Zwraca krotkę wylosowanego ruchu z wszystkich możliwych na planszy
        o danym numerze/indeksie
        """
        chosen_move = choice(self.AI_get_playable_moves(brd_num))
        return chosen_move


class HardAI(RandomAI):
    """
    Zapewnia mozliwosc prowadzena rozgrywki przez inteligentny komputer
    Dziedziczy po klasie RandomAI()
    """
    def __init__(self, Ultimate: UltimateTicTacToe) -> None:
        super().__init__(Ultimate)
        pass

    def Hard_chose_board(self):  # -> int
        """
        Zapewnia wybór planszy przez komputer na podstawie paru
        prostych kryteriów. Zwraca numer/indeks najlepszej do grania planszy
        """
        for board in self.game.ult_boards:  # board where can win
            idx = self.game.get_index(board)
            if not board.finished:
                if self.Hard_get_finish_block(idx):
                    return idx

        for board in self.game.ult_boards:  # board where can block
            idx = self.game.get_index(board)
            if not board.finished:
                if self.Hard_get_finish_block(idx, 'X'):
                    return idx

        for board in self.game.ult_boards:  # board where can play centre
            idx = self.game.get_index(board)
            if not board.finished:
                if self.Hard_get_centre(idx):
                    return idx

        for board in self.game.ult_boards:  # board where can oposite corner
            idx = self.game.get_index(board)
            if not board.finished:
                if self.Hard_get_oposite_corner(idx):
                    return idx
        return self.Ai_get_random_board()  # any other move

    def Hard_chose_move(self, brd_num):  # -> tuple
        """
        Wybiera i zwraca najlepszy możliwy ruch na podstawie prostych kryteriów
        """
        # finish win
        move = self.Hard_get_finish_block(brd_num)
        if not move:
            # block
            move = self.Hard_get_finish_block(brd_num, 'X')
            if not move:
                # take centre
                move = self.Hard_get_centre(brd_num)
                if not move:
                    # take oposite corner
                    move = self.Hard_get_oposite_corner(brd_num)
                    if not move:
                        # take any corner
                        move = self.Hard_get_any_corner(brd_num)
                        if not move:
                            # take any side == random move
                            move = self.Ai_get_random_move(brd_num)
                    else:
                        return move
                else:
                    return move
            else:
                return move
        else:
            return move
        return move

    def Hard_get_any_corner(self, brd_num):  # -> tuple, None
        """
        Wybiera oraz zwraca wspolrzedne jakiegokolwiek pustego rogu
        na planszy o danym numerze/indeksie jeśli taki ruch istnieje,
        jesli nie to zwraca 'None'
        """
        empty_fields = self.game.get_mini_board(brd_num).get_empty_fields()
        if (0, 0) in empty_fields:
            return (0, 0)
        elif (0, 2) in empty_fields:
            return (0, 2)
        elif (2, 2) in empty_fields:
            return (2, 2)
        elif (2, 0) in empty_fields:
            return (2, 0)
        else:
            return None

    def Hard_get_oposite_corner(self, brd_num):  # tuple, None
        """
        Wybiera przeciwny róg na planszy o danym numerze/indeksie
        Zwraca wspołrzedne tego ruchu '(wiersz, kolumna)' jesli
        taki ruch istnieje, w innym przypadku zwraca 'None'
        """
        left_up = self.game.get_mini_board(brd_num).get_move(0, 0)
        left_down = self.game.get_mini_board(brd_num).get_move(2, 0)
        right_up = self.game.get_mini_board(brd_num).get_move(0, 2)
        right_down = self.game.get_mini_board(brd_num).get_move(2, 2)
        if left_up == 'X':
            if right_down == '-':
                return (2, 2)
        elif left_down == 'X':
            if right_up == '-':
                return (0, 2)
        elif right_up == 'X':
            if left_down == '-':
                return (2, 0)
        elif right_down == 'X':
            if left_up == '-':
                return (0, 0)
        else:
            return None

    def Hard_get_finish_block(self, brd_num, player='O'):  # -> tuple, None
        """
        Zapewnia możliwość blokowania lub kończenia wygranej w zaleznosci
        od danego parametru 'player' ('X' to blokuje, a 'O' to kończy wygraną)
        Sprawdza czy w jakimkolwiek wierszu, kolumnie, lub ukosie
        istnieją 2 symbole gracza 'player' oraz symbol pustego pola.
        Jeśli tak to zwraca pozycje '(wiersz, kolumne)' tego pustego pola,
        a jesli nie to zwraca None.
        """
        # check row or col
        for row in range(3):
            check_row = []
            check_col = []
            for col in range(3):
                pos_row = self.game.get_mini_board(brd_num).get_move(row, col)
                pos_col = self.game.get_mini_board(brd_num).get_move(col, row)
                check_row.append(pos_row)
                check_col.append(pos_col)

            if check_row.count(player) == 2 and '-' in check_row:
                col_idx = check_row.index('-')
                return (row, col_idx)
            elif check_col.count(player) == 2 and '-' in check_col:
                row_idx = check_col.index('-')
                return (row_idx, row)

        # check diag
        check_diag = []
        for diag in range(3):
            pos_diag = self.game.get_mini_board(brd_num).get_move(diag, diag)
            check_diag.append(pos_diag)
        if check_diag.count(player) == 2 and '-' in check_diag:
            diag_idx = check_diag.index('-')
            return (diag_idx, diag_idx)
        # check another diag
        check_diagv2 = []
        help_list = [2, 1, 0]
        for diag_row in range(3):
            diag_col = help_list[diag_row]
            get_mini = self.game.get_mini_board(brd_num)  # -> Board()
            pos_diagv2 = get_mini.get_move(diag_row, diag_col)
            check_diagv2.append(pos_diagv2)
        if check_diagv2.count(player) == 2 and '-' in check_diagv2:
            diagv2_row_idx = check_diagv2.index('-')
            return (diagv2_row_idx, help_list[diagv2_row_idx])
        return None

    def Hard_get_centre(self, brd_num):  # -> tuple, None
        """
        Sprawdza czy środek na planszy o danym indeksie jest pusty.
        Jesli jest to zwraca 'wspolrzędne' środka planszy,
        w przeciwnym wypadku zwraca 'None'
        """
        pos = self.game.get_mini_board(brd_num).get_move(1, 1)
        if pos == '-':
            return (1, 1)
        else:
            return None
