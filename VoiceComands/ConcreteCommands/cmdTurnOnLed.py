import r2d2

class cmdTurnOnLed(object):
    ledDict = {
                  "azul":"blue",
                  "rojo":"red",
                  "verde":"green",
                  "superior":"blueup",
    }
    invokeList = ["enciende led", "enciende luz"]

    def __init__(self):
        pass

    def executeCmd(self, *args):
        print('TEXTO DE VOZ: '+ args[0])
        print(str(self.getColorFromText(str(args[0]))))
        r2d2.turnLed(str(self.getColorFromText(str(args[0]))))
        r2d2.saySimple("okey")

    def getColorFromText(self, text):
        for color in self.ledDict.keys():
            print(color)
            if(color in text):
                return self.ledDict[color]
                break

