import tkinter as tk
from tkinter import ttk
from ctypes import windll

from menu import *
from config import *
from game import *
from end import *

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        try: 
            windll.shcore.SetProcessDpiAwareness(1) 
        except: 
            pass

        self.title("Connect 4")
        self.geometry("1024x768")
        self.resizable(False, False)

        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        button_font = ("Helvetica", 20)
        style = ttk.Style()
        style.configure("Custom.TButton", font=button_font, padding=10, width=30, height=5)

        self.frames = {}

        for FrameClass in (MainMenu, GameConfig, GameFrame, End_frame):
            frame_name = FrameClass.__name__
            frame = FrameClass(parent=self.container, controller=self)
            self.frames[frame_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MainMenu")

    def show_frame(self, frame_name, func_name=None, *args):
        frame = self.frames[frame_name]
        frame.tkraise()

        if func_name: 
            func = getattr(frame, func_name) 
            func(*args)


app = App()
app.mainloop()
