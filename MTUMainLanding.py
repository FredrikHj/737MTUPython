import sys

from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget

class Window(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Button with a parent widget
        topBtn = QPushButton(parent=self)
        topBtn.setFixedSize(100, 60)
        # Button with a text and parent widget
        centerBtn = QPushButton(text="Center", parent=self)
        centerBtn.setFixedSize(100, 60)
        # Button with an icon, a text, and a parent widget
        bottomBtn = QPushButton(
            icon=QIcon("./icons/logo.svg"),
            text="Bottom",
            parent=self
        )
        bottomBtn.setFixedSize(100, 60)
        bottomBtn.setIconSize(QSize(40, 40))
        layout = QVBoxLayout()
        layout.addWidget(topBtn)
        layout.addWidget(centerBtn)
        layout.addWidget(bottomBtn)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
'''
import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtGui import QIcon

from api.ConnectionAPI import fsuipc, phidgets
from PhidgetsFunctions.ConnectToPhidgetServer import ConnectToPhidgetServer

def mainLanding():
    app = QApplication(sys.argv)
    win = QMainWindow()

    win.setGeometry(0, 0, 1200, 1000)
    win.setWindowTitle("B737MTU Controll")
    
    win.setWindowIcon(QIcon("./media/mtu.png"))
    
    def servicesBox(serviceName, width):
        mtuServiceName = "mtuServiceName {serviceName}"
        
        #Connection Services API
        serviceConAPI = serviceName

        mtuServiceName = QtWidgets.QLabel(win)
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