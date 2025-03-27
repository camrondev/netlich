import _bios as _b
import os
nl = _b.BIOS

class UserInterface(nl):
    def __init__(self):
        super().__init__()
        os.system(f"title master% netlich [{self.BIOS_CONTAINER}]")

        self.input_color = self.BIOS_BSHCC("r")

        self.prntlines({"┳┓ ┏┓ ┏┳┓ \033[95m┓ ┳┏┓┓┏": "r",
                        f"┃┃ ┣   ┃  \033[95m┃ ┃┃ ┣┫ \033[0m{self.SYS_USER_PLATF} @ NetLich v^{self.BIOS_VERSION}": "r",
                        "┛┗ ┗┛  ┻  \033[95m┗┛┻┗┛┛┗": "r"})

    def set_input_color(self, _color: str = "r"):
        self.input_color = self.BIOS_BSHCC(_color)

    def clisten(self):
        self.prnt(f"┌{self.BIOS_BSHCC("lpurple")}netlich{self.BIOS_BSHCC("r")}─")
        _userinput = str(input(f"└{self.input_color}"))

UI = UserInterface()

while True:
    UI.clisten()