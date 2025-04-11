import os, sys, socket, _post_log as _post, traceback, functools
from typing import NewType
#▒ ° ± ┘ ┐ ┌ └ ┼ ─ ├ ┤ ┴ ┬ │ ≤ ≥ · ♦ ≠ π £│┘ ┐ ┌ └

UserAccessLevel = NewType("UserAccessLevel", int)
SystemErrorCode = NewType("SystemErrorCode", int)

TO_POST = lambda _loadedvar: _post.lg(f"BIOS/{_loadedvar}")

class BIOS:
    """
    Handles POST, UI, and uIN.
    """
    _post.lg("INIT NL/BIOS")
    def __init__(self):
        ##= - - =##
        # SysVars #
        ##= - - =##
        self.SYS_DRIVE_CHAR = __file__[0].upper();                                          TO_POST("SYS_DRIVE_CHAR")
        self.SYS_USER_PLATF = sys.platform.upper();                                         TO_POST("SYS_USER_PLATF")
        self.SYS_USER_HNAME = socket.gethostname();                                         TO_POST("SYS_USER_HNAME")
        self.SYS_USER_HADDR = socket.gethostbyname(self.SYS_USER_HNAME);                    TO_POST("SYS_USER_HADDR")
        self.BIOS_EXEC_FILE = __file__.replace(f"{__file__[0]}:", f"{self.SYS_DRIVE_CHAR}:");TO_POST("BIOS_EXEC_FILE")

        
        self.BIOS_ACS_FLAGS = ['r', 'w'];                                                   TO_POST("BIOS_ACS_FLAGS")
        self.BIOS_ACS_MAXLV = len(self.BIOS_ACS_FLAGS);                                     TO_POST("BIOS_ACS_MAXLV")

        self.BIOS_CONTAINER = os.getcwd();                                                  TO_POST("BIOS_CONTAINER")
        self.BIOS_VERSION   = "1.0";                                                        TO_POST("BIOS_VERSION")
        
        self.BIOS_PRODUCT_VERSION = {"ud/bios": 0.6,
                                     "ud/ui":   1.0,
                                     "ud/cmd":  0.0,
                                     "ud/misc": 2.1};                                       TO_POST("BIOS_PRODUCT_VERSION")
        self.BIOS_ERR_CLIST = {SystemErrorCode(0): "ERR_INSTANCE_NOT_FOUND"};               TO_POST("BIOS_ERR_CLIST")
        self.BIOS_LISTPLATF = {"win32": "WIN32",
                               "linux": "LINUX",
                               "darwin":"MACOS",
                               "java":  "VJAVA",
                               "cli":   "COLIN"};                                           TO_POST("BIOS_LISTPLATF")
        self.BIOS_LISTERROR = {"ERR_0": "Could not parse SEC, 0.",
                               "ERR_INSTANCE_NOT_FOUND": "Unable to verify a local NL Network."};TO_POST("BIOS_LISTERROR")
        
        ### Load permitted BASH COLORCODE list.

        self.BIOS_LOADBSHCC = {"lpurple":"\033[95m",
                               "purple": "\033[35m",
                               "green":  "\033[32m",
                               "lblue":  "\033[94m",
                               "blue":   "\033[34m",
                               "lred":   "\033[91m",
                               "gray":   "\033[90m",
                               "red":    "\033[31m",
                               "bold":   "\033[1m",
                               "italic": "\033[3m",
                               "r":      "\033[0m"};                                        TO_POST("BIOS_LOADBSHCC")
        
        self.BIOS_BSHCC     = lambda _color: \
            self.BIOS_LOADBSHCC[_color];                                                    TO_POST("BIOS_BSHCC")
        
        self.BIOS_LISTWIDGET_ID = {"network_status": self.request_netty()};                 TO_POST("BIOS_LISTWIDGET_ID")
        
        
        ### BIOS Security & SecureUI Settings.

        self.BIOS_SECUREUI_SHOWHOSTADDR     = False;                                         TO_POST("BIOS_SECUREUI_SHOWHOSTADDR")
        self.BIOS_SECUREUI_SHOWHOSTADDR_CLR = {True:  "\033[0m\033[4m",
                                               False: "\033[30m\033[4m"};                   TO_POST("BIOS_SECUREUI_SHOWHOSTADDR_CLR")
        self.BIOS_SECUREUI_PERMS_REQUESTED  = None;                                         TO_POST("BIOS_SECUREUI_PERMS_REQUESTED")
        
    ##= - - =##
    # Methods #
    ##= - - =##
    def prnt(self, _message: str = None, _color: str = "r") -> None:
        print(f"{self.BIOS_BSHCC(_color)}{_message}\033[0m")


    def prntlines(self, _lines: dict = None) -> None:
        if not _lines:
            return
        
        for _line in _lines:
            self.prnt(_line, _lines[_line])


    def prnterr(self, _code: SystemErrorCode = 0) -> callable:
        return self.prnt(f"{self.request_errstring(self.err(_code))}", "lred")
    

    def title(self, _string: str = None) -> None:
        if _string == None:
            return

        os.system(f"title {_string}/net")

    ##= - - =##
    # Request #
    ##= - - =##
    def request_useracslev(self, _flags: str = None) -> tuple[UserAccessLevel, list]:
        if not _flags:
            return 
        self.BIOS_SECUREUI_PERMS_REQUESTED = _flags

        _useracslev  = 0
        _denied = []
        for _char in _flags:
            if _char in self.BIOS_ACS_FLAGS:
                _useracslev += 1
            else:
                _denied.append(_char)

        return (UserAccessLevel(_useracslev), _denied)
    

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
    

    def request_userinputcolor(self, _color: str = "r") -> str:
        try:
            return self.BIOS_BSHCC(_color)
        except KeyError:
            return
    

    def request_file_execname(self) -> str:
        return self.BIOS_EXEC_FILE
    

    def request_errstring(self, _error: str = "ERR_0") -> str:
        try:
            return self.BIOS_LISTERROR[_error]
        except KeyError:
            return
    

    def request_system_platform(self, _platform: str = sys.platform) -> str:
        return self.BIOS_LISTPLATF[_platform]
    

    def request_netty(self) -> bool:
        _netty = False

        return _netty

    
    ## = = - - # # # # = = -
    # SecureUI | Requests /
    ## = = - - # # # # = = -
    def sui_request_recvhaddrcolor(self) -> str:
        return self.BIOS_SECUREUI_SHOWHOSTADDR_CLR \
                   [self.BIOS_SECUREUI_SHOWHOSTADDR]
    

    def sui_request_recvpermissions_allow(self, _filter: str = None) -> str:
        if _filter == None:
            return self.BIOS_SECUREUI_PERMS_REQUESTED
        
        _filtered = self.BIOS_SECUREUI_PERMS_REQUESTED
        for _char in _filter:
            if _char in _filtered:
                _filtered = _filtered.replace(_char, "")
        return _filtered

    
    def err(self, _code: SystemErrorCode = 0) -> str:
        for _identifier in self.BIOS_ERR_CLIST:
            if _code == _identifier:
                return self.BIOS_ERR_CLIST[SystemErrorCode(_code)]
            continue
        return "ERR_0"