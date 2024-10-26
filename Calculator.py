from tkinter import *
import random


class Calculator():
    
    def __init__(self, windows) -> None:
        self.windows = windows
        windows.title("Calculator")
        windows.geometry("480x640")
        windows.config(background="Black")
        numbers = 0
        

        value = Label(text=f"{numbers:02}", font=("Ariel", 60,), background="black", foreground="white", padx=5, pady=5)
        value.place(x=0, y=100)

        Button_one = Button(text="1", font=("ariel", 40), fg="#37ff00", background="Black", bd=5, relief=RAISED, padx=20, activebackground="black", activeforeground="#37ff00")
        Button_one.place(x=0, y=200)

        Button_two = Button(text="2", font=("ariel", 40), fg="#37ff00", background="Black", bd=5, relief=RAISED, padx=20, activebackground="black", activeforeground="#37ff00")
        Button_two.place(x=120, y=200)

        Button_three = Button(text="3", font=("ariel", 40), fg="#37ff00", background="Black", bd=5, relief=RAISED, padx=20, activebackground="black", activeforeground="#37ff00")
        Button_three.place(x=240, y=200)

        Button_four = Button(text="4", font=("ariel", 40), fg="#37ff00", background="Black", bd=5, relief=RAISED, padx=20, activebackground="black", activeforeground="#37ff00")
        Button_four.place(x=360, y=200)

        Button_five = Button(text="5", font=("ariel", 40), fg="#37ff00", background="Black", bd=5, relief=RAISED, padx=20, activebackground="black", activeforeground="#37ff00")
        Button_five.place(x=0, y=310)

        Button_six = Button(text="6", font=("ariel", 40), fg="#37ff00", background="Black", bd=5, relief=RAISED, padx=20, activebackground="black", activeforeground="#37ff00")
        Button_six.place(x=120, y=310)

        Button_seven = Button(text="7", font=("ariel", 40), fg="#37ff00", background="Black", bd=5, relief=RAISED, padx=20, activebackground="black", activeforeground="#37ff00")
        Button_seven.place(x=240, y=310)

        Button_eight = Button(text="8", font=("ariel", 40), fg="#37ff00", background="Black", bd=5, relief=RAISED, padx=20, activebackground="black", activeforeground="#37ff00")
        Button_eight.place(x=360, y=310)

        Button_nine = Button(text="9", font=("ariel", 40), fg="#37ff00", background="Black", bd=5, relief=RAISED, padx=20, activebackground="black", activeforeground="#37ff00")
        Button_nine.place(x=0, y=420)

        Button_zero = Button(text="0", font=("ariel", 40), fg="#37ff00", background="Black", bd=5, relief=RAISED, padx=20, activebackground="black", activeforeground="#37ff00")
        Button_zero.place(x=120, y=420)

        Button_color = Button(text="C", font=("Courier", 33), fg="#37ff00", background="Black", bd=5, relief=RAISED, padx=25, pady=13, activebackground="black", activeforeground="#37ff00", command=self.color_function)
        Button_color.place(x=240, y=420)

        Button_Submit = Button(text="S", font=("Courier", 33), fg="#37ff00", background="Black", bd=5, relief=RAISED, padx=26, pady=13, activebackground="black", activeforeground="#37ff00")
        Button_Submit.place(x=360, y=420)

        Button_addition = Button(text="+", font=("ariel", 40), fg="#37ff00", background="Black", bd=5, relief=RAISED, padx=20, activebackground="black", activeforeground="#37ff00")
        Button_addition.place(x=0, y=530)

        Button_substraction = Button(text="-", font=("ariel", 40), fg="#37ff00", background="Black", bd=5, relief=RAISED, padx=25, activebackground="black", activeforeground="#37ff00")
        Button_substraction.place(x=120, y=530)

        Button_division = Button(text="/", font=("ariel", 40), fg="#37ff00", background="Black", bd=5, relief=RAISED, padx=30, activebackground="black", activeforeground="#37ff00")
        Button_division.place(x=240, y=530)

        Button_multiplication = Button(text="*", font=("ariel", 40), fg="#37ff00", background="Black", bd=5, relief=RAISED, padx=24, activebackground="black", activeforeground="#37ff00")
        Button_multiplication.place(x=360, y=530)

    def one_function(self):
        pass



    def color_function(self):
        colors = ["#37ff00", "white", "black", "#fa1105", "#f7f300", "#02faf6", "#64faf7", "#02a7fa", "#41b7f2", "#5bbef0", "#306bf2", "#0534a1", "#0443d4", "#034efc", "#0702fa", "#060391", "#ff0095"]
        self.current_background_color = random.choice(colors)
        windows.config(background=f"{self.current_background_color}")






















if __name__ == '__main__':
    windows = Tk()
    calculator = Calculator(windows)
    windows.mainloop()
