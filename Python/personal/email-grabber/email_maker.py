from re import S
from pynput.keyboard import Key, Controller
import pyperclip
import time


'''
copy name to clipboard/type into box
press enter
press left
press enter
copy to clipboar and save
press backspace
'''

keyboard = Controller()

emails = []

time.sleep(5)

with open('temp.txt', 'r') as file:
  for line in file:
    pyperclip.copy(line)

    keyboard.press(Key.ctrl.value)
    keyboard.press('v')
    keyboard.release(Key.ctrl.value)
    keyboard.release('v')

    time.sleep(0.6)
    
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    
    time.sleep(0.1)
    
    keyboard.press(Key.left)
    keyboard.release(Key.left)

    time.sleep(0.1)
    
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    time.sleep(0.1)
    
    keyboard.press(Key.ctrl.value)
    keyboard.press('c')
    keyboard.release(Key.ctrl.value)
    keyboard.release('c')

    time.sleep(0.1)
    
    email = pyperclip.paste()
    
    with open('emails.txt', 'a') as f:
      f.write(f'{email}\n')
        
    keyboard.press(Key.backspace)
    keyboard.release(Key.backspace)

    
    
