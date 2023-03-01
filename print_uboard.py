from ultimate_board import UltimateTicTacToe, Board
from globals import red, bold, green, blue


def mini_board(mini: Board, row_in_brd):  # -> list
    """Funkcja zwracająca liste obiektów 'FIeld()' w danym wierszu"""
    return mini.board[row_in_brd]


def print_row(list_of_fields: list):
    """Funkcja printujaca i oddzielająca pozycje na mini planszy"""
    for idx, elem in enumerate(list_of_fields):
        if idx == len(list_of_fields) - 1:
            liner = " || "
        else:
            liner = f" {red('|')} "
        print(str(elem), end=liner)


def print_finished_boards(game: UltimateTicTacToe):
    """
    Funckcja odpowiadająca za wyświetlanie tabelki '_Board indexing_'
    Tabelka wyświetla indeksy małych plansz(0-8) na dużej planszy
    oraz pokazuje, które plansze zostały zremisowane(pusty string)
    lub wygrane(symbol gracza ktory wygrał daną plansze)
    """
    winners = [tup[1] for tup in game.finished_boards]
    idx = -1
    print("_Board indexing_".center(42))

    for _ in range(3):
        print(end="".center(18))
        splitter = "|"
        for y in range(3):
            idx += 1
            if y == 2:
                splitter = ""
            if winners[idx] == 'O' or winners[idx] == 'X':
                winner = bold(str(winners[idx]))
            else:
                winner = winners[idx]
            print(winner, end=splitter)
        print()


def mark_winner(game, brd_num):
    """Funkcja zamienia małą plansze na kolorowy
        symbol gracza który daną plansze wygrał
    """
    mini = game.get_mini_board(brd_num)
    plr_x = green('X')
    plr_o = blue('O')
    if mini.winner == 'X':  # 'X' win
        for row_idx in range(3):
            if row_idx == 1:
                mini.get_field(row_idx, 1).mark_pos(plr_x)
                mini.get_field(row_idx, 0).mark_pos(" ")
                mini.get_field(row_idx, 2).mark_pos(" ")
            else:
                mini.get_field(row_idx, 0).mark_pos(plr_x)
                mini.get_field(row_idx, 2).mark_pos(plr_x)
                mini.get_field(row_idx, 1).mark_pos(" ")

    elif mini.winner == 'O':  # 'O' win
        for row_idx in range(3):
            for col_idx in range(3):
                if row_idx == 1 and col_idx == 1:
                    mini.get_field(row_idx, col_idx).mark_pos(" ")
                else:
                    mini.get_field(row_idx, col_idx).mark_pos(plr_o)


def print_ultimate_board(game: UltimateTicTacToe):
    """
    Funkcja odpowiadająca za wyświetlanie planszy razem z tabelką indeksów
    """
    mini_brds_list = game.ult_boards
    splitter = '-' * 43
    split_list = ['--']

    for _ in range(3):
        for col_num in range(3):
            for _ in range(3):
                split_list.append('-')
            split_list.append(bold(str(col_num)))
        split_list.append('-')
    split_list.append('--')
    first_splitter = "".join(split_list)
    start, stop = 0, 3
    print(first_splitter)

    run = 0
    while run != 3:
        for idx, row_in_brd in enumerate(range(3)):
            print(end=f"{bold(str(idx))} || ")
            for brd_num in range(start, stop):
                mini_brd = mini_brds_list[brd_num]
                x_list = mini_board(mini_brd, row_in_brd)
                print_row(x_list)
            print()
            if idx == 2:
                print(splitter)
                start += 3
                stop += 3
                run += 1
    print_finished_boards(game)
