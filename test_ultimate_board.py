from ultimate_board import UltimateTicTacToe
from board import Board
from errors import (
    InvalidBoardError, BoardFinishedError,
    MoveError, BotStartGameError
    )
from pytest import raises


def test_init():
    game = UltimateTicTacToe()
    assert len(game.ult_boards) == 9
    assert game.current_board is None
    assert len(game.finished_boards) == 9
    assert type(game.ult_boards[0]) == Board


def test_get_index():
    game = UltimateTicTacToe()
    assert game.get_index(game.ult_boards[2]) == 2


def test_get_mini_board():
    game = UltimateTicTacToe()
    board = game.ult_boards[3]
    assert game.get_mini_board(3) == board


def test_get_uboard_move_empty():
    game = UltimateTicTacToe()
    assert game.get_uboard_move(0, 0, 0) == '-'


def test_get_uboard_move_player():
    game = UltimateTicTacToe()
    game.get_mini_board(0).get_field(0, 0).update_pos('X')
    game.get_mini_board(3).get_field(1, 1).update_pos('O')
    assert game.get_uboard_move(0, 0, 0) == 'X'
    assert game.get_uboard_move(3, 1, 1) == 'O'


def test_set_uboard_move():
    game = UltimateTicTacToe()
    board = game.get_mini_board(0)
    assert game.get_uboard_move(0, 0, 0) == '-'
    game.set_uboard_move(board, 0, 0, 'X')
    assert game.get_uboard_move(0, 0, 0) == 'X'


def test_set_uboard_move_error():
    game = UltimateTicTacToe()
    assert game.get_uboard_move(0, 0, 0) == '-'
    assert game.current_board is None
    with raises(MoveError):
        game.set_uboard_move(game.current_board, 0, 0, 'X')


def test_set_uboard():
    game = UltimateTicTacToe()
    assert game.current_board is None
    game.set_uboard(0)
    board = game.get_mini_board(0)
    assert game.current_board == board


def test_set_uboard_BotStartGameError():
    game = UltimateTicTacToe()
    with raises(BotStartGameError):
        game.set_uboard(game.current_board)


def test_set_uboard_InvalidvalueError():
    game = UltimateTicTacToe()
    with raises(InvalidBoardError):
        game.set_uboard(123)


def test_set_uboard_BoardFinishedError():
    game = UltimateTicTacToe()
    game.get_mini_board(0).set_move(0, 0, 'X')
    game.get_mini_board(0).set_move(0, 2, 'X')
    game.get_mini_board(0).set_move(0, 1, 'X')
    game.get_mini_board(0).check_board_win('X')
    with raises(BoardFinishedError):
        game.set_uboard(0)


def test_update_finished_boards_not_win_nor_draw():
    game = UltimateTicTacToe()
    game.get_mini_board(0).set_move(0, 0, 'X')
    game.get_mini_board(0).set_move(0, 2, 'X')
    game.get_mini_board(0).set_move(0, 1, 'O')
    game.get_mini_board(0).set_move(1, 1, 'O')
    game.get_mini_board(0).check_board_draw()
    game.get_mini_board(0).check_board_win('X')
    game.get_mini_board(0).check_board_win('O')
    game.update_finished_boards(0, 'X')
    game.update_finished_boards(0, 'O')
    assert game.finished_boards[0] == (0, 0)


def test_update_finished_boards_win():
    game = UltimateTicTacToe()
    game.get_mini_board(0).set_move(0, 0, 'X')
    game.get_mini_board(0).set_move(0, 2, 'X')
    game.get_mini_board(0).set_move(0, 1, 'X')
    game.get_mini_board(0).set_move(1, 1, 'O')
    game.get_mini_board(0).check_board_draw()
    game.get_mini_board(0).check_board_win('X')
    assert game.finished_boards[0] == (0, 0)
    game.update_finished_boards(0, 'X')
    assert game.finished_boards[0] == (0, 'X')


def test_update_finished_boards_draw():
    game = UltimateTicTacToe()
    game.get_mini_board(0).set_move(0, 0, 'X')
    game.get_mini_board(0).set_move(0, 2, 'O')
    game.get_mini_board(0).set_move(0, 1, 'X')
    game.get_mini_board(0).set_move(1, 0, 'O')
    game.get_mini_board(0).set_move(1, 2, 'X')
    game.get_mini_board(0).set_move(1, 1, 'O')
    game.get_mini_board(0).set_move(2, 0, 'X')
    game.get_mini_board(0).set_move(2, 2, 'O')
    game.get_mini_board(0).set_move(2, 1, 'O')
    game.get_mini_board(0).check_board_draw()
    game.get_mini_board(0).check_board_win('X')
    game.get_mini_board(0).check_board_win('O')
    assert game.finished_boards[0] == (0, 0)
    game.update_finished_boards(0, 'O')
    game.update_finished_boards(0, 'X')
    assert game.finished_boards[0] == (0, ' ')


def test_check_mini():
    game = UltimateTicTacToe()
    assert game.get_mini_board(0).winner is None
    game.get_mini_board(0).set_move(0, 0, 'X')
    game.get_mini_board(0).set_move(0, 1, 'X')
    game.get_mini_board(0).set_move(0, 2, 'X')
    game.check_mini(0, 'X')
    assert game.get_mini_board(0).winner == 'X'


def test_chek_mini_but_draw():
    game = UltimateTicTacToe()
    game.get_mini_board(0).set_move(0, 0, 'X')
    game.get_mini_board(0).set_move(0, 2, 'O')
    game.get_mini_board(0).set_move(0, 1, 'X')
    game.get_mini_board(0).set_move(1, 0, 'O')
    game.get_mini_board(0).set_move(1, 2, 'X')
    game.get_mini_board(0).set_move(1, 1, 'O')
    game.get_mini_board(0).set_move(2, 0, 'X')
    game.get_mini_board(0).set_move(2, 2, 'O')
    game.get_mini_board(0).set_move(2, 1, 'O')
    game.check_mini(0, 'X')
    game.check_mini(0, 'O')
    assert game.get_mini_board(0).winner == 'Draw'


def test_next_board():
    game = UltimateTicTacToe()
    assert game.next_board(0, 0) == 0


def test_next_board_v2():
    game = UltimateTicTacToe()
    assert game.next_board(2, 1) == 7


def test_player_switch():
    game = UltimateTicTacToe()
    assert game.player_switch('X') == 'O'
    assert game.player_switch('O') == 'X'


def test_check_ultimate_row_win():
    game = UltimateTicTacToe()
    game.get_mini_board(0).set_move(0, 0, 'X')
    game.get_mini_board(0).set_move(0, 1, 'X')
    game.get_mini_board(0).set_move(0, 2, 'X')
    game.get_mini_board(1).set_move(0, 0, 'X')
    game.get_mini_board(1).set_move(0, 1, 'X')
    game.get_mini_board(1).set_move(0, 2, 'X')
    game.get_mini_board(2).set_move(0, 0, 'X')
    game.get_mini_board(2).set_move(0, 1, 'X')
    game.get_mini_board(2).set_move(0, 2, 'X')
    game.check_mini(0, 'X')
    game.check_mini(1, 'X')
    game.check_mini(2, 'X')
    assert game.check_ultimate_win('X') is True


def test_check_ultimate_not_row_win():
    game = UltimateTicTacToe()
    game.get_mini_board(0).set_move(0, 0, 'X')
    game.get_mini_board(0).set_move(0, 1, 'X')
    game.get_mini_board(0).set_move(0, 2, 'X')
    game.get_mini_board(1).set_move(0, 0, 'X')
    game.get_mini_board(1).set_move(0, 1, 'X')
    game.get_mini_board(1).set_move(0, 2, 'X')
    game.get_mini_board(2).set_move(0, 0, 'X')
    game.get_mini_board(2).set_move(0, 1, 'X')
    game.get_mini_board(2).set_move(0, 2, 'O')
    game.check_mini(0, 'X')
    game.check_mini(1, 'X')
    game.check_mini(2, 'X')
    assert game.check_ultimate_win('X') is False


def test_check_ultimate_diagonally_win():
    game = UltimateTicTacToe()
    game.get_mini_board(0).set_move(0, 0, 'X')
    game.get_mini_board(0).set_move(0, 1, 'X')
    game.get_mini_board(0).set_move(0, 2, 'X')
    game.get_mini_board(4).set_move(0, 0, 'X')
    game.get_mini_board(4).set_move(0, 1, 'X')
    game.get_mini_board(4).set_move(0, 2, 'X')
    game.get_mini_board(8).set_move(0, 0, 'X')
    game.get_mini_board(8).set_move(0, 1, 'X')
    game.get_mini_board(8).set_move(0, 2, 'X')
    game.check_mini(0, 'X')
    game.check_mini(4, 'X')
    game.check_mini(8, 'X')
    assert game.check_ultimate_diagonally('X') is True


def test_check_ultimate_diagonally_not_win():
    game = UltimateTicTacToe()
    game.get_mini_board(0).set_move(0, 0, 'X')
    game.get_mini_board(0).set_move(0, 1, 'X')
    game.get_mini_board(0).set_move(0, 2, 'O')
    game.get_mini_board(4).set_move(0, 0, 'X')
    game.get_mini_board(4).set_move(0, 1, 'O')
    game.get_mini_board(4).set_move(0, 2, 'X')
    game.get_mini_board(8).set_move(0, 0, 'X')
    game.get_mini_board(8).set_move(0, 1, 'O')
    game.get_mini_board(8).set_move(0, 2, 'X')
    game.check_mini(0, 'X')
    game.check_mini(4, 'X')
    game.check_mini(8, 'X')
    assert game.check_ultimate_diagonally('X') is False


def test_check_ultimate_column_win():
    game = UltimateTicTacToe()
    game.get_mini_board(0).set_move(0, 0, 'X')
    game.get_mini_board(0).set_move(0, 1, 'X')
    game.get_mini_board(0).set_move(0, 2, 'X')
    game.get_mini_board(3).set_move(0, 0, 'X')
    game.get_mini_board(3).set_move(0, 1, 'X')
    game.get_mini_board(3).set_move(0, 2, 'X')
    game.get_mini_board(6).set_move(0, 0, 'X')
    game.get_mini_board(6).set_move(0, 1, 'X')
    game.get_mini_board(6).set_move(0, 2, 'X')
    game.check_mini(0, 'X')
    game.check_mini(3, 'X')
    game.check_mini(6, 'X')
    assert game.check_ultimate_column('X') is True


def test_check_ultimate_column_not_win():
    game = UltimateTicTacToe()
    game.get_mini_board(1).set_move(0, 0, 'X')
    game.get_mini_board(1).set_move(0, 1, 'X')
    game.get_mini_board(1).set_move(0, 2, 'O')
    game.get_mini_board(4).set_move(0, 0, 'X')
    game.get_mini_board(4).set_move(0, 1, 'O')
    game.get_mini_board(4).set_move(0, 2, 'X')
    game.get_mini_board(7).set_move(0, 0, 'X')
    game.get_mini_board(7).set_move(0, 1, 'O')
    game.get_mini_board(7).set_move(0, 2, 'X')
    game.check_mini(1, 'X')
    game.check_mini(4, 'X')
    game.check_mini(7, 'X')
    assert game.check_ultimate_column('X') is False


def test_chec_ultimate_not_win():
    game = UltimateTicTacToe()
    game.get_mini_board(0).set_move(0, 0, 'X')
    game.get_mini_board(0).set_move(0, 1, 'X')
    game.get_mini_board(0).set_move(0, 2, 'O')
    game.get_mini_board(4).set_move(0, 0, 'X')
    game.get_mini_board(4).set_move(0, 1, 'O')
    game.get_mini_board(4).set_move(0, 2, 'X')
    game.get_mini_board(8).set_move(0, 0, 'X')
    game.get_mini_board(8).set_move(0, 1, 'O')
    game.get_mini_board(8).set_move(0, 2, 'X')
    game.check_mini(0, 'X')
    game.check_mini(4, 'X')
    game.check_mini(8, 'X')
    assert game.check_ultimate_win('X') is False


def test_chec_ultimate_win():
    game = UltimateTicTacToe()
    game.get_mini_board(0).set_move(0, 0, 'X')
    game.get_mini_board(0).set_move(1, 1, 'X')
    game.get_mini_board(0).set_move(2, 2, 'X')
    game.get_mini_board(4).set_move(0, 0, 'X')
    game.get_mini_board(4).set_move(0, 1, 'X')
    game.get_mini_board(4).set_move(0, 2, 'X')
    game.get_mini_board(8).set_move(0, 0, 'X')
    game.get_mini_board(8).set_move(1, 1, 'X')
    game.get_mini_board(8).set_move(2, 2, 'X')
    game.check_mini(0, 'X')
    game.check_mini(4, 'X')
    game.check_mini(8, 'X')
    assert game.check_ultimate_win('X') is True


def test_chec_ultimate_draw():
    game = UltimateTicTacToe()
    game.get_mini_board(0).set_move(0, 0, 'X')
    game.get_mini_board(0).set_move(0, 1, 'X')
    game.get_mini_board(0).set_move(0, 2, 'X')

    game.get_mini_board(1).set_move(0, 0, 'X')
    game.get_mini_board(1).set_move(0, 1, 'X')
    game.get_mini_board(1).set_move(0, 2, 'X')

    game.get_mini_board(2).set_move(0, 0, 'X')
    game.get_mini_board(2).set_move(0, 1, 'X')
    game.get_mini_board(2).set_move(0, 2, 'X')

    game.get_mini_board(3).set_move(0, 0, 'X')
    game.get_mini_board(3).set_move(0, 1, 'X')
    game.get_mini_board(3).set_move(0, 2, 'X')

    game.get_mini_board(4).set_move(0, 0, 'X')
    game.get_mini_board(4).set_move(0, 1, 'X')
    game.get_mini_board(4).set_move(0, 2, 'X')

    game.get_mini_board(5).set_move(0, 0, 'X')
    game.get_mini_board(5).set_move(0, 1, 'X')
    game.get_mini_board(5).set_move(0, 2, 'X')

    game.get_mini_board(6).set_move(0, 0, 'X')
    game.get_mini_board(6).set_move(0, 1, 'X')
    game.get_mini_board(6).set_move(0, 2, 'X')

    game.get_mini_board(7).set_move(0, 0, 'X')
    game.get_mini_board(7).set_move(0, 1, 'X')
    game.get_mini_board(7).set_move(0, 2, 'X')

    game.get_mini_board(8).set_move(0, 1, 'X')
    game.get_mini_board(8).set_move(0, 2, 'X')
    game.get_mini_board(8).set_move(0, 0, 'X')

    game.check_mini(0, 'X')
    game.check_mini(1, 'X')
    game.check_mini(2, 'X')
    game.check_mini(3, 'X')
    game.check_mini(4, 'X')
    game.check_mini(5, 'X')
    game.check_mini(6, 'X')
    game.check_mini(7, 'X')
    game.check_mini(8, 'X')

    assert game.check_ultimate_draw() is True


def test_chekc_ultimate_draw_not():
    game = UltimateTicTacToe()
    game.get_mini_board(4).set_move(0, 0, 'X')
    game.get_mini_board(4).set_move(0, 1, 'X')
    game.get_mini_board(4).set_move(0, 2, 'X')

    game.get_mini_board(5).set_move(0, 0, 'X')
    game.get_mini_board(5).set_move(0, 1, 'X')
    game.get_mini_board(5).set_move(0, 2, 'X')

    game.get_mini_board(6).set_move(0, 0, 'X')
    game.get_mini_board(6).set_move(0, 1, 'X')
    game.get_mini_board(6).set_move(0, 2, 'X')

    game.get_mini_board(7).set_move(0, 0, 'X')
    game.get_mini_board(7).set_move(0, 1, 'X')
    game.get_mini_board(7).set_move(0, 2, 'X')

    game.get_mini_board(8).set_move(0, 1, 'X')
    game.get_mini_board(8).set_move(0, 2, 'X')
    game.get_mini_board(8).set_move(0, 0, 'X')

    game.check_mini(0, 'X')
    game.check_mini(1, 'X')
    game.check_mini(2, 'X')
    game.check_mini(3, 'X')
    game.check_mini(4, 'X')
    game.check_mini(5, 'X')
    game.check_mini(6, 'X')
    game.check_mini(7, 'X')
    game.check_mini(8, 'X')
    assert game.check_ultimate_draw() is False
