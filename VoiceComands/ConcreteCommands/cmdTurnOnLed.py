import r2d2

class cmdTurnOnLed(object):
    ledDict = {
                  "azul":"blue",
                  "red":"rojo",
                  "verde":"green",
                  "superior":"blueup",
    }
    invokeList = ["enciende led", "enciende luz"]

    def __init__(self):
        pass

    def executeCmd(self, *args):
        print('TEXTO DE VOZ: '+ args[0])
        r2d2.turnLed(self.getColorFromText(args[0]))

    def getColorFromText(self, text):
        for color in self.ledDict.keys():
            if(color in text):
                return self.ledDict[color]
                break

