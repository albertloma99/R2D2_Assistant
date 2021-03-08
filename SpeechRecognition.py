import speech_recognition as sr
import pyttsx3
from gtts import gTTS


r = sr.Recognizer()

while(1):

    try:
        print(sr.Microphone.list_microphone_names())
        with sr.Microphone(device_index= 2) as source2:

            r.adjust_for_ambient_noise(source2, duration=1.5)

            audio = r.listen(source2)
            MyText = r.recognize_google(audio, language="es-ES")
            MyText = MyText.lower()

            print("Dijiste: "+ MyText)


    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occured")
