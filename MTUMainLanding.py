from tkinter import *
mainApp = Tk()

from api.ConnectionAPI import APIPhidgets, APIFsuipc
from MainWindow import MainWindows

mainApp.title("B737MTU Controll")
# mainApps -----------------------------------------------------------------
#mainApp.iconbitmap('c:\Projekt - Lokalt\737MTUPython\media\mtu.png')
MainWindows(mainApp)
    #print("Continnue :)")
# Connect to Phidgets Server -----------------------------------------------

# --------------------------------------------------------------------------
mainApp.mainloop()