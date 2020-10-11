import random, time, sys, os
import tkinter as tk
from tkinter import *

people = ["Barborak Adam", "Bedocs David", "Budiacova Vladimira", "Ferencik Tadeas", "Hajdin Dominik", "Hodalova Mirka",
          "Chamrova Laura",
          "Janicek Andrej", "Kosecka Slavka", "Kosikova Tereza", "Kosinarova Kristina", "Kostal Lubos",
          "Kruzliakova Barbora", "Kubicova Veronika", "Pappova Tiffany",
          "Polacek Viktor", "Porubec Jakub", "Rakus Martin", "Sepsi Richard", "Schuster Sofia", "Svitan Daniel",
          "Stofkova Simona", "Tomanik Oliver", "Tomsikova Hanka",
          "Tothova Elena", "Tulek Jakub", "Vachula Tomas", "Vargovcik Matej"]

people_to_rig = ["Tulek Jakub", "Sepsi Richard", "Svitan Daniel", "Porubec Jakub"]


class RNG:
    def __init__(self, people):
        self.people = people
        self.names = {}
        self.change_values()

    def change_values(self):
        for person in self.people:
            self.names[person] = random.randint(1, 10000)

    def search_by_val(self, val):
        for k in self.names:
            if val == self.names[k]:
                return k

    def get_random_person(self):
        wwchd = 0
        for n in self.names:
            if self.names.get(n) > wwchd:
                wwchd = self.names.get(n)
        ret = self.search_by_val(wwchd)
        self.change_values()
        return ret

    def rig(self, person, multiplier):
        for name in self.names:
            if name == person:
                self.names[name] = self.names.get(name) * multiplier
                return


"""

class People:
    def __init__(self, filename):
        self.filename = filename
        if not os.path.exists(self.filename):
            raise FileNotFoundError()

"""

win = Tk()


class Helper:
    def __init__(self, win, people, people_to_rig):
        self.rng = RNG(people)
        self.label1 = Label(win, text="Vyberame")
        self.label1.place(x=200, y=20)
        for name in people_to_rig:
            self.rng.rig(name, 0.75)

    def create_label_and_display_winner(self):
        winner = self.rng.get_random_person()
        print(winner)
        self.label1.config(text=winner)

    def Exit(self):
        win.quit()


Lf1 = LabelFrame(win, text="", height=180, width=169).place(x=10, y=10)
bottomlabel = Label(Lf1, text=" ")

Lf2 = LabelFrame(win, text="", height=180, width=300).place(x=190, y=10)
# bottomlabel = Label(Lf2, text = "test")
helper = Helper(Lf1, people, people_to_rig)

border = 0
fg = "lightgrey"

b1 = Button(win, command=helper.create_label_and_display_winner, text="Žrebovať", border=border,
            activebackground="gray", activeforeground="white", bg=fg, height=5, width=10).place(x=15, y=15)
b2 = Button(win, text="Pridať", border=border, activebackground="gray", activeforeground="white", bg=fg, height=5,
            width=10).place(x=96, y=15)
b3 = Button(win, text="Odobrať", border=border, activebackground="gray", activeforeground="white", bg=fg, height=5,
            width=10).place(x=15, y=101)
b4 = Button(win, command=helper.Exit, text="Koniec", border=border, activebackground="gray", activeforeground="white",
            bg=fg, height=5, width=10).place(x=96, y=101)

win.title('Rng')
win.geometry("500x200")
win.mainloop()