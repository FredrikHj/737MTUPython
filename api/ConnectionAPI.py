def ConnectionAPI():
    print()
phidgets = {
    "name": "Phidgets",
    "connectionLoading": False,
    "connected": False,
    "connectionMess": "Connected",
    "conLost": False,
    "conLostMess": "Connection Lost - Retrying!",
    "backendNotFound": False,
    "backendNotFoundMess": "Backend Not Found - Retrying",
    "connectionInfo": {
        "dataReceived": False,
        "receivedData": {},
    },
}
fsuipc = {
    "name": "FSUIPC",
    "connectionLoading": False,
    "connected": False,
    "connectionMess": "Connected",
    "conLost": False,
    "conLostMess": "Connection Lost - Retrying!",
    "websocketNotFound": False,
    "websocketNotFoundMess": "Websocket Not Found - Retrying",
    "connectionInfo": {
        "dataReceived": False,
        "receivedData": {},
    },
}
