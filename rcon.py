from mctools import RCONClient

def connectToServer(ip,passwd,port=25575):
    client = RCONClient(ip,port)
    client.login(passwd)
    return client

def checkConnection(client):
    auth = client.is_authenticated()
    return auth