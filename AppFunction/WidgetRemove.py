import time
from AppFunction.RunConnectionStates import runConStates

def widgetRemove(rootApp, widgetsToRemove):
    widgetsToRemove.grid_remove()
    
    runConStates(rootApp)
