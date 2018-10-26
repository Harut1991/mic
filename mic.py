import speech_recognition as sr
import wikipedia
import goog
r = sr.Recognizer()
goog.face("hellow")
def question():
  with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source,duration=1)  # here
    goog.face("any question?")
    print('speeck')
    audio1 = r.listen(source)
    recorder = r.recognize_google(audio1)
    print(recorder)
    ny = wikipedia.page(recorder)
    goog.face(ny.content.split('\n')[0])

    question()

question()
