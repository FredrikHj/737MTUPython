from tkinter import *
window = Tk()
#window.geometry("100", "100")
#geometry(100, 100)
#window.WindowTitle("B737MTU Controll")


myLabel = Label(window, text="trsdvg")
myLabel.pack()

window.mainloop()
'''
import sys

from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget

from api.ConnectionAPI import fsuipc, phidgets
from PhidgetsFunctions.ConnectToPhidgetServer import ConnectToPhidgetServer

class Window(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        def servicesBox(serviceName, width):
            mtuServiceName = "mtuServiceName {serviceName}"
            
            #Connection Services API
            serviceConAPI = serviceName

            mtuServiceName = QWidget(window)
            mtuServiceName.setText(serviceName.upper() + " - ")
            
            mtuServiceName.setStyleSheet(
                "min-width: 260px;"
                "min-height: 50px;"
                "font-weight: bold;"
                "font-size: 40px;"
            )
            mtuServiceName.move(width, 30)
            print("efw", serviceConAPI)

    # Call the function to show the labels of the included services
        servicesBox("phidgets", 100)
        servicesBox("fsuipc", 700)

        
        centerBtn = QPushButton(text="Center", parent=self)
        centerBtn.setFixedSize(100, 60)

        
        layout = QVBoxLayout()
       
        layout.addWidget(centerBtn)
    
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.setWindowIcon(QIcon("./media/mtu.png"))
    window.show()
    sys.exit(app.exec())



def mainLanding():

    
   
    def initMtuButton():
        class Window(QWidget):
            def __init__(self, parent=None):
                super().__init__(parent)
                initMtuButton = QPushButton(text="Initilize MTU", parent=self)
                initMtuButton.setFixedSize(60, 350)
                
                initMtuButtonLayout = QVBoxLayout()
                initMtuButtonLayout.addWidget(initMtuButton)

                ConnectToPhidgetServer()
                self.setLayout(initMtuButtonLayout)
    initMtuButton()
    #win.setToolTip("Mtu")
    
    win.show()
    sys.exit(app.exec())


mainLanding()
'''