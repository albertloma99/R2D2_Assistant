import r2d2
import random

class cmdInsult(object):

    invokeList = ["tonto", "bobo","gilipollas","subnormal"]

    def __init__(self):
        pass

    def executeCmd(self, *args):
        randomSound = random.choice(["Sounds/Upset TwoTone.wav","Sounds/Abrupt Burst.wav"])
        r2d2.playSound(randomSound)