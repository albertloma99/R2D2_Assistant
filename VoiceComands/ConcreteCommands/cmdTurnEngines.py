import r2d2

class cmdTurnEngines(object):

    invokeList = ["enciende motores", "salta a la velocidad de la luz","salta la velocidad de la luz","hipervelocidad"]

    def __init__(self):
        pass

    def executeCmd(self, *args):
        r2d2.say("Alla vamos")
        r2d2.playSound("Sounds/Jump to lightspeed.wav")