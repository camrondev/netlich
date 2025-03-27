import os, sys
from typing import NewType
#▒ ° ± ┘ ┐ ┌ └ ┼ ─ ├ ┤ ┴ ┬ │ ≤ ≥ · ♦ ≠ π £
UserAccessLevel = NewType("UserAccessLevel", int)

class BIOS:
    """
    Handles POST, UI, and uIN.
    """

    def __init__(self):
        ##= - - =##
        # SysVars #
        ##= - - =##
        self.SYS_DRIVE_CHAR = __file__[0].upper()
        self.SYS_USER_PLATF = sys.platform.upper()
        self.BIOS_EXEC_FILE = __file__.replace(f"{__file__[0]}:", f"{self.SYS_DRIVE_CHAR}:")

        self.BIOS_CONTAINER = os.getcwd()
        self.BIOS_VERSION   = "1.00.0"
        
        ### Load permitted BASH COLORCODE list.

        self.BIOS_LOADBSHCC = {"lpurple":"\033[95m",
                               "purple": "\033[35m",
                               "green":  "\033[32m",
                               "blue":   "\033[34m",
                               "red":    "\033[31m",
                               "bold":   "\033[1m",
                               "italic": "\033[3m",
                               "r":      "\033[0m"}
        
        self.BIOS_BSHCC     = lambda _color: \
            self.BIOS_LOADBSHCC[_color]
        
    ##= - - =##
    # Methods #
    ##= - - =##
    def prnt(self, _message: str = None, _color: str = "r"):
        os.system(f"echo {self.BIOS_BSHCC(_color)}{_message}\033[0m")


    def prntlines(self, _lines: dict = None):
        if not _lines:
            return
        for _line in _lines:
            self.prnt(_line, _lines[_line])