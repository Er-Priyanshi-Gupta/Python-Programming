import win32com.client 
speaker = win32com.client.Dispatch("SAPI.SpVoice") 
while 1: 
    print("Enter list of people whom you want to give shoutout") 
    s = input().split(",")
    print(s)
    speaker.Speak(s)
    