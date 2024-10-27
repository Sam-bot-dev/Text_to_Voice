import pyttsx3 # for more info check this website  (https://pypi.org/project/pyttsx3/ )
engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()