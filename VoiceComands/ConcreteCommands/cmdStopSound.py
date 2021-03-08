import r2d2

class cmdStopSound(object):

    invokeList = ["para la musica", "para el sonido"]

    def __init__(self):
        pass

    def executeCmd(self):
        r2d2.stopSound()