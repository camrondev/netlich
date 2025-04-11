# System POST Logs
_mount = []# is only emptied when the mount is flashed to scr

def mountvar(_var: str = None) -> None:
    if _var == None:
        return
    
    _mount.append(_var)


def lg(_str: str = None) -> None:
    if _str == None:
        return
    
    if _str[0] == "%":
        print(f"LD BIOS/UserInterface/{_str}")
        return
    
    print(f"LD {_str}")


def flash() -> None:
    try:
        for _var in _mount:
            lg(_var)
        _mount.clear()
    except Exception:
        return
    
    _mount.clear()