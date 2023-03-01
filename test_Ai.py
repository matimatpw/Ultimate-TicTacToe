from ultimate_board import UltimateTicTacToe
from AI import HardAI, RandomAI


def test_AI_random_get_playable_boards_all():
    game = UltimateTicTacToe()
    bot = RandomAI(game)
    assert bot.AI_get_playable_boards() == [0, 1, 2, 3, 4, 5, 6, 7, 8]


def test_AI_random_get_playable_boards():
    game = UltimateTicTacToe()
    bot = RandomAI(game)
    game.set_uboard_move(game.get_mini_board(5), 0, 0, 'X')
    game.set_uboard_move(game.get_mini_board(5), 0, 1, 'X')
    game.set_uboard_move(game.get_mini_board(5), 0, 2, 'X')
    game.check_mini(5, 'X')
    assert bot.AI_get_playable_boards() == [0, 1, 2, 3, 4, 6, 7, 8]


def test_AI_get_random_board(monkeypatch):
    def fake(a):
        return 2
    monkeypatch.setattr('AI.choice', fake)
    game = UltimateTicTacToe()
    bot = RandomAI(game)
    assert bot.Ai_get_random_board() == 2


def test_AI_get_playable_moves_all():
    game = UltimateTicTacToe()
    bot = RandomAI(game)
    assert bot.AI_get_playable_moves(0) == [
        (0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)
        ]


def test_AI_get_playable_moves():
    game = UltimateTicTacToe()
    bot = RandomAI(game)
    game.set_uboard_move(game.get_mini_board(0), 0, 0, 'X')
    game.set_uboard_move(game.get_mini_board(0), 1, 0, 'X')
    game.set_uboard_move(game.get_mini_board(0), 2, 2, 'X')
    game.set_uboard_move(game.get_mini_board(0), 2, 0, 'X')
    assert bot.AI_get_playable_moves(0) == [
        (0, 1), (0, 2), (1, 1), (1, 2), (2, 1)
        ]


def test_AI_get_random_move(monkeypatch):
    def fake(a):
        return (2, 0)
    monkeypatch.setattr('AI.choice', fake)
    game = UltimateTicTacToe()
    bot = RandomAI(game)
    assert bot.Ai_get_random_move(0) == (2, 0)


def test_Ai_Hard_finish_win_row():
    game = UltimateTicTacToe()
    bot = HardAI(game)
    brd = game.get_mini_board(0)
    game.set_uboard_move(brd, 2, 0, 'O')
    game.set_uboard_move(brd, 2, 1, 'O')
    assert bot.Hard_get_finish_block(0) == (2, 2)


def test_Ai_Hard_finish_win__another_row():
    game = UltimateTicTacToe()
    bot = HardAI(game)
    brd = game.get_mini_board(0)
    game.set_uboard_move(brd, 1, 0, 'O')
    game.set_uboard_move(brd, 1, 2, 'O')
    assert bot.Hard_get_finish_block(0) == (1, 1)


def test_Ai_Hard_finish_win_col():
    game = UltimateTicTacToe()
    bot = HardAI(game)
    brd = game.get_mini_board(0)
    game.set_uboard_move(brd, 1, 0, 'O')
    game.set_uboard_move(brd, 0, 0, 'O')
    assert bot.Hard_get_finish_block(0) == (2, 0)


def test_Ai_Hard_finish_win_diag():
    game = UltimateTicTacToe()
    bot = HardAI(game)
    brd = game.get_mini_board(0)
    game.set_uboard_move(brd, 1, 1, 'O')
    game.set_uboard_move(brd, 0, 0, 'O')
    assert bot.Hard_get_finish_block(0) == (2, 2)


def test_Ai_Hard_finish_win_other_diag():
    game = UltimateTicTacToe()
    bot = HardAI(game)
    brd = game.get_mini_board(0)
    game.set_uboard_move(brd, 1, 1, 'O')
    game.set_uboard_move(brd, 0, 2, 'O')
    game.set_uboard_move(brd, 0, 1, 'X')
    assert bot.Hard_get_finish_block(0) == (2, 0)


def test_Ai_Hard_finish_None():
    game = UltimateTicTacToe()
    bot = HardAI(game)
    brd = game.get_mini_board(0)
    game.set_uboard_move(brd, 1, 1, 'O')
    game.set_uboard_move(brd, 0, 2, 'X')
    assert bot.Hard_get_finish_block(0) is None


def test_Ai_Hard_block_row():
    game = UltimateTicTacToe()
    bot = HardAI(game)
    brd = game.get_mini_board(0)
    game.set_uboard_move(brd, 1, 0, 'X')
    game.set_uboard_move(brd, 1, 1, 'X')
    assert bot.Hard_get_finish_block(0, 'X') == (1, 2)


def test_Ai_Hard_block_col():
    game = UltimateTicTacToe()
    bot = HardAI(game)
    brd = game.get_mini_board(0)
    game.set_uboard_move(brd, 1, 0, 'X')
    game.set_uboard_move(brd, 2, 0, 'X')
    assert bot.Hard_get_finish_block(0, 'X') == (0, 0)


def test_Ai_Hard_block_diag():
    game = UltimateTicTacToe()
    bot = HardAI(game)
    brd = game.get_mini_board(0)
    game.set_uboard_move(brd, 1, 1, 'X')
    game.set_uboard_move(brd, 2, 0, 'X')
    assert bot.Hard_get_finish_block(0, 'X') == (0, 2)


def test_Ai_Hard_block_diag_other():
    game = UltimateTicTacToe()
    bot = HardAI(game)
    brd = game.get_mini_board(0)
    game.set_uboard_move(brd, 2, 2, 'X')
    game.set_uboard_move(brd, 0, 0, 'X')
    assert bot.Hard_get_finish_block(0, 'X') == (1, 1)


def test_Ai_Hard_chose_block_move():
    game = UltimateTicTacToe()
    bot = HardAI(game)
    brd = game.get_mini_board(0)
    game.set_uboard_move(brd, 0, 2, 'X')
    game.set_uboard_move(brd, 2, 0, 'X')
    assert bot.Hard_chose_move(0) == (1, 1)


def test_Ai_Hard_chose_side(monkeypatch):
    def fake(arg):
        return (2, 1)
    monkeypatch.setattr('AI.choice', fake)

    game = UltimateTicTacToe()
    bot = HardAI(game)
    brd = game.get_mini_board(0)
    game.set_uboard_move(brd, 0, 0, 'X')
    game.set_uboard_move(brd, 2, 0, 'X')
    game.set_uboard_move(brd, 1, 2, 'X')
    game.set_uboard_move(brd, 0, 2, 'O')
    game.set_uboard_move(brd, 2, 2, 'O')
    game.set_uboard_move(brd, 1, 0, 'O')
    game.set_uboard_move(brd, 1, 1, 'O')  # zajety srodek
    assert bot.Hard_chose_move(0) == (2, 1)


def test_Ai_Hard_chose_finish():
    game = UltimateTicTacToe()
    bot = HardAI(game)
    brd = game.get_mini_board(0)
    game.set_uboard_move(brd, 0, 2, 'O')
    game.set_uboard_move(brd, 2, 0, 'O')
    assert bot.Hard_chose_move(0) == (1, 1)


def test_Ai_Hard_chose_oposite_cornerh():
    game = UltimateTicTacToe()
    bot = HardAI(game)
    brd = game.get_mini_board(0)
    game.set_uboard_move(brd, 0, 0, 'X')
    game.set_uboard_move(brd, 1, 1, 'O')
    assert bot.Hard_chose_move(0) == (2, 2)


def test_Ai_Hard_get_None():
    game = UltimateTicTacToe()
    bot = HardAI(game)
    brd = game.get_mini_board(0)
    game.set_uboard_move(brd, 0, 2, 'X')
    game.set_uboard_move(brd, 1, 0, 'X')
    assert bot.Hard_get_finish_block(0, 'X') is None


def test_Hard_get_centre():
    game = UltimateTicTacToe()
    bot = HardAI(game)
    brd = game.get_mini_board(0)
    game.set_uboard_move(brd, 0, 2, 'X')
    game.set_uboard_move(brd, 1, 0, 'X')
    assert bot.Hard_get_centre(0) == (1, 1)


def test_Hard_get_centre_None():
    game = UltimateTicTacToe()
    bot = HardAI(game)
    brd = game.get_mini_board(0)
    game.set_uboard_move(brd, 0, 2, 'X')
    game.set_uboard_move(brd, 1, 1, 'X')
    assert bot.Hard_get_centre(0) is None


def test_Hard_get_oposite_corner():
    game = UltimateTicTacToe()
    bot = HardAI(game)
    brd = game.get_mini_board(0)
    game.set_uboard_move(brd, 1, 1, 'O')
    game.set_uboard_move(brd, 0, 0, 'X')
    assert bot.Hard_get_oposite_corner(0) == (2, 2)


def test_Hard_chose_board_where_win():
    game = UltimateTicTacToe()
    bot = HardAI(game)
    brd = game.get_mini_board(0)
    game.set_uboard_move(brd, 0, 2, 'O')
    game.set_uboard_move(brd, 2, 0, 'O')
    assert bot.Hard_chose_board() == 0


def test_Hard_chose_board_where_block():
    game = UltimateTicTacToe()
    bot = HardAI(game)
    brd = game.get_mini_board(7)
    game.set_uboard_move(brd, 0, 2, 'X')
    game.set_uboard_move(brd, 2, 0, 'X')
    assert bot.Hard_chose_board() == 7


def test_Hard_chose_board_where_take_centre():
    game = UltimateTicTacToe()
    bot = HardAI(game)
    brd_zero = game.get_mini_board(0)
    brd_one = game.get_mini_board(1)
    brd_two = game.get_mini_board(2)
    game.set_uboard_move(brd_zero, 1, 1, 'O')
    game.set_uboard_move(brd_one, 1, 1, 'O')
    game.set_uboard_move(brd_two, 1, 1, 'O')
    assert bot.Hard_chose_board() == 3


def test_Hard_chose_board_where_take_oposite_corner():
    game = UltimateTicTacToe()
    bot = HardAI(game)
    brd_zero = game.get_mini_board(0)
    brd_one = game.get_mini_board(1)
    brd_two = game.get_mini_board(2)
    brd_three = game.get_mini_board(3)
    brd_four = game.get_mini_board(4)
    brd_five = game.get_mini_board(5)
    brd_six = game.get_mini_board(6)
    brd_svn = game.get_mini_board(7)
    brd_eight = game.get_mini_board(8)
    game.set_uboard_move(brd_zero, 1, 1, 'O')
    game.set_uboard_move(brd_two, 1, 1, 'O')
    game.set_uboard_move(brd_three, 1, 1, 'O')
    game.set_uboard_move(brd_four, 1, 1, 'O')
    game.set_uboard_move(brd_five, 1, 1, 'O')
    game.set_uboard_move(brd_six, 1, 1, 'O')
    game.set_uboard_move(brd_svn, 1, 1, 'O')
    game.set_uboard_move(brd_eight, 1, 1, 'O')
    game.set_uboard_move(brd_one, 1, 1, 'O')
    game.set_uboard_move(brd_svn, 0, 0, 'X')
    assert bot.Hard_chose_board() == 7


def test_take_any_other(monkeypatch):
    def fake(arg):
        return 6
    monkeypatch.setattr('AI.choice', fake)

    game = UltimateTicTacToe()
    bot = HardAI(game)
    brd_zero = game.get_mini_board(0)
    brd_one = game.get_mini_board(1)
    brd_two = game.get_mini_board(2)
    brd_three = game.get_mini_board(3)
    brd_four = game.get_mini_board(4)
    brd_five = game.get_mini_board(5)
    brd_six = game.get_mini_board(6)
    brd_svn = game.get_mini_board(7)
    brd_eight = game.get_mini_board(8)
    game.set_uboard_move(brd_zero, 1, 1, 'O')
    game.set_uboard_move(brd_one, 1, 1, 'O')
    game.set_uboard_move(brd_two, 1, 1, 'O')
    game.set_uboard_move(brd_three, 1, 1, 'O')
    game.set_uboard_move(brd_four, 1, 1, 'O')
    game.set_uboard_move(brd_five, 1, 1, 'O')
    game.set_uboard_move(brd_six, 1, 1, 'O')
    game.set_uboard_move(brd_svn, 1, 1, 'O')
    game.set_uboard_move(brd_eight, 1, 1, 'O')
    assert bot.Hard_chose_board() == 6
