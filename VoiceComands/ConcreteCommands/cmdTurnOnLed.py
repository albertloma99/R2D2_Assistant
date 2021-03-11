import r2d2

class cmdTurnOnLed(object):

    invokeList = ["enciende led", "enciende luz"]

    def __init__(self):
        pass

    def executeCmd(self, *args):
        r2d2.turnLed("blue")