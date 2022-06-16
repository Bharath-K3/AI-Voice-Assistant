import pyautogui
import speech_recognition as sr

r = sr.Recognizer()

def commands(text):
    if text == "open admin":
        # Open The Admin Directory
        pyautogui.moveTo(37, 35, 1)
        pyautogui.click(button='left', clicks=2)

    elif text == "open start menu":
        # Open The start menu
        pyautogui.moveTo(18, 1057, 1)
        pyautogui.click(button='left', clicks=1)

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print ("Say Something")
    audio = r.listen(source)
          
    try:
        text = r.recognize_google(audio)
        print("you said: ", text)
        commands(text.lower())
      
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
      
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))