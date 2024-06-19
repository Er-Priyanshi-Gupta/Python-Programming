import os
folders = os.listdir("Python-Programming//Utility-Programs//cluster")
i = 1
for file in folders:
    if file.endswith(".png"):
        print(file)
        os.rename(f"Python-Programming//Utility-Programs//cluster/{file}",f"Python-Programming//Utility-Programs//cluster/{i}.png")
    i+=1