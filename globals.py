possible_values = [0, 1, 2]
possible_players = ['X', 'O']
possible_boards = [0, 1, 2, 3, 4, 5, 6, 7, 8]
possible_bots = ['Random', 'Hard']


def red(object):
    """Zwraca czerwony element"""
    red = ['\x1b[38;2;255;0;0m', '\x1b[0m']
    red.insert(1, object)
    color_object = "".join(red)
    return color_object


def blue(object):
    """Zwraca niebieski element"""
    red = ['\x1b[38;2;0;110;250m', '\x1b[0m']
    red.insert(1, object)
    color_object = "".join(red)
    return color_object


def green(object):
    """Zwraca zielony element"""
    red = ['\x1b[38;2;0;250;0m', '\x1b[0m']
    red.insert(1, object)
    color_object = "".join(red)
    return color_object


def bold(object):
    """Zwraca pogrubiony element"""
    bolder = ['\033[1m', '\033[0m']
    bolder.insert(1, object)
    bold_object = "".join(bolder)
    return bold_object


def uline(object):
    """Zwraca podkreslony emlement"""
    underline = ['\033[4m', '\033[0m']
    underline.insert(1, object)
    ulined = "".join(underline)
    return ulined
