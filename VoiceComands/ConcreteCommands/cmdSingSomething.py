import r2d2

class cmdSingSomething(object):

    invokeList = ["canta algo","canta"]

    def __init__(self):
        pass

    def executeCmd(self, *args):
        r2d2.playSound("Sounds/Sing Song.wav")