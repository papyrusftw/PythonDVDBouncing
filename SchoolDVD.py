import tkinter as tk
import tkinter.messagebox
import random
class Project:
    def __init__(self):
        self.speed = 4
        self.dx = self.speed
        self.dy = self.speed
        self.bouncing = False
        self.Username = ""
        self.NameEntryWindow()
    
    def NameEntryWindow(self):
        self.NameWindow = tk.Tk()
        self.NameWindow.title("Enter Your Name")
        self.NameWindow.geometry("400x200+300+200")
        self.NameWindow.config(bg="white")
        self.NameWindow.resizable(False, False)
        self.NameLabel = tk.Label(self.NameWindow, text="Enter your name:", font=("Arial", 14), bg="white").pack(pady=20)
        self.NameEntry = tk.Entry(self.NameWindow, font=("Arial", 12))
        self.NameEntry.pack(pady=10)
        self.NameEntry.focus()
        self.ContinueButton = tk.Button(self.NameWindow, text="Continue", font=("Arial", 12),
        command=self.ProceedToMainWindow).pack(pady=10)
        self.NameWindow.mainloop()

    def ProceedToMainWindow(self):
        self.Username = self.NameEntry.get()
        if self.Username == "":
            tkinter.messagebox.showerror(title="No name", message="You have to enter a name!")
            return
        elif len(self.Username) > 20:
            tkinter.messagebox.showerror(title="Mr. Long name", message="Too long to be real")
            self.NameEntry.delete("0", "end")
            return
        self.NameWindow.destroy()
        self.WindowInitialization()
        self.CreateText()
        self.CreateButtons()
        self.WindowVisibility()
    
    def WindowInitialization(self):
        self.window = tk.Tk()
        self.window.title("DVD Bouncing")
        self.window.geometry("800x400+100+100")
        self.window.config(bg="white")
        self.window.resizable(False, False)
    
    def CreateText(self):
        self.TitleLabel = tk.Label(self.window,
        text=f"{self.Username}, do you like the classic DVD edge bouncing?", width=50,
        font=("Arial", 16),
        justify="center", bg="white")
        self.TitleLabel.pack(pady=10)
    
    def CreateButtons(self):
        self.YesButton = tk.Button(self.window, text="Yes", width=10, height=3, font=10, bg="white",
        command=self.ToggleBouncing)
        self.NoButton = tk.Button(self.window, text="No", width=10, height=3, font=10, bg="white",
        command=self.WhenNo)
        self.YesButton.place(x=250, y=50)
        self.NoButton.place(x=450, y=50)
    
    def ToggleBouncing(self):
        if self.bouncing:
            self.bouncing = False
            self.YesButton.config(text="Yes")
        else:
            self.bouncing = True
            self.YesButton.config(text="Stop")
            self.NoButton.place_forget()
            self.Bounce()
    
    def WhenNo(self):
        self.TitleLabel.config(text="Liar, everyone does!")
        self.NoButton.place_forget()
        if not self.bouncing:
            self.ToggleBouncing()
    
    def RandomColor(self):
        HexColor = f"#{random.randint(0, 0xFFFFFF):06x}"
        return HexColor
    
    def Bounce(self):
        if not self.bouncing:
            return
        x = self.YesButton.winfo_x()
        y = self.YesButton.winfo_y()
        ButtonWidth = self.YesButton.winfo_width()
        ButtonHeight = self.YesButton.winfo_height()
        WindowWidth = self.window.winfo_width()
        WindowHeight = self.window.winfo_height()
        Bounced = False
        if x + ButtonWidth + self.dx > WindowWidth or x + self.dx < 0:
            self.dx = -self.dx
            Bounced = True
        if y + ButtonHeight + self.dy > WindowHeight or y + self.dy < 0:
            self.dy = -self.dy
            Bounced = True
        if Bounced:
            self.YesButton.config(bg=self.RandomColor())
        self.YesButton.place(x=x + self.dx, y=y + self.dy)
        self.window.after(20, self.Bounce)
    
    def WindowVisibility(self):
        self.window.mainloop()
Project()