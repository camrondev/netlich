import _bios as _b
import os
nl = _b.BIOS
class UserInterface(nl):



    def __init__(self):
        super().__init__(); print("INIT NL/BIOS/UserInterface")
        os.system(f"title master% netlich [{self.BIOS_CONTAINER}]")

        self.input_color = self.request_userinputcolor("r"); print("LD BIOS/UserInterface/input_color.")
        self.haddr_color = self.sui_request_recvhaddrcolor(); print("LD BIOS/UserInterface/haddr_color.")
        self.access      = self.request_useracslev("niggaswitnomoney-real"); print("LD BIOS/UserInterface/access.")
        

        if self.access == None:
            self.prntlines({f"{self.request_file_execname()} encountered a fatal error:": "red",
                            "This application lacks the permissions to operate. PERMISSION_ERROR": "r"})
            os.system("pause")
            _b.sys.exit()
        else:
            self.access_n_1  = str(); print("LD BIOS/UserInterface/access_n_1.")
            for _item in self.access[1]:
                self.access_n_1 = f"{self.access_n_1}{_item}"


        self.ui_c_lightpurple = self.BIOS_BSHCC("lpurple"); print("LD BIOS/UserInterface/ui_c_lightpurple.")
        self.ui_c_purple      = self.BIOS_BSHCC("purple");  print("LD BIOS/UserInterface/ui_c_purple.")
        self.ui_c_green       = self.BIOS_BSHCC("green");   print("LD BIOS/UserInterface/ui_c_green.")
        self.ui_c_lightblue   = self.BIOS_BSHCC("lblue");   print("LD BIOS/UserInterface/ui_c_lightblue.")
        self.ui_c_blue        = self.BIOS_BSHCC("blue");    print("LD BIOS/UserInterface/ui_c_blue.")
        self.ui_c_red         = self.BIOS_BSHCC("red");     print("LD BIOS/UserInterface/ui_c_red.")
        self.ui_c_reset       = self.BIOS_BSHCC("r");       print("LD BIOS/UserInterface/ui_c_reset.")
        self.ui_c_bold        = self.BIOS_BSHCC("bold");    print("LD BIOS/UserInterface/ui_c_bold.")#?  possibly deprecated w10
        self.ui_c_italic      = self.BIOS_BSHCC("italic");  print("LD BIOS/UserInterface/ui_c_italic.")#?


        self.prnt("NL BIOS/report: \033[32mApplication successfully loaded.")  # POST/LOG Endpoint, User-accessible UI after this point.


    def ui_display_header(self):
        self.prntlines({f" ┳┓ ┏┓ ┏┳┓ \033[95m┓ ┳┏┓┓┏ \033[0m[NLv{self.request_productversion()}]\033[35m\033[4m┐│\033[94m\033[35m┌─{self.haddr_color}{self.SYS_USER_UIP}\033[0m]  Use \"net.help\"": "r",
                        f" ┃┃ ┣   ┃  \033[95m┃ ┃┃ ┣┫ \033[35m│\033[95mNETL ☼\033[35m│\033[94mBI\033[35m│\033[94mUI\033[35m│\033[94mCM\033[35m│\033[94mMISC.\033[35m│\033[36m@\033[90m{self.SYS_USER_HNAME}": "r",
                        f" ┛┗ ┗┛  ┻  \033[95m┗┛┻┗┛┛┗ \033[35m│{self.SYS_USER_PLATF} \033[94mProduct Version\033[35m└─\033[95mCurrent Host": "r"})



    def clisten(self):
        os.system("pause")
        os.system("cls")
        self.ui_display_header()
        self.prnt(f"\033[90m║SYSTEM  DIR PRM ║{self.ui_c_red}X{self.ui_c_lightblue}{self.access_n_1}\033[90m│{self.ui_c_green}{self.sui_request_recvpermissions_allow(self.access_n_1)}")
        self.prnt(f"┌{self.ui_c_lightpurple}netlich{self.ui_c_reset}─{self.ui_c_lightblue}({self.ui_c_green}~{self.ui_c_lightblue}){self.ui_c_reset}─║{self.access[0]}║")
        _userinput = str(input(f"└{self.input_color}"))


UI = UserInterface()
UI.clisten()