import r2d2

class cmdTurnOffAllLeds(object):

    invokeList = ["apaga leds", "apaga todos los leds","apaga luces", "apaga todas las luces"]

    def __init__(self):
        pass

    def executeCmd(self, *args):
        r2d2.turnOffAll()
