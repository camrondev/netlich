# System POST Logs
def lg(_str: str = None) -> None:
    if _str == None:
        return
    
    if _str[0] == "%":
        print(f"LD BIOS/UserInterface/{_str}")
        return
    
    print(f"LD {_str}")