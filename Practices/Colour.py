"""
Class for BOLD, UNDERLINE and Coloured stuffs
This class can be used a constants container that can be used for printing
different coloured strings
"""


class Colour:
    """
    This class can be used a constants container that can be used for printing
    different coloured strings
    """
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
