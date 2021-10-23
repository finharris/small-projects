import tkinter as tk


class EnemyDamage:
    hp = 1500

    def attack(self):
        if self.hp > 0:
            self.hp -= 500
            print("OUCH! -500 damage!")

        if self.hp <= 0:
            self.healthcheck()
        else:
            pass

    def healthcheck(self):
        if self.hp == 0:
            print("You died :o")
            print(self.hp)
        elif self.hp > 0:
            print("You, somehow, are still alive with " + str(self.hp) + " hp left.")
        else:
            pass

    def fullheal(self):
        if self.hp < 1500:
            self.hp = 1500

            print("You have been FULL HEALED to 1500 hp!")
        else:
            pass


enemy1 = EnemyDamage()
enemy2 = EnemyDamage()

win = tk.Tk()
win.geometry("500x400")
win.title("Enemy Damager")

tk.Label(win, text="Enemy Damager").pack()
tk.Label(win, text="-------------").pack()
tk.Button(win, text="enemy1 attack", command=enemy1.attack).pack()
tk.Button(win, text="enemy1 check", command=enemy1.healthcheck).pack()
tk.Button(win, text="enemy1 heal", command=enemy1.fullheal).pack()

tk.Label(win, text="").pack()

tk.Button(win, text="enemy2 attack", command=enemy2.attack).pack()
tk.Button(win, text="enemy2 check", command=enemy2.healthcheck).pack()
tk.Button(win, text="enemy2 heal", command=enemy2.fullheal).pack()

win.mainloop()
