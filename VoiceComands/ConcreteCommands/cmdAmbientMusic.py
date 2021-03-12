import r2d2

class cmdAmbientMusic(object):

    invokeList = ["pon música","pon algo de música"]

    def __init__(self):
        pass

    def executeCmd(self, *args):
        r2d2.playSound("Sounds/Cantina band.wav")