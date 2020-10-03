import speech_recognition as speechRecognition
import pyttsx3


class Jarvis:

    def speechToText(self):
        recognizer = speechRecognition.Recognizer()
        with speechRecognition.Microphone() as source:
            print("Say Something...!")
            try:
                audio = recognizer.listen(source)
                recognizer.adjust_for_ambient_noise(source,duration=1)
                speech = recognizer.recognize_google(audio)
                if speech is None:
                    speech=""
            except:
                print("I am not getting what you are saying")
                speech=" "
        return speech.lower()

    def speak(self, text):
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.setProperty('rate', 175)  # getting details of current voice
        engine.setProperty('volume', 1.0)  # setting up volume level  between 0 and 1
        engine.say(text)
        engine.runAndWait()
