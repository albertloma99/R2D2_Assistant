from flask import Flask, escape, request

app = Flask(__name__)


@app.route('/')
def hello():
    command = request.args.get('command')
    return 'Requested Command: '+command

Flask.run(app,port=6969, host='0.0.0.0')