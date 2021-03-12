import r2d2


class cmdHelloThere(object):

    invokeList = ["hello there","hellouda"]

    def __init__(self):
        pass

    def executeCmd(self, *args):
        r2d2.playSound("Sounds/GeneralKenobi.wav")