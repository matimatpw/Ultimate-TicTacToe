from ultimate_board import UltimateTicTacToe
from game import AI_board, AI_move, HardAI, RandomAI


def test_HardAI_board_normal():
    game = UltimateTicTacToe()
    Ai = HardAI(game)
    assert AI_board(game, Ai, 0, True) == 0


def test_HardAI_board_get_board_that_can_win():
    game = UltimateTicTacToe()
    Ai = HardAI(game)
    game.get_mini_board(0).set_move(0, 0, 'O')
    game.get_mini_board(0).set_move(0, 1, 'O')
    assert AI_board(game, Ai, None, True) == 0


def test_HardAI_board_get_board_that_can_block():
    game = UltimateTicTacToe()
    Ai = HardAI(game)
    game.get_mini_board(2).set_move(0, 0, 'X')
    game.get_mini_board(2).set_move(0, 1, 'X')
    assert AI_board(game, Ai, None, True) == 2


def test_HardAI_board_get_board_that_play_centre():
    game = UltimateTicTacToe()
    Ai = HardAI(game)
    game.get_mini_board(0).set_move(1, 1, 'O')
    game.get_mini_board(1).set_move(1, 1, 'X')
    assert AI_board(game, Ai, None, True) == 2


def test_HardAI_board_get_board_that_play_oposite_corner():
    game = UltimateTicTacToe()
    Ai = HardAI(game)
    game.get_mini_board(0).set_move(1, 1, 'O')
    game.get_mini_board(1).set_move(1, 1, 'X')
    game.get_mini_board(2).set_move(1, 1, 'X')
    game.get_mini_board(2).set_move(0, 0, 'X')
    assert AI_board(game, Ai, None, True) == 2


def test_HardAI_move_that_finish_win():
    game = UltimateTicTacToe()
    Ai = HardAI(game)
    game.get_mini_board(0).set_move(0, 0, 'O')
    game.get_mini_board(0).set_move(0, 1, 'O')
    assert AI_move(game, Ai, 0, True, 'O') == (0, 2)


def test_HardAI_move_that_block():
    game = UltimateTicTacToe()
    Ai = HardAI(game)
    game.get_mini_board(0).set_move(0, 0, 'X')
    game.get_mini_board(0).set_move(1, 1, 'X')
    assert AI_move(game, Ai, 0, True, 'O') == (2, 2)


def test_HardAI_move_that_play_centre():
    game = UltimateTicTacToe()
    Ai = HardAI(game)
    assert AI_move(game, Ai, 0, True, 'O') == (1, 1)


def test_HardAI_move_that_play_oposite_corner():
    game = UltimateTicTacToe()
    Ai = HardAI(game)
    game.get_mini_board(0).set_move(2, 0, 'X')
    game.get_mini_board(0).set_move(1, 1, 'O')
    assert AI_move(game, Ai, 0, True, 'O') == (0, 2)


def test_HardAI_move_that_play_any_corner():
    game = UltimateTicTacToe()
    Ai = HardAI(game)
    game.get_mini_board(0).set_move(1, 1, 'X')
    assert AI_move(game, Ai, 0, True, 'O') == (0, 0)


def test_HardAI_move_that_play_any_side(monkeypatch):
    def fake(a):
        return (1, 0)
    monkeypatch.setattr('AI.choice', fake)
    game = UltimateTicTacToe()
    Ai = HardAI(game)
    game.get_mini_board(0).set_move(0, 0, 'X')
    game.get_mini_board(0).set_move(1, 1, 'X')
    game.get_mini_board(0).set_move(2, 2, 'O')
    game.get_mini_board(0).set_move(2, 0, 'O')
    game.get_mini_board(0).set_move(0, 1, 'O')
    game.get_mini_board(0).set_move(0, 2, 'X')
    game.get_mini_board(0).set_move(2, 1, 'X')

    assert AI_move(game, Ai, 0, True, 'O') == (1, 0)


def test_HardAI_move_that_play_any_side_v2(monkeypatch):
    def fake(a):
        return (1, 2)
    monkeypatch.setattr('AI.choice', fake)
    game = UltimateTicTacToe()
    Ai = HardAI(game)
    game.get_mini_board(0).set_move(0, 0, 'X')
    game.get_mini_board(0).set_move(1, 1, 'X')
    game.get_mini_board(0).set_move(2, 2, 'O')
    game.get_mini_board(0).set_move(2, 0, 'O')
    game.get_mini_board(0).set_move(0, 1, 'O')
    game.get_mini_board(0).set_move(0, 2, 'X')
    game.get_mini_board(0).set_move(2, 1, 'X')

    assert AI_move(game, Ai, 0, True, 'O') == (1, 2)


def test_RandomAI_move(monkeypatch):
    def fake(a):
        return (1, 2)
    monkeypatch.setattr('AI.choice', fake)
    game = UltimateTicTacToe()
    Ai = RandomAI(game)

    assert AI_move(game, Ai, 0, False, 'O') == (1, 2)


def test_RandomAI_move_v2(monkeypatch):
    def fake(a):
        return (1, 2)
    monkeypatch.setattr('AI.choice', fake)
    game = UltimateTicTacToe()
    Ai = RandomAI(game)
    game.get_mini_board(0).set_move(0, 0, 'X')
    game.get_mini_board(0).set_move(1, 1, 'X')

    assert AI_move(game, Ai, 0, False, 'O') == (1, 2)


def test_RandomAI_get_board(monkeypatch):
    def fake(a):
        return 3
    monkeypatch.setattr('AI.choice', fake)
    game = UltimateTicTacToe()
    Ai = RandomAI(game)

    assert AI_board(game, Ai, None, False) == 3

# test_HardAI_board_get_board_that_can_win()
