# Robo Code in Python
# import the required module from text to speech conversion
import win32com.client

# Calling the Dispatch method of the module which
# interact with Microsoft Speech SDK to speak
# the given input from the keyboard

speaker = win32com.client.Dispatch("SAPI.SpVoice")
while(True):
    s = input("enter what you want me to speak: ")
    if(s=="q"):
        speaker.Speak(f"Good Bye it was nice talking to you")
        break
    speaker.Speak(f"{s}")

# To stop the program Enter q
