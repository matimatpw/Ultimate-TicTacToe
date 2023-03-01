class MoveError(Exception):
    pass


class InvalidValueError(Exception):
    def __init__(self, *args) -> None:
        body = "Wrong value error! ->"
        super().__init__(f"{body} row:'{args[0]}' column:'{args[1]}'")


class InvalidBoardError(Exception):
    def __init__(self, arg) -> None:
        body = "Wrong value error! ->"
        super().__init__(f"{body} board_number: '{arg}'")


class InvalidPlayerError(Exception):
    def __init__(self, arg) -> None:
        super().__init__(f"Wrong player error! -> '{arg}'")


class WrongTypeError(Exception):
    def __init__(self, *args) -> None:
        body = "Wrong type error! ->"
        super().__init__(f"{body} row:'{args[0]}' column:'{args[1]}'")


class BoardFinishedError(Exception):
    pass


class WrongMoveError(Exception):
    pass


class BotStartGameError(Exception):
    pass
