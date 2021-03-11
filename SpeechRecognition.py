import requests
import speech_recognition as sr

remoteIP = 'http://192.168.2.116:6969'

r = sr.Recognizer()
while True:
    try:
        #print(sr.Microphone.list_microphone_names())
        with sr.Microphone(device_index= 4) as source2:
            print('Listening...')
            #r.adjust_for_ambient_noise(source2)

            audio = r.listen(source2)
            r.pause_threshold = 1
            MyText = r.recognize_google(audio, language="es-ES")
            MyText = MyText.lower()
            print(MyText)
            payload = {'command':str(MyText)}
            requests.get(remoteIP, params=payload)




    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occured")