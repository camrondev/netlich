# Allows for Local In-App Restarts
import os, sys


def __revive__(_target: str = None):
    if _target == None:
        return
    
    if not sys.executable:
        return
    
    os.system(f'"{_target}"')