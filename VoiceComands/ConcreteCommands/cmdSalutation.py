import r2d2

class cmdSalutation(object):

    invokeList = ["hola", "hola que tal","buenas","buenos días","buenas tardes"]

    def __init__(self):
        pass

    def executeCmd(self, *args):
        r2d2.playSound("Sounds/Happy Confirmation.wav")