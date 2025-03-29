import os, sys, socket
from typing import NewType
#▒ ° ± ┘ ┐ ┌ └ ┼ ─ ├ ┤ ┴ ┬ │ ≤ ≥ · ♦ ≠ π £
UserAccessLevel = NewType("UserAccessLevel", int)
SystemErrorCode = NewType("SystemErrorCode", int)

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
        self.SYS_USER_HNAME = socket.gethostname()
        self.SYS_USER_UIP   = socket.gethostbyname(self.SYS_USER_HNAME)
        self.BIOS_EXEC_FILE = __file__.replace(f"{__file__[0]}:", f"{self.SYS_DRIVE_CHAR}:")
        
        self.BIOS_ACS_FLAGS = ['-r', '-w']
        self.BIOS_ACS_MAXLV = len(self.BIOS_ACS_FLAGS)

        self.BIOS_CONTAINER = os.getcwd()
        self.BIOS_VERSION   = "1.0"
        
        self.BIOS_PRODUCT_VERSION = {"ud/bios": 0.1,
                                     "ud/ui":   0.1,
                                     "ud/cmd":  0.0,
                                     "ud/misc": 0.1}
        
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
        
        
        ### BIOS Security & SecureUI Settings.

        self.BIOS_SECUREUI_SHOWHOSTADDR = False
        self.BIOS_SECUREUI_SHOWHOSTADDR_CLR = {True:  "\033[0m\033[4m",
                                               False: "\033[30m\033[4m"}
        
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

    ##= - - =##
    # Request #
    ##= - - =##
    def request_useracslev(self, _flags: str = None) -> tuple[UserAccessLevel, list]:
        if not _flags:
            return 
        
        _iter, _deny = 0, []
        for _char in _flags:
            if _char in self.BIOS_ACS_FLAGS:
                _iter += 1
                continue
            _deny.append(_char)

        return (UserAccessLevel(_iter), _deny)
    

    def request_productversion(self) -> str:
        _string = str()
        _base_n = self.BIOS_PRODUCT_VERSION
        
        _parse_bios = str(_base_n["ud/bios"]).replace(".", "")
        _parse_ui   = str(_base_n["ud/ui"]).replace(".", "")
        _parse_cmd  = str(_base_n["ud/cmd"]).replace(".", "")
        _parse_misc = str(_base_n["ud/misc"]).replace(".", "")

        _string = f"{self.BIOS_VERSION}." \
                 f"{_parse_bios}.{_parse_ui}." \
                 f"{_parse_cmd}.{_parse_misc}"
        
        return _string


    
    def err(self, _code: SystemErrorCode = 0):
        ...