import r2d2

class cmdSpainMode(object):

    invokeList = ["arriba españa"]

    def executeCmd(self):
        r2d2.playSound("Sounds\Himno de España.mp3")