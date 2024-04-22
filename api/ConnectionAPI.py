# Connection messegnes
def ConnectionAPI():
    print()

APIPhidgets = {
    "name": "Phidgets",
    "connectionLoading": False,
    "connected": False,
    "connectionState": "Disconnected",
    "conLost": False,
    "conLostMess": "Connection Lost - Retrying!",
    "backendNotFound": False,
    "backendNotFoundMess": "Backend Not Found - Retrying",
    "connectionInfo": {
        "dataReceived": False,
        "receivedData": {},
    },
}
APIFsuipc = {
    "name": "FSUIPC",
    "connectionLoading": False,
    "connected": False,
    "connectionState": "Disconnected",
    "conLost": False,
    "conLostMess": "Connection Lost - Retrying!",
    "websocketNotFound": False,
    "websocketNotFoundMess": "Websocket Not Found - Retrying",
    "connectionInfo": {
        "dataReceived": False,
        "receivedData": {},
    },
}
