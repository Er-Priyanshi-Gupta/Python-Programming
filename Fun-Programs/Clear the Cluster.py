import os
folders = os.listdir("Python-Programming//Fun-Programs//cluster")
i = 1
for file in folders:
    if file.endswith(".png"):
        print(file)
        os.rename(f"Python-Programming//Fun-Programs//cluster/{file}",f"Python-Programming//Fun-Programs//cluster/{i}.png")
    i+=1