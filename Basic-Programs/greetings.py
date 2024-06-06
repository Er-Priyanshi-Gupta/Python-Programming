import time
print("Enter Name")
name = input()
currentTime = time.strftime("%H:%M:%S")
hour = int(time.strftime("%H"))
print(currentTime)
if (hour >= 4 and hour <= 11):
  print("Good Moring ", name)
elif (hour >= 12 and hour <= 16):
  print("Good Afternoon ", name)
elif (hour >= 17 and hour <= 20):
  print("Good Evening ", name)
else:
  print("Good Night ", name)
