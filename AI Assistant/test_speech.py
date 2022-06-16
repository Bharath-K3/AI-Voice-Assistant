import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print ("Say Something")
    audio = r.listen(source)
          
    try:
        text = r.recognize_google(audio)
        print("you said: ", text)
      
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
      
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))