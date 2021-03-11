from flask import Flask, escape, request
from VoiceComands.CommandList import CommandList
import r2d2

app = Flask(__name__)

@app.route('/')
def hello():
    command = request.args.get('command')
    dispatchCommnad(command)
    return 'Requested Command: '+command

def dispatchCommnad(text):

    for cmd in CommandList:
        for textInvoke in cmd.invokeList:
            if(textInvoke in text):
                print("EXECUTING COMMAND")
                cmd.executeCmd(text)
r2d2.main()
Flask.run(app,port=6969, host='0.0.0.0')