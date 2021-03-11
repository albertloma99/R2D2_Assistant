import r2d2

class cmdStopSound(object):

    invokeList = ["para la música", "para el sonido","para"]

    def __init__(self):
        pass

    def executeCmd(self, *args):
        r2d2.stopSound()