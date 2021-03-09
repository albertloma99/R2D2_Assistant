import r2d2

class cmdSpainMode(object):

    invokeList = ["arriba españa", "españa", "franco"]

    def __init__(self):
        pass

    def executeCmd(self):
        print("playing el himnito de españita")
        r2d2.playSound('Sounds/HimnodeEspana.wav')