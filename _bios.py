import os, sys, socket, _post_log as _post, traceback, functools
from typing import NewType
#▒ ° ± ┘ ┐ ┌ └ ┼ ─ ├ ┤ ┴ ┬ │ ≤ ≥ · ♦ ≠ π £│┘ ┐ ┌ └

UserAccessLevel = NewType("UserAccessLevel", int)
SystemErrorCode = NewType("SystemErrorCode", int)
NLProcess       = NewType("NLProcess", str)
NFInfo          = NewType("NFInfo", str)
NFWarn          = NewType("NFWarn", str)
NFUI            = NewType("NFUI", str)

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
        
        self.BIOS_PRODUCT_VERSION = \
            {"ud/bios": 1.1,
             "ud/ui":   1.1,
             "ud/cmd":  0.0,
             "ud/misc": 2.3};                                                               TO_POST("BIOS_PRODUCT_VERSION")
        self.BIOS_ERR_CLIST = \
            {SystemErrorCode(0): "ERR_INSTANCE_NOT_FOUND"};                                 TO_POST("BIOS_ERR_CLIST")
        self.BIOS_LISTPLATF = \
            {"win32": "WIN32",
             "linux": "LINUX",
             "darwin":"MACOS",
             "java":  "VJAVA",
             "cli":   "COLIN"};                                                             TO_POST("BIOS_LISTPLATF")
        self.BIOS_LISTERROR = \
            {"ERR_0": "Could not parse SEC, 0.",
             "ERR_INSTANCE_NOT_FOUND": "Unable to verify a local NL Network."};             TO_POST("BIOS_LISTERROR")

        self.BIOS_LOADBSHCC = \
            {"lpurple":"\033[95m",
             "purple": "\033[35m",
             "green":  "\033[32m",
             "lblue":  "\033[94m",
             "blue":   "\033[34m",
             "lred":   "\033[91m",
             "gray":   "\033[90m",
             "red":    "\033[31m",
             "bold":   "\033[1m",
             "italic": "\033[3m",
             "r":      "\033[0m"};                                                          TO_POST("BIOS_LOADBSHCC")
        
        self.BIOS_BSHCC     = lambda _color: \
            self.BIOS_LOADBSHCC[_color];                                                    TO_POST("BIOS_BSHCC")
        
        self.BIOS_LISTWIDGET_ID = \
            {"network_status": self.request_netty()};                                       TO_POST("BIOS_LISTWIDGET_ID")
        
        self.BIOS_LISTNOTIFICATION_TYPE = \
            {NFInfo: f"{self.BIOS_BSHCC("lblue")}(?)",
             NFWarn: f"{self.BIOS_BSHCC("lred")}(!)",
             NFUI:   f"{self.BIOS_BSHCC("gray")}(×)"};                                      TO_POST("BIOS_LISTNOTIFICATION_TYPE")
        
        
        ### BIOS Security & SecureUI Settings.

        self.BIOS_SECUREUI_SHOWHOSTADDR     = False;                                        TO_POST("BIOS_SECUREUI_SHOWHOSTADDR")
        self.BIOS_SECUREUI_SHOWHOSTADDR_CLR = \
            {True:  "\033[0m\033[4m",
             False: "\033[30m\033[4m"};                                                     TO_POST("BIOS_SECUREUI_SHOWHOSTADDR_CLR")
        self.BIOS_SECUREUI_PERMS_REQUESTED  = None;                                         TO_POST("BIOS_SECUREUI_PERMS_REQUESTED")
        self.BIOS_SECUREUI_INSTANCE_FORMAT  = \
            {"p/netlich_main": NLProcess};                                                  TO_POST("BIOS_SECUREUI_INSTANCE_FORMAT")
        

    ##= - - =##
    # Methods #
    ##= - - =##


    def prnt(self, _message: str = None, _color: str = "r") -> None:
        """
        Print a message to the screen.
        """
        print(f"{self.BIOS_BSHCC(_color)}{_message}\033[0m")


    def prntlines(self, _lines: dict = None) -> None:
        """
        Print multiple lines of messages to the screen.
        """
        if not _lines:
            return
        
        for _line in _lines:
            self.prnt(_line, _lines[_line])


    def prnterr(self, _code: SystemErrorCode = 0) -> callable:
        """
        Print an error code to the screen.\n
        *No endpoint.*
        """
        return self.notification(f"{self.request_errstring(self.err(_code))}", NFWarn)
    

    def notification(self, _message: str = "No message.", _type = None) -> None:
        """
        Print a formatted notification to the screen.
        """
        if _type == None:
            _type = NFUI
        
        try:
            if not _type in self.BIOS_LISTNOTIFICATION_TYPE:
                raise KeyError("Invalid notification type.")
            
            self.prnt(f"{self.BIOS_LISTNOTIFICATION_TYPE[_type]} {_message}")

        except KeyError:
            return
        
    
    def list_to_string(self, _target_list: list = None, _fileformat: bool = False) -> str: #for string -> string.split -> string
        """
        Combines a list of strings.\n
        *Includes whitespace.*
        """
        if _target_list == None:
            return 
        if not isinstance(_target_list[0], str):
            return
        
        _value = ""
        if _fileformat:
            for _item in _target_list:

                for _char in _item:
                    _value = f"{_value}{_char}"
                _value = f"{_value}\\"
        else:
            for _item in _target_list:

                for _char in _item:
                    _value = f"{_value}{_char}"

        return _value


    def title(self, _string: str = None) -> None:
        """
        Set the title of the window.
        """
        if _string == None:
            return

        os.system(f"title {_string}/net")


    ##= - - =##
    # Request #
    ##= - - =##


    def request_useracslev(self, _flags: str = None) -> tuple[UserAccessLevel, list]:
        """
        **GET** User Access Level by Permission, Restrictions
        """
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
        """
        **GET** Product Version String
        """
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
        """
        **GET** Input Color
        """
        try:
            return self.BIOS_BSHCC(_color)
        
        except KeyError:
            return
    

    def request_file_execname(self) -> str:
        """
        **GET** File Name of BIOS
        """
        return self.BIOS_EXEC_FILE
    

    def request_errstring(self, _error: str = "ERR_0") -> str:
        """
        **GET** Error Message by Code
        """
        try:
            return self.BIOS_LISTERROR[_error]
        
        except KeyError:
            return
    

    def request_system_platform(self, _platform: str = sys.platform) -> str:
        """
        **GET** Platform String by OS
        """
        return self.BIOS_LISTPLATF[_platform]
    

    def request_netty(self) -> bool:
        """
        **GET** NetLich-type Network Connectivity Status
        """
        _netty = False

        return _netty

    
    ## = = - - # # # # = = -##
    # SecureUI | Requests /  #
    ## = = - - # # # # = = -##


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
    

    def sui_generate_env(self) -> None:
        _container = self.BIOS_CONTAINER
        if not os.path.exists(_container + "\\meta"):
            self.notification("An error occurred referencing \\meta.", NFInfo)
            self.notification(f"Creating META folder @ {self.BIOS_BSHCC("r")}" \
                              f"{_container}{self.BIOS_BSHCC('green')}\\[meta]", NFInfo)
            os.mkdir(f"{_container}\\meta")

    
    def err(self, _code: SystemErrorCode = 0) -> str:
        for _identifier in self.BIOS_ERR_CLIST:
            if _code == _identifier:

                return self.BIOS_ERR_CLIST[SystemErrorCode(_code)]
            continue

        return "ERR_0"
    