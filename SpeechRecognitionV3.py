import speech_recognition as sr
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

remoteIP = 'http://192.168.2.116:6969'
activationWord = 'r2'

while True:
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone(device_index=4) as source:
        print("Please wait. Calibrating microphone...")
        # listen for 1 second and create the ambient noise energy level
        r.adjust_for_ambient_noise(source, duration=1)
        print("Say something!")
        audio = r.listen(source, phrase_time_limit=5)

    # recognize speech using Sphinx/Google
    try:
        response = r.recognize_google(audio, language='es-ES')
        response = str(response).lower()
        if(activationWord.lower() in response):#Filter by activation word
            response = response.replace(activationWord, '').lstrip()
            print(response.upper())
            payload = {'command': str(response)}
            requests.get(remoteIP, params=payload)
        else:
            print(response)


    except sr.UnknownValueError:
        pass
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))