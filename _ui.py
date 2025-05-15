import _bios as _b
import os, _boot
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
        self.widget_bar  = str();                           TO_POST("widget_bar")
        self.wid_con_src = 0;                               TO_POST("wid_con_src")

        if _source == None:
            _source = list(self.BIOS_SECUREUI_INSTANCE_FORMAT.keys())[0]
        self.ui_instance = _source;                         TO_POST("ui_instance")

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

        _b._post.flash()
        self.prnt("\033[32mApplication successfully loaded.")  # POST/LOG Endpoint, User-accessible UI after this point.


    def ui_widget(self, _wid_content: list = None) -> str:
        """
        Widget Functionality for the CLI.  #1.0.17.15.00.45
        """
        if not self.widget_bar:
            self.widget_bar = str()
        if _wid_content == None:
            self.widget_bar = "No widgets."
            return self.widget_bar
        
        for id in _wid_content:
            self.widget_bar  = f"{self.BIOS_LISTWIDGET_ID[id]} {self.ui_c_lightblue}:{self.ui_c_reset} "
            self.wid_con_src += 1

        return self.widget_bar


    def ui_display_header(self) -> None:
        _           = self.ui_c_reset
        _uidh_top = f" ╔╗╔ ╔═╗ ╔╦╗ \033[95m╦  ╦╔═╗╦ ╦ │{_}NLBuild {self.request_productversion()} © camrondev @" \
                                                    f"{self.ui_c_gray}fws --creator"
        _uidh_mid = f" ║║║ ║╣   ║  \033[95m║  ║║  ╠═╣ │{_}"
        _uidh_bot = f" ╝╚╝ ╚═╝  ╩  \033[95m╩═╝╩╚═╝╩ ╩ │{_}"
        _uidh_abar= f" \033[30m\033[102m {len(self.widget_bar.split(":"))} WGT \033[42m║{_}"

        self.prntlines({_uidh_top: "r", _uidh_mid: "r", _uidh_bot: "r", _uidh_abar: "r"})


    def ui_listen_uin(self):
        #os.system("pause")
        os.system("cls")
        self.ui_display_header()

        _direct = self.BIOS_CONTAINER
        _widget = ["network_status"]
        self.prnt(f"{self.ui_s_botRi}{self.ui_c_lightpurple}netlich{self.ui_c_lightblue}({self.ui_c_green}{_direct}{self.ui_c_lightblue}){self.ui_c_reset}─{self.ui_widget(_widget)}")
        _uin = str(input(f"{self.ui_s_topRi}{self.input_color}"))

        _boot.__revive__(f"{self.BIOS_CONTAINER}\\_ui.py")


UI = UserInterface()


while True:
    UI.ui_listen_uin()