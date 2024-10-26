from tkinter import *
import random


class StopWatch:


    def __init__(self, windows) -> None:

        self.windows = windows
        self.windows.title("StopWatch")
        self.windows.geometry("1000x510")
        self.windows.config(background="Black")
        self.running = False
        self.Time_interval = 500           # Mili-seconds
        self.Time_Eclipsed = 0
        # self.windows.overrideredirect(True)      # overrideredirect(True) is used to remove title-bar
        

        # icon = PhotoImage(file="D:\\Vids and Pics\\Pictures\\GUI Icons\\watch1.png")
        # self.windows.iconphoto(windows, icon)

        self.Time = Label(text="00:00:00", font=("Ariel", 120), bg="Black", fg="White")
        self.Time.place(x=170, y=35)

        self.start_stop_button = Button(text="Start", font=("Courier", 40), fg="#37ff00", bg="Black", activebackground="black", activeforeground="#37ff00", border=10, relief=RAISED, command=self.Toggle_Start_Stop_button)
        self.start_stop_button.place(y=300, x=220)

        self.Reset_button = Button(text="Reset", font=("Courier", 40), fg="#0000ff", bg="Black", activebackground="black", activeforeground="#0000ff", border=10, relief=RAISED, command=self.Toggle_Reset_Button)
        self.Reset_button.place(y=300, x=550)

        self.Color_Changer_button = Button(text="Color Changer", font=("Courier", 15), fg="White", bg="Black", activebackground="black", activeforeground="White", border=10, relief=RAISED, command=self.Color_Changer)
        self.Color_Changer_button.place(y=450, x=400)




    def Reset_During_Running(self):
        self.Time_Eclipsed = 0
        self.Stop()
        Minutes, Seconds = divmod(self.Time_Eclipsed // 1000, 60)
        Hours, Ninutes = divmod(Minutes, 60)
        self.Time_String = f"{Hours:02}:{Minutes:02}:{Seconds:02}"
        self.Time.config(text=self.Time_String)
        self.windows.title(f"{self.Time_String}")


    def Reset_During_Not_Running(self):
        self.Time_Eclipsed = 0
        Minutes, Seconds = divmod(self.Time_Eclipsed // 1000, 60)
        Hours, Ninutes = divmod(Minutes, 60)
        self.Time_String = f"{Hours:02}:{Minutes:02}:{Seconds:02}"
        self.Time.config(text=self.Time_String)
        self.windows.title(f"{self.Time_String}")


    def Start(self):
        self.running = True
        self.Update()
        self.start_stop_button.config(text="Stop", font=("Courier", 40), fg="Red", bg="Black", activebackground="black", activeforeground="Red", border=10, relief=RAISED, command=self.Stop)
        

    def Stop(self):
        self.running = False
        self.start_stop_button.config(text="Start", font=("Courier", 40), fg="#37ff00", bg="Black", activebackground="black", activeforeground="#37ff00", border=10, relief=RAISED, command=self.Start)


    def Update(self):
        if self.running:
            self.Time_Eclipsed += self.Time_interval
            Minutes, Seconds = divmod(self.Time_Eclipsed // 1000, 60)
            Hours, Ninutes = divmod(Minutes, 60)
            self.Time_String = f"{Hours:02}:{Minutes:02}:{Seconds:02}"
            self.Time.config(text=self.Time_String)
            self.windows.after(self.Time_interval, self.Update)
            self.windows.title(f"{self.Time_String}")


    def Toggle_Start_Stop_button(self):
        if self.running == True:
            self.Stop()
        elif self.running == False:
            self.Start()

    def Toggle_Reset_Button(self):
        if self.running == True:
            self.Reset_During_Running()
        elif self.running == False:
            self.Reset_During_Not_Running()

    def Color_Changer(self):
        self.Background_Colors = ['#37ff00', 'White', '#1e04c7', '#ff0000', 'Black', '#00e5ff', '#cc00ff', '#ff00bf', '#ff0077', '#00ffee', '#00ffaa', '#eeff00', '#5ee081']
        self.Current_Background_Color = random.choice(self.Background_Colors)    # random.choice(any collection) picks random item from the given collection
        self.windows.config(background=self.Current_Background_Color)
        self.Time.config(background=self.Current_Background_Color)

        if self.Current_Background_Color == 'White' or self.Current_Background_Color == '#00e5ff' or self.Current_Background_Color == '#00ffee' or self.Current_Background_Color == '#00ffaa' or self.Current_Background_Color == '#eeff00':
            self.Time.config(foreground='Black')
        else:
            self.Time.config(foreground='White')



if __name__ == '__main__':
    windows = Tk()
    StopWatch = StopWatch(windows)
    windows.mainloop()
