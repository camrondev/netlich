import os, sys, socket
from typing import NewType
#▒ ° ± ┘ ┐ ┌ └ ┼ ─ ├ ┤ ┴ ┬ │ ≤ ≥ · ♦ ≠ π £
UserAccessLevel = NewType("UserAccessLevel", int)
SystemErrorCode = NewType("SystemErrorCode", int)

class BIOS:
    """
    Handles POST, UI, and uIN.
    """
    print("LD NL/BIOS/-->++")
    def __init__(self):
        ##= - - =##
        # SysVars #
        ##= - - =##
        self.SYS_DRIVE_CHAR = __file__[0].upper(); print("LD BIOS/SYS_DRIVE_CHAR.")
        self.SYS_USER_PLATF = sys.platform.upper(); print("LD BIOS/SYS_USER_PLATF: OS.")
        self.SYS_USER_HNAME = socket.gethostname(); print("LD BIOS/SYS_USER_HNAME.")
        self.SYS_USER_UIP   = socket.gethostbyname(self.SYS_USER_HNAME); print("LD BIOS/SYS_USER_UIP: HADDR.")
        self.BIOS_EXEC_FILE = __file__.replace(f"{__file__[0]}:", f"{self.SYS_DRIVE_CHAR}:")
        print("LD BIOS/BIOS_EXEC_FILE: BOOT.")
        
        self.BIOS_ACS_FLAGS = ['-r', '-w']; print("LD BIOS/BIOS_ACS_FLAGS: PRM_FLAGS.")
        self.BIOS_ACS_MAXLV = len(self.BIOS_ACS_FLAGS); print("LD BIOS/BIOS_ACS_MAXLV.")

        self.BIOS_CONTAINER = os.getcwd(); print("LD BIOS/BIOS_CONTAINER: WORKING DIRECTORY.")
        self.BIOS_VERSION   = "1.0"; print("LD BIOS/BIOS_VERSION: APP VERSION.")
        
        self.BIOS_PRODUCT_VERSION = {"ud/bios": 0.2,
                                     "ud/ui":   0.3,
                                     "ud/cmd":  0.0,
                                     "ud/misc": 0.1}; print("LD BIOS/BIOS_PRODUCT_VERSION: /BI/UI/CM/MISC..")
        
        ### Load permitted BASH COLORCODE list.

        self.BIOS_LOADBSHCC = {"lpurple":"\033[95m",
                               "purple": "\033[35m",
                               "green":  "\033[32m",
                               "lblue":  "\033[94m",
                               "blue":   "\033[34m",
                               "red":    "\033[31m",
                               "bold":   "\033[1m",
                               "italic": "\033[3m",
                               "r":      "\033[0m"}; print("LD BIOS/BIOS_LOADBSHCC: NETLICH/BASH CCx9 ESCAPE SEQ..")
        
        self.BIOS_BSHCC     = lambda _color: \
            self.BIOS_LOADBSHCC[_color]; print("LD BIOS/BIOS_BSHCC: CCx9 ESCAPE SEQ. CALL.")
        
        
        ### BIOS Security & SecureUI Settings.

        self.BIOS_SECUREUI_SHOWHOSTADDR = False; print("LD BIOS/BIOS_SECUREUI_SHOWHOSTADDR: ToggleHADDR. SecureUI.")
        self.BIOS_SECUREUI_SHOWHOSTADDR_CLR = {True:  "\033[0m\033[4m",
                                               False: "\033[30m\033[4m"}; print("LD BIOS/BIOS_SECUREUI_SHOWHOSTADDR_CLR: CCx2 ESCAPE SEQ.: ToggleHADDR.")
        
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