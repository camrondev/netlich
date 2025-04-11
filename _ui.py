import _bios as _b
import os
NL      = _b.BIOS
POST    = _b._post
TO_POST = lambda _loadedvar: POST.mountvar(f"%{_loadedvar}")

class UserInterface(NL):
    def __init__(self, _source = None):
        super().__init__();                                 POST.lg("INIT NL/BIOS/UserInterface")
        self.title("Operating System")
        self.input_color = self.request_userinputcolor("r");TO_POST("input_color")
        self.haddr_color = self.sui_request_recvhaddrcolor();TO_POST("haddr_color")
        self.access      = self.request_useracslev("rw");   TO_POST("access")
        self.access_n_1  = self.access[1];                  TO_POST("access_n_1")
        self.local_netty = False;                           TO_POST("local_netty")
        self.widget_bar  = []

        if _source == None:
            _source = "main"
        self.ui_instance = _source;                          TO_POST("ui_instance")

        self.ui_c_lightpurple = self.BIOS_BSHCC("lpurple"); TO_POST("ui_c_lightpurple")
        self.ui_c_purple      = self.BIOS_BSHCC("purple");  TO_POST("ui_c_purple")
        self.ui_c_green       = self.BIOS_BSHCC("green");   TO_POST("ui_c_green")
        self.ui_c_lightblue   = self.BIOS_BSHCC("lblue");   TO_POST("ui_c_lightblue")
        self.ui_c_blue        = self.BIOS_BSHCC("blue");    TO_POST("ui_c_blue")
        self.ui_c_lred        = self.BIOS_BSHCC("lred");    TO_POST("ui_c_lred")
        self.ui_c_gray        = self.BIOS_BSHCC("gray");    TO_POST("ui_c_gray")
        self.ui_c_red         = self.BIOS_BSHCC("red");     TO_POST("ui_c_red")
        self.ui_c_reset       = self.BIOS_BSHCC("r");       TO_POST("ui_c_reset")
        self.ui_c_bold        = self.BIOS_BSHCC("bold");    TO_POST("ui_c_bold")#?  possibly deprecated w10
        self.ui_c_italic      = self.BIOS_BSHCC("italic");  TO_POST("ui_c_italic")#?

        self.ui_s_col         = "│";                        TO_POST("ui_s_col")
        self.ui_s_botRi       = "┌";                        TO_POST("ui_s_botRi")
        self.ui_s_botLe       = "┐";                        TO_POST("ui_s_botLe")
        self.ui_s_topRi       = "└";                        TO_POST("ui_s_topRi")
        self.ui_s_topLe       = "┘";                        TO_POST("ui_s_topLe")

        #CHECK NL NETWORK STATUS

        _b._post.flash()
        self.prnt("notice: \033[32mApplication successfully loaded.")  # POST/LOG Endpoint, User-accessible UI after this point.

    def ui_getwidget(self, _widget_id: str = None):
        if _widget_id == None:
            return

        return self.BIOS_LISTWIDGET_ID[_widget_id]


    def ui_display_header(self) -> None:
        _           = self.ui_c_reset
        _haddrcolor = self.sui_request_recvhaddrcolor()
        _hosthidden = "visible"
        _hnamecolor = "\033[90m"
        match _haddrcolor:
            case "\033[30m\033[4m":
                _hosthidden = "invisible"
                _hnamecolor = "\033[30m"
            case _:
                _hosthidden = "visible"
                _hnamecolor = "\033[90m"

        _uidh_top = f" ┳┓ ┏┓ ┏┳┓ \033[95m┓ ┳┏┓┓┏ │{_}NLBuild {self.request_productversion()} © camrondev @" \
                                                    f"{self.ui_c_gray}fws --creator"
        _uidh_mid = f" ┃┃ ┣   ┃  \033[95m┃ ┃┃ ┣┫ │{_}"
        _uidh_bot = f" ┛┗ ┗┛  ┻  \033[95m┗┛┻┗┛┛┗ │{_}"

        self.prntlines({_uidh_top: "r", _uidh_mid: "r", _uidh_bot: "r"})


    # │┘ ┐ ┌ └─
    def ui_listen_uin(self):
        os.system("pause")
        os.system("cls")
        self.ui_display_header()

        _widget = self.ui_getwidget("network_status")
        _direct = ...
        self.prnt(f"{self.ui_s_botRi}{self.ui_c_lightpurple}netlich{self.ui_c_lightblue}({self.ui_c_green}{_direct}{self.ui_c_lightblue}){_widget}")
        _uin = str(input(f"{self.ui_s_topRi}{self.input_color}"))
        


UI = UserInterface()
UI.ui_listen_uin()