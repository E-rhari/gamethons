import keyboard
from datetime import datetime, timedelta
from time import sleep
import json


timeInstances = []

print("Welcome to Eletrical Conductor level creator!")
print("The level creating process will start as soon as your first input ('z' or 'x' key) is entered.")
print("When you're done, simply input 'q' to exit the process and name your level")
while not keyboard.is_pressed("z") or keyboard.is_pressed("x"):
    continue    

print("Making started!")
initialTime = datetime.now()

while not keyboard.is_pressed("q"):
    if keyboard.is_pressed("z") or keyboard.is_pressed("x"):
        curentTime = datetime.now()
        delta = (curentTime - initialTime)
        miliDelta = round(delta.total_seconds() * 1000)
        timeInstances.append(miliDelta)
        print(miliDelta)
        sleep(0.1)
with open("beats.json", "w") as beats:
    # beatsString = json.loads(str(beats))
    json.dump(timeInstances, beats, indent=4, sort_keys=True)

print("\n\nAaaand, we are done!")
name = input("Now please name your level: ")
with open(f"{name}.txt", "a") as level:
    for instance in timeInstances:
        command = f'createBeat({instance}, {timeInstances.index(instance)})\n'
        level.write(command)
