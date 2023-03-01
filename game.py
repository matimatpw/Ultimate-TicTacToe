from operator import itemgetter as iget
from globals import possible_players, possible_bots
from ultimate_board import UltimateTicTacToe
from errors import (
    InvalidValueError, MoveError,
    WrongMoveError, BoardFinishedError,
    BotStartGameError, InvalidBoardError
)
from print_uboard import print_ultimate_board, mark_winner
from globals import bold, uline, red
from AI import RandomAI, HardAI


def chose_bot(gm):
    """Słuzy do wyboru rodzaju bota
        Zwraca obiekt wybranego bota
    """
    bot_specify = True
    while bot_specify:
        bot = input('Wybierz rodzaj bota (Random lub Hard): ').title().strip()
        if bot not in possible_bots:
            print('Wrong bot!')
        else:
            bot_specify = False
    if bot == 'Random':
        return RandomAI(gm)
    else:
        return HardAI(gm)


def game_config(bot, plr):
    """Ustawia wartośći początkowe gry. Zwraca słownik tych wartośći"""
    if plr.upper() not in possible_players:
        quit("Wrong player! -> ('O' or 'X')")

    config = {
        'gameon': True,
        'brd_spec': False,
        'next_brd': None,
    }

    if type(bot) == HardAI:
        hard_bot = True
        bot_info = "Mode Hard bot"
    elif type(bot) == RandomAI:
        hard_bot = False
        bot_info = "Mode Random bot"

    config.update({'bot': hard_bot, 'bot_info': bot_info})
    return config


def set_move(ugame: UltimateTicTacToe, next_brd, plr):
    """Sprawdza poprawność wykonanego ruchu oraz ustawia
        i zwraca ruch na planszy
    """
    run = True
    while run:
        try:
            row = int(input('Chose row: ').strip())
            col = int(input('Chose column: ').strip())
            board = ugame.get_mini_board(next_brd)
            ugame.set_uboard_move(board, row, col, plr)
            run = False
        except MoveError:
            print(bold('Board not selected!'))
        except ValueError:
            print(bold('Incorrect move! (0-2)'))
        except InvalidValueError:
            print(bold('Incorret move!'))
        except WrongMoveError:
            print(bold('Move is occupied!'))
    return (row, col)


def set_board(ugame: UltimateTicTacToe, next_brd, brd_spec):
    """Sprawdza poprawność wybranej planszy oraz zwraca
    plansze na której bedzie prowadzona rozgrywka
    """
    run = True
    while run:
        try:
            if not brd_spec:  # jesli mozna wybrac plansze
                next_brd = int(input('Chose board: ').strip())

            ugame.set_uboard(next_brd)
            brd_spec = True
            print(uline(f"Player 'X' play on board number '{next_brd}'"))
            run = False
        except ValueError:
            print(bold('Wrong board! (0-8)'))
        except InvalidBoardError:
            print(bold('Chose correct board! (0-8)'))
        except BoardFinishedError:
            print(bold('Board finished!'))
            brd_spec = False
    return next_brd


def check_ultimate(ugame: UltimateTicTacToe, plr):
    """Sprawdza czy i w jaki sposób gra została zakończona"""
    if ugame.check_ultimate_win(plr):
        print_ultimate_board(ugame)
        print(f"'{plr}' won. {red(bold('~GAME OVER~'))}".center(70))
        return True
    elif ugame.check_ultimate_draw():
        print_ultimate_board(ugame)
        print(f"Ultimate Draw! {red(bold('~GAME OVER~'))}".center(70))
        return True
    return None


def AI_move(ugame: UltimateTicTacToe, Ai, next_brd, hard_mode, plr):
    """Funkcja służy do wykonywania ruchu przez bota
        Zwraca krotke ruchu (wiersz, kolumna)
    """
    if not hard_mode:  # random
        move = Ai.Ai_get_random_move(next_brd)
    else:  # hard
        move = Ai.Hard_chose_move(next_brd)

    row, col = move
    board = ugame.get_mini_board(next_brd)
    ugame.set_uboard_move(board, row, col, plr)
    return (row, col)


def AI_board(ugame: UltimateTicTacToe, Ai, next_brd, hard_mode):
    """Funkcja służy do wybierania planszy przez bota
        Zwraca numer wybranej planszy
    """
    try:
        ugame.set_uboard(next_brd)
    except BoardFinishedError:
        if not hard_mode:
            next_brd = Ai.Ai_get_random_board()
        else:
            next_brd = Ai.Hard_chose_board()
    except BotStartGameError:
        if not hard_mode:
            next_brd = Ai.Ai_get_random_board()
        else:
            next_brd = Ai.Hard_chose_board()
    return next_brd


def play(game: UltimateTicTacToe, Ai: HardAI or RandomAI, player='X'):
    """
    Funkcja umożliwia przeporwadzenie rozgrywki.
    Przyjmuje 3 argumenty :
    ~obiekt gry : 'UltimateTicTacToe()'
    ~obiekt bota : 'HardAI()' lub 'RandomAI()' (inteligentny lub losowy)
    ~symbol gracza który ma zaczynać ('X' lub 'O')
    """
    # konfiguracja poczatkowa
    config = game_config(Ai, player)
    values = iget('gameon', 'brd_spec', 'next_brd', 'bot', 'bot_info')(config)
    gameon, board_specify, next_board, hard_bot, bot_info = values

    while gameon:
        print(bold(uline(bot_info)).center(58))
        print_ultimate_board(game)
        if player.upper() == 'X':
            run_plr = True
        else:
            run_plr = False

        # tura AI
        if not run_plr:
            next_board = AI_board(game, Ai, next_board, hard_bot)
            row, col = AI_move(game, Ai, next_board, hard_bot, player)
            print(uline(f"Ai 'O' play on board number '{next_board}'"))
            board_specify = True

        # tura gracza
        if run_plr:
            next_board = set_board(game, next_board, board_specify)
            row, col = set_move(game, next_board, player)

        game.check_mini(next_board, player)
        mark_winner(game, next_board)

        if check_ultimate(game, player):
            gameon = False

        next_board = game.next_board(row, col)
        player = game.player_switch(player)


if __name__ == "__main__":
    game = UltimateTicTacToe()
    Ai = chose_bot(game)
    play(game, Ai)
