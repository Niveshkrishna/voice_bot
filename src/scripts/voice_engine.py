#!/usr/bin/env python
import speech_recognition as sr
from espeak import espeak
import sound_play as sd

def get_text_from_speech(audio, recognizer):
    # obtain audio from the microphone
    try:
        data_input = recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        data_input = -1
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return data_input

# text to speech synthesizer function
def get_speech_from_text(text):
    espeak.synth(text)
    
    
