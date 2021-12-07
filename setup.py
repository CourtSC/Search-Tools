#! python3
#! setup.py - Moves Batch Files to C:\Windows so the modifying the PATH variable is no longer necessary.

from pathlib import Path
import os, shutil, pyuac

if not pyuac.isUserAdmin():
    pyuac.runAsAdmin()

p = Path('C:/Search-Tools/Batch Files')
w = Path('C:/Windows')

for i in os.listdir(p):
    shutil.copy(p / i, w)