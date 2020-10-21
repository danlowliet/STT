import speech_recognition as sr

r = sr.Recognizer() #initialize recognizer
print("Speak: ")

audio = r.listen(sr.Microphone()) #listen to the source
try:
    text = r.recognize_google(audio)
    print("you said: {}".format(text))
except:
    print("Sorry could not recognize your voice")
