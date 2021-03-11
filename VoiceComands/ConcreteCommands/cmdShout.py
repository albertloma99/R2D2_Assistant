import r2d2

class cmdShout(object):

    invokeList = ["susto", "grita"]

    def __init__(self):
        pass

    def executeCmd(self, *args):
        r2d2.shout()