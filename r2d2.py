
import math
import random
from wavefile import WaveFile
import pygame
import RPi.GPIO as GPIO
import time
import os
import subprocess

global activeProc

Blue = 13
Red = 15
Green = 11
BlueUp = 7

note_freqs = [
    #  C       C#       D      D#      E       F       F#      G       G#      A       A#      B
     16.35,  17.32,  18.35,  19.45,   20.6,  21.83,  23.12,   24.5,  25.96,   27.5,  29.14,  30.87,
      32.7,  34.65,  36.71,  38.89,   41.2,  43.65,  46.25,   49.0,  51.91,   55.0,  58.27,  61.74,
     65.41,   69.3,  73.42,  77.78,  82.41,  87.31,   92.5,   98.0,  103.8,  110.0,  116.5,  123.5,
     130.8,  138.6,  146.8,  155.6,  164.8,  174.6,  185.0,  196.0,  207.7,  220.0,  233.1,  246.9,
     261.6,  277.2,  293.7,  311.1,  329.6,  349.2,  370.0,  392.0,  415.3,  440.0,  466.2,  493.9,
     523.3,  554.4,  587.3,  622.3,  659.3,  698.5,  740.0,  784.0,  830.6,  880.0,  932.3,  987.8,
    1047.0, 1109.0, 1175.0, 1245.0, 1319.0, 1397.0, 1480.0, 1568.0, 1661.0, 1760.0, 1865.0, 1976.0,
    2093.0, 2217.0, 2349.0, 2489.0, 2637.0, 2794.0, 2960.0, 3136.0, 3322.0, 3520.0, 3729.0, 3951.0,
    4186.0, 4435.0, 4699.0, 4978.0, 5274.0, 5588.0, 5920.0, 6272.0, 6645.0, 7040.0, 7459.0, 7902.0,
]




def generate_sin_wave(sample_rate, frequency, duration, amplitude):
    """
    Generate a sinusoidal wave based on `sample_rate`, `frequency`, `duration` and `amplitude`
    `frequency` in Hertz, `duration` in seconds, the values of `amplitude` must be in range [0..1]
    """
    data = []
    samples_num = int(duration * sample_rate)
    volume = amplitude * 32767
    for n in range(samples_num):
        value = math.sin(2 * math.pi * n * frequency / sample_rate)
        data.append(int(value * volume))
    return data


def generate_r2d2_message(filename, message):
    """
    Generate R2D2 message and save to `filename`
    """
    min_msg_len = 1
    max_msg_len = 20
    r2d2_message = []
    for _ in range(len(message)): #range(random.randint(min_msg_len, max_msg_len))
        r2d2_message.append(note_freqs[random.randint(0, len(note_freqs) - 1)])

    sample_rate = 8000  # 8000 Hz
    dot_dur = 0.080  # 80 ms
    volume = 0.80  # 80%

    wave = WaveFile(sample_rate)
    wave_duration = 0
    wave_data = []
    for freq in r2d2_message:
        wave_duration += dot_dur
        wave_data += generate_sin_wave(sample_rate, freq, dot_dur, volume)
    wave.add_data_subchunk(wave_duration, wave_data)
    wave.save(filename)

def shout():
    filename = "shout.wav"
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    time.sleep(0.5)
    while(pygame.mixer.music.get_busy()):
        turnOffLed("blueup")
        turnOffLed("red")
        turnLed("blue")
        time.sleep(0.1)
        turnOffLed("blue")
        turnLed("red")
        turnLed("blueup")
        time.sleep(0.1)
    turnOffAll()

def textToSpeech(text):
    scommand='espeak -a 200 -ves+M "' + text + '"'
    turnLed("red")
    os.system(scommand)
    turnOffAll()

def say(message):
    filename = "r2d2.wav"
    generate_r2d2_message(filename, message)
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while(pygame.mixer.music.get_busy()):
        turnOffLed("blueup")
        turnOffLed("red")
        turnLed("blue")
        time.sleep(0.7)
        turnOffLed("blue")
        turnLed("red")
        turnLed("blueup")
        time.sleep(0.7)
    turnOffAll()

def saySimple(message):
    filename = "r2d2.wav"
    generate_r2d2_message(filename, message)
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    
def turnOffLed(led):
    if led.lower() == "blue":
        GPIO.output(Blue, False)
        #print(led)
    elif led.lower() == "red":
        GPIO.output(Red, False)
        #print(led)
    elif led.lower() == "green":
        GPIO.output(Green, False)
        #print(led)
    elif led.lower() == "blueup":
        GPIO.output(BlueUp, False)
        #print(led)
    else:
        print('command not recognized')
        
def turnLed(led):
    if led.lower() == "blue":
        GPIO.output(Blue, True)
        #print(led)
    elif led.lower() == "red":
        GPIO.output(Red, True)
        #print(led)
    elif led.lower() == "green":
        GPIO.output(Green, True)
        #print(led)
    elif led.lower() == "blueup":
        GPIO.output(BlueUp, True)
        #print(led)
    else:
        print('command not recognized')
def setVolume(volume):
    os.system("amixer sset 'Master' {0}%".format(volume))

def playSound():
    name = "sound.wav"
    global activeProc
    activeProc = subprocess.Popen(["cvlc",":gain-value=1",name,"vlc://quit"])
    #os.system("cvlc --volume-step 256 {0} vlc://quit".format(name))
    print('returncode:', activeProc.returncode)
    turnOffAll()
    
def playSoundCry():
    name = "cry.mp3"
    global activeProc
    activeProc = subprocess.Popen(["cvlc",":gain-value=1",name,"vlc://quit"])
    #os.system("cvlc --volume-step 256 {0} vlc://quit".format(name))
    print('returncode:', activeProc.returncode)
    turnOffAll()

def playSound(filename):
    global activeProc
    activeProc = subprocess.Popen(["cvlc", ":gain-value=1", filename, "vlc://quit"])
    # os.system("cvlc --volume-step 256 {0} vlc://quit".format(name))
    print('returncode:', activeProc.returncode)
    turnOffAll()
    
def stopSound():
    activeProc.terminate()
    turnOffAll()
        
def turnOffAll():
    GPIO.output(7, False)
    GPIO.output(11, False)
    GPIO.output(13, False)
    GPIO.output(15, False)

def turnOnAll():
    GPIO.output(7, True)
    GPIO.output(11, True)
    GPIO.output(13, True)
    GPIO.output(15, True)

def main():
    filename = "r2d2.wav"
    generate_r2d2_message(filename, "Conoces la historia de Darth Plagueis eL Sabio?")
    pygame.mixer.init()
    #pygame.mixer.music.load("xd.mp3")
    #pygame.mixer.music.play()
    GPIO.setwarnings(False) 
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Blue, GPIO.OUT)
    GPIO.setup(Green, GPIO.OUT)
    GPIO.setup(Red, GPIO.OUT)
    GPIO.setup(BlueUp, GPIO.OUT)
    
    turnOffAll()
    
    # play R2D2 message
    #playsound(filename)
    #winsound.PlaySound(filename, winsound. SND_FILENAME)


if __name__ == '__main__':
    main()