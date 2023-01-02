from PyQt5 import uic

with open ("Main.py" , "w" , encoding="utf-8") as fout :
    uic.compileUi("Main.ui" , fout)