from tkinter import *
from api.ConnectionAPI import APIPhidgets, APIFsuipc
from AppFunction.WidgetRemove import widgetRemove
from PhidgetsFunctions.InitConnectionPhidgets import initConnectionPhidgets
def MainWindows(MainWindow):

    def mainWindowLayout(MainAppWindow):
        #MainWindow.iconbitmap('c:\Projekt - Lokalt\737MTUPython\media\mtu.png')
    
        #Name of servies
        mtuServiceNamePhidgets = "phidgets"
        mtuServiceNameFsuipc = "fsuipc"

        #Creates the main Windows with the included layout
        emptyRow0Col0 = Label(MainAppWindow, text="           ").grid(row=0, column=0)

        emptyRow1Col1 = Label(MainAppWindow, text="           ").grid(row=1, column=0)
        mtuServiceNamePhidgets = Label(MainAppWindow, text=mtuServiceNamePhidgets.upper() + " - ").grid(row=1, column=1)
        conStateServicePhidgets = Label(MainAppWindow, text=APIPhidgets["connectionState"])
        conStateServicePhidgets.grid(row=1, column=2)

        emptyRow1Col3 = Label(MainAppWindow, text="           ").grid(row=1, column=3)
        mtuServiceNameFsuipc = Label(MainAppWindow, text=mtuServiceNameFsuipc.upper() + " - ").grid(row=1, column=4)
        conStateServiceFsuipc = Label(MainAppWindow, text=APIFsuipc["connectionState"])
        conStateServiceFsuipc.grid(row=1, column=5)
        emptyRow1Col6 = Label(MainAppWindow, text="           ").grid(row=1, column=6)

        emptyRow2Col0 = Label(MainAppWindow, text="   ").grid(row=2, column=0)
        emptyRow2Col1 = Label(MainAppWindow, text="   ").grid(row=2, column=1)
        emptyRow2Col2 = Label(MainAppWindow, text="   ").grid(row=2, column=2)

        #In the same time 
        def runInitMTU():
            APIPhidgets["connectionState"] = "Connected"
            APIFsuipc["connectionState"] = "Connected"
            widgetRemove(MainAppWindow, conStateServicePhidgets)
            widgetRemove(MainAppWindow, conStateServiceFsuipc)
            #removeInitBtn()
            initConnectionPhidgets()
        
        #Create the initMTU Button
        runInitMTUBtn = Button(MainAppWindow, text="INITILIZE MTU", command=runInitMTU)
        runInitMTUBtn.grid(row=1, column=3)

        #Remove the created Button
        def removeInitBtn():
            widgetRemove(MainAppWindow, runInitMTUBtn)
    
    if(APIPhidgets["connectionState"] == "Connected" and APIFsuipc["connectionState"] == "Connected"):
        return print("All Services Connected!")
    else:
        mainWindowLayout(MainWindow)