import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow
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

    ConnectToPhidgetServer()
    #win.setToolTip("Mtu")
    
    win.show()
    sys.exit(app.exec())


mainLanding()