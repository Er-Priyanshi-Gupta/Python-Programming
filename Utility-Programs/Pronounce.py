import win32com.client 
speaker = win32com.client.Dispatch("SAPI.SpVoice") 
print("Enter list of people whom you want to give shoutout") 
s = input().split(",")
print(s)
for name in s:
    speaker.Speak(f"Shoutout to{name}")
    