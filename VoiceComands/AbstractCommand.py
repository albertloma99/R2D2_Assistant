import abc


class AbstractCommand(object):
    invokeList = []

    def executeCmd(self, params):
        pass


class ConcreteCommand(AbstractCommand):

    invokeList = ["prueba de funcionamiento"]

    def executeCmd(self, params):
        print("Funcionando")
