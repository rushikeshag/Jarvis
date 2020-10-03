from src.python.jarvis import Jarvis
from src.python.util.search import getSearch, Google
import time
import sys

jarvis = Jarvis()
jarvis.speak("Calibrating system")
# time.sleep(4)
jarvis.speak("System is ready at its full potential")
while True:
    print("listening")
    text = jarvis.speechToText()
    if "friday" in text:
        jarvis.speak('at your service sir')
        while True:
            text = jarvis.speechToText()
            if 'friday are you there' in text :
                jarvis.speak('at your service sir')
            if 'open youtube' in text:
                jarvis.speak("opening youtube ,  sir")
                getSearch('youtube')
            if 'play music' in text:
                jarvis.speak("playing music")
                getSearch('play song')
            if 'down' in text:
                jarvis.speak("Bye sir")
                time.sleep(1)
                jarvis.speak('Shutting down sir')
                sys.exit()
            if 'google' in text:
                jarvis.speak("What do you want to search sir ?")
                text = jarvis.speechToText()
                google = Google()
                google.search(text)
            if 'sleep' in text:
                jarvis.speak('Ok sir')
                break
    elif "hello" in text:
        jarvis.speak('Sorry Sir,You are talking to me ?')
