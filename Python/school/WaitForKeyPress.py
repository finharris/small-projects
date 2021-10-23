# pip install keyboard
import keyboard

while True:
    if keyboard.read_key():
        print("You pressed a key")
        break