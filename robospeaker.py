import win32com.client as wincom

print("Welcome to Robo Speaker 1.1. Created by Sahil Prakash ")
while True:
    x = input("Enter what to want to speak: ")
    if x == "q":
        speak = wincom.Dispatch("SAPI.SpVoice")
        text = "Bye bye friends see you next time"
        speak.Speak(text)
        break
    speak = wincom.Dispatch("SAPI.SpVoice")
    text = f"{x}"
    speak.Speak(text)
