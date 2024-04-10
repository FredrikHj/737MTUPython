from Phidget22.Phidget import *
from Phidget22.Net import *
import time
    
def ConnectToPhidgetServer():
    Net.addServer("hub5000.local", "localhost", 5661, "", 0,)

    def setOnServerAddedHandler(self, server, kv):
        print("Server: " + str(server))
        print("Kv: " + str(kv))
        print("on")

    def onServerAdded(self, server, kv):
        print("Server: " + str(server))
        print("Kv: " + str(kv))
     
    net = Net()   

    
    #Register for event before calling open
    net.setOnServerAddedHandler(setOnServerAddedHandler)

    # Register for event before calling open
    net.setOnServerAddedHandler(onServerAdded)
    

