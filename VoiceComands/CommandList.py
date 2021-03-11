from VoiceComands.ConcreteCommands.cmdSpainMode import cmdSpainMode
from VoiceComands.ConcreteCommands.cmdStopSound import cmdStopSound
from VoiceComands.ConcreteCommands.cmdTurnOnLed import cmdTurnOnLed
from VoiceComands.ConcreteCommands.cmdTurnOffAllLeds import cmdTurnOffAllLeds
from VoiceComands.ConcreteCommands.cmdShout import cmdShout

CommandList = [
    cmdSpainMode(),
    cmdStopSound(),
    cmdTurnOnLed(),
    cmdTurnOffAllLeds(),
    cmdShout(),

]