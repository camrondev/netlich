import _bios as _b
import os
nl = _b.BIOS
TO_POST = lambda _loadedvar: _b._post.lg(f"%{_loadedvar}")
class UserInterface(nl):



    def __init__(self):
        super().__init__();                                                     _b._post.lg("INIT NL/BIOS/UserInterface")
        os.system(f"title master% netlich [{self.BIOS_CONTAINER}]")

        self.input_color = self.request_userinputcolor("r");                    TO_POST("input_color")
        self.haddr_color = self.sui_request_recvhaddrcolor();                   TO_POST("haddr_color")
        self.access      = self.request_useracslev("rw");                       TO_POST("access")
        

        if self.access == None:
            self.prntlines({f"{self.request_file_execname()} encountered a fatal error:": "red",
                            "This application lacks the permissions to operate. PERMISSION_ERROR": "r"})
            os.system("pause")
            _b.sys.exit()
        else:
            self.access_n_1  = str();                                           TO_POST("access_n_1")
            for _item in self.access[1]:
                self.access_n_1 = f"{self.access_n_1}{_item}"


        self.ui_c_lightpurple = self.BIOS_BSHCC("lpurple"); TO_POST("ui_c_lightpurple")
        self.ui_c_purple      = self.BIOS_BSHCC("purple");  TO_POST("ui_c_purple")
        self.ui_c_green       = self.BIOS_BSHCC("green");   TO_POST("ui_c_green")
        self.ui_c_lightblue   = self.BIOS_BSHCC("lblue");   TO_POST("ui_c_lightblue")
        self.ui_c_blue        = self.BIOS_BSHCC("blue");    TO_POST("ui_c_blue")
        self.ui_c_red         = self.BIOS_BSHCC("red");     TO_POST("ui_c_red")
        self.ui_c_reset       = self.BIOS_BSHCC("r");       TO_POST("ui_c_reset")
        self.ui_c_bold        = self.BIOS_BSHCC("bold");    TO_POST("ui_c_bold")#?  possibly deprecated w10
        self.ui_c_italic      = self.BIOS_BSHCC("italic");  TO_POST("ui_c_italic")#?


        self.prnt("notice: \033[32mApplication successfully loaded.")  # POST/LOG Endpoint, User-accessible UI after this point.


    def ui_display_header(self):
        _ = self.ui_c_reset
        self.prntlines({f" ┳┓ ┏┓ ┏┳┓ \033[95m┓ ┳┏┓┓┏ │{_} NETLich Build [NLV{self.request_productversion()}] (c) camrondev": "r",
                        f" ┃┃ ┣   ┃  \033[95m┃ ┃┃ ┣┫ │{_} {self.SYS_USER_PLATF}──NETLICH──{self.ui_c_lightpurple}Current Host─┐{self.ui_c_lightpurple}  nl\033[90m fws --creator": "r",
                        f" ┛┗ ┗┛  ┻  \033[95m┗┛┻┗┛┛┗ │[{self.sui_request_recvhaddrcolor()}{self.SYS_USER_HADDR}{_}{self.ui_c_lightpurple}]────────────────┘{_}  Use (\"net.help\")": "r"})


    # │┘ ┐ ┌ └─
    def clisten(self):
        os.system("pause")
        os.system("cls")
        self.ui_display_header()
        self.prnt(f"\033[90m│SYSTEM│DIRECTORY│ACCESS│")
        self.prnt(f"┌{self.ui_c_lightpurple}netlich{self.ui_c_lightblue}({self.ui_c_green}~{self.ui_c_lightblue}){self.ui_c_reset}─║{self.access[0]}\033[90m@{self.ui_c_green}{self.sui_request_recvpermissions_allow(self.access_n_1)}{self.ui_c_reset}║")
        _userinput = str(input(f"└{self.input_color}"))


UI = UserInterface()
UI.clisten()