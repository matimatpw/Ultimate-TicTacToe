from board import Board, Field
from errors import (
    InvalidPlayerError, InvalidValueError,
    WrongMoveError, WrongTypeError)
from pytest import raises as pt


def test_Field():
    field = Field()
    assert field.get_pos == '-'


def test_field_update_pos():
    field = Field()
    assert field.get_pos == '-'
    field.update_pos('X')
    assert field.get_pos == 'X'


def test_check_empty_move_true():
    field = Field()
    assert field.check_empty_move() is True


def test_check_empty_move_false():
    field = Field()
    field.update_pos('O')
    assert field.check_empty_move() is False


def test_str_field():
    field = Field()
    field.update_pos('O')
    assert str(field) == 'O'


def test_board_init():
    board = Board()
    assert len(board.board) == 3
    for field_list in board.board:
        for field in field_list:
            assert field.get_pos == '-'
    assert board.finished is False
    assert board.winner is None


def test_board_get_field():
    board = Board()
    field = board.board[0][0]
    assert board.get_field(0, 0) == field


def test_board_get_empty_move():
    board = Board()
    assert board.get_move(0, 0) == '-'


def test_board_get_move():
    board = Board()
    board.get_field(0, 0).update_pos('X')
    assert board.get_move(0, 0) == 'X'


def test_set_move():
    board = Board()
    assert board.get_move(0, 0) == '-'
    board.set_move(0, 0, 'X')
    assert board.get_move(0, 0) == 'X'


def test_set_move_InvalidValueError():
    board = Board()
    with pt(InvalidValueError):
        board.set_move(-13, 0, 'X')


def test_set_move_WrongTYoeError_str():
    board = Board()
    with pt(WrongTypeError):
        board.set_move('as', 0, 'X')


def test_set_move_WrongTYoeError_strnumber():
    board = Board()
    with pt(WrongTypeError):
        board.set_move('2', 0, 'X')


def test_set_move_WrongTYoeError_float():
    board = Board()
    with pt(WrongTypeError):
        board.set_move(1.231, 0, 'X')


def test_set_occupied_move_error():
    board = Board()
    board.set_move(0, 0, 'O')
    with pt(WrongMoveError):
        board.set_move(0, 0, 'X')


def test_set_move_wrong_player():
    board = Board()
    with pt(InvalidPlayerError):
        board.set_move(0, 0, 'l')


def test_get_empty_fields():
    board = Board()
    board.set_move(0, 0, 'X')
    board.set_move(2, 2, 'X')
    board.set_move(1, 1, 'O')
    assert board.get_empty_fields() == [
        (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]


def test_check_correct_move_true():
    board = Board()
    assert board.check_correct_move(0, 0) is True


def test_check_correct_move_false():
    board = Board()
    board.set_move(0, 0, 'X')
    assert board.check_correct_move(0, 0) is False


def test_check_correct_board_true():
    board = Board()
    board.set_move(0, 0, 'X')
    board.set_move(0, 2, 'X')
    board.set_move(0, 1, 'X')
    board.check_board_win('X')
    assert board.check_correct_board() is False


def test_check_correct_board_false():
    board = Board()
    assert board.check_correct_board() is True


def test_check_row_win_true():
    board = Board()
    board.set_move(0, 0, 'X')
    board.set_move(0, 2, 'X')
    board.set_move(0, 1, 'X')
    assert board.check_row_win('X') is True


def test_check_row_win_false():
    board = Board()
    board.set_move(0, 0, 'X')
    board.set_move(0, 2, 'O')
    board.set_move(0, 1, 'X')
    assert board.check_row_win('X') is False


def test_check_diagonally_win_false():
    board = Board()
    board.set_move(0, 0, 'X')
    board.set_move(2, 2, 'O')
    board.set_move(1, 1, 'X')
    assert board.check_diagonally_win('X') is False


def test_check_diagonally_win_true():
    board = Board()
    board.set_move(0, 0, 'X')
    board.set_move(2, 2, 'X')
    board.set_move(1, 1, 'X')
    assert board.check_diagonally_win('X') is True


def test_check_column_win_true():
    board = Board()
    board.set_move(0, 0, 'X')
    board.set_move(2, 0, 'X')
    board.set_move(1, 0, 'X')
    assert board.check_column_win('X') is True


def test_check_column_win_fasle():
    board = Board()
    board.set_move(0, 0, 'X')
    board.set_move(2, 0, 'O')
    board.set_move(1, 0, 'X')
    assert board.check_column_win('X') is False


def test_check_board_win_true():
    board = Board()
    board.set_move(0, 0, 'X')
    board.set_move(2, 0, 'X')
    assert board.finished is False
    board.set_move(1, 0, 'X')
    assert board.check_board_win('X') is True
    assert board.finished is True
    assert board.winner == 'X'


def test_check_board_win_false():
    board = Board()
    board.set_move(0, 0, 'X')
    board.set_move(2, 0, 'O')
    board.set_move(1, 0, 'X')
    assert board.check_board_win('X') is False
    assert board.finished is False
    assert board.winner is None


def test_check_board_draw_true():
    board = Board()
    board.set_move(0, 0, 'X')
    board.set_move(0, 1, 'O')
    board.set_move(0, 2, 'X')
    board.set_move(1, 0, 'O')
    board.set_move(1, 1, 'X')
    board.set_move(1, 2, 'O')
    board.set_move(2, 0, 'O')
    board.set_move(2, 1, 'X')
    board.set_move(2, 2, 'O')
    board.check_board_win('X')
    board.check_board_win('O')
    assert board.check_board_draw() is True
    assert board.finished is True
    assert board.winner == 'Draw'


def test_check_board_draw_false():
    board = Board()
    board.set_move(0, 0, 'X')
    board.set_move(0, 1, 'O')
    board.set_move(0, 2, 'X')
    board.set_move(1, 0, 'O')
    board.set_move(1, 1, 'X')
    board.set_move(1, 2, 'O')
    board.set_move(2, 0, 'O')
    board.set_move(2, 1, 'X')
    board.check_board_win('X')
    board.check_board_win('O')
    assert board.check_board_draw() is False
    assert board.finished is False
    assert board.winner is None
