import time
from tkinter import *
import random


class Counter():

    def __init__(self, windows) -> None:
        self.windows = windows
        windows.geometry("930x490")
        windows.config(background="Black")
        windows.title("Counter")
        self.counter = 0
        self.incrementing_counter = 1
        
       # icon = PhotoImage(file="D:\\Vids and Pics\\Pictures\\GUI Icons\\counter.png")
       # windows.iconphoto(windows, icon)

        self.counting = Label(text=f"{self.counter:02}", font=("Ariel", 120), foreground="White", background="Black", activebackground="Black", activeforeground="White")
        self.counting.place(x=390, y=35)

        Count_Button = Button(text="Count", font=("Courier", 45), foreground="#3cff00", background="Black", activebackground="Black", activeforeground="#3cff00", bd=5, relief=RAISED, command=self.counting_funtion)
        Count_Button.place(x=40, y=350)

        Reset_Button = Button(text="Reset", font=("Courier", 45), foreground="#0011ff", background="Black", activebackground="Black", activeforeground="#0011ff", bd=5, relief=RAISED, command=self.Reset_function)
        Reset_Button.place(x=350,y=350)

        Color_Button = Button(text="Color", font=("Courier", 45), foreground="#05f5e5", background="Black", activebackground="Black", activeforeground="#05f5e5", bd=5, relief=RAISED, command=self.Color_function)
        Color_Button.place(x=650,y=350)


    def counting_funtion(self):
        self.counter += self.incrementing_counter
        self.counting.config(text=f"{self.counter:02}")

    def Color_function(self):
        colors = ["#05f5e5", "#0011ff", "#99ff00", "#ff1900", "#f3ff05", "#9aff03", "#1cff03", "#02f54f", "#02fa93", "#05ffe2", "#30f0d9", "#04c9b2", "#02d9fa", "#029bfa", "#004cff", "#0905fc", "#5f02f5", "#a703ff", "#dd00ff", "#ff00bb", "#f533c1", "#f50575", "#ff002f", "White", "Black"]
        random_colors = random.choice(colors)
        windows.config(background=f"{random_colors}")
        self.counting.config(background=f"{random_colors}")

        if random_colors == "#05f5e5" or random_colors == "#99ff00" or random_colors == "#f3ff05" or random_colors == "#9aff03" or random_colors == "#1cff03" or random_colors == "#02f54f" or random_colors == "#02fa93" or random_colors == "#05ffe2" or random_colors == "#30f0d9" or random_colors == "#f533c1" or random_colors == "White" or random_colors == "#02d9fa":
            self.counting.config(fg="Black")
        else:
            self.counting.config(fg="White")

    def Reset_function(self):
        self.counter = 0
        self.counting.config(text=f"{self.counter:02}")




if __name__ == '__main__':

    windows = Tk()
    counter = Counter(windows)
    windows.mainloop()
