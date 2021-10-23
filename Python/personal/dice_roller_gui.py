import tkinter as tk
import random

win = tk.Tk()  # makes window
win.title("Dice Roller")  # adds "Dice Roller" title
win.resizable(True, True)  # lets you resize window
win.geometry("500x400")  # sets default window size
# create a variable of type StringVar
n = tk.StringVar()
# have the function set that variable
def roll_dice():
        global n
        n.set(random.randint(1, 6))
# call it once to set the initial value of the variable
roll_dice()
tk.Label(win, text="Dice Roller").pack()
tk.Button(win, text="Click To Roll", command=roll_dice).pack()
# display the variable
tk.Label(win, textvariable=n).pack()

win.mainloop()
