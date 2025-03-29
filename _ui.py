import _bios as _b
import os
nl = _b.BIOS

class UserInterface(nl):
    def __init__(self):
        super().__init__()
        os.system(f"title master% netlich [{self.BIOS_CONTAINER}]")

        self.input_color = None
        self.haddr_color = None
        self.access      = self.request_useracslev("rw")

        self.ui_c_lightpurple = self.BIOS_BSHCC("lpurple")
        self.ui_c_purple      = self.BIOS_BSHCC("purple")
        self.ui_c_green       = self.BIOS_BSHCC("green")
        self.ui_c_blue        = self.BIOS_BSHCC("blue")
        self.ui_c_red         = self.BIOS_BSHCC("red")
        self.ui_c_reset       = self.BIOS_BSHCC("r")
        self.ui_c_bold        = self.BIOS_BSHCC("bold")#?  possibly deprecated w10
        self.ui_c_italic      = self.BIOS_BSHCC("italic")#?

        self.set_input_color("r")
        self.update_addr_color()

        self.prntlines({f" ┳┓ ┏┓ ┏┳┓ \033[95m┓ ┳┏┓┓┏ \033[0m[NLv{self.request_productversion()}]\033[35m\033[4m┐│\033[94m\033[35m┌─{self.haddr_color}{self.SYS_USER_UIP}\033[0m]  Use \"net.help\"": "r",
                        f" ┃┃ ┣   ┃  \033[95m┃ ┃┃ ┣┫ \033[35m│\033[95mNETL ☼\033[35m│\033[94mBI\033[35m│\033[94mUI\033[35m│\033[94mCM\033[35m│\033[94mMISC.\033[35m│\033[36m@\033[90m{self.SYS_USER_HNAME}": "r",
                        f" ┛┗ ┗┛  ┻  \033[95m┗┛┻┗┛┛┗ \033[35m│{self.SYS_USER_PLATF} \033[94mProduct Version\033[35m└─\033[95mCurrent Host": "r"})

    def set_input_color(self, _color: str = "r"):
        self.input_color = self.BIOS_BSHCC(_color)

    def update_addr_color(self):
        self.haddr_color = self.BIOS_SECUREUI_SHOWHOSTADDR_CLR \
                           [self.BIOS_SECUREUI_SHOWHOSTADDR]

    def clisten(self):
        self.prnt(f"┌{self.ui_c_lightpurple}netlich{self.ui_c_reset}─{self.ui_c_green}/~ {self.ui_c_purple}≤ {self.access[0]}")
        _userinput = str(input(f"└{self.input_color}"))

UI = UserInterface()

while True:
    UI.clisten()