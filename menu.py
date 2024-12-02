from tkinter import ttk

class MainMenu(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, padding=20)
        self.controller = controller
        self.configure(relief="ridge", borderwidth=5)

        title_label = ttk.Label(self, text="Main Menu", font=("Helvetica", 35, "bold"))
        title_label.pack(pady=70)

        button1 = ttk.Button(self, text="New Game", command=lambda: controller.show_frame("GameConfig"))
        button1.pack(pady=40, ipadx=20, ipady=10)
        button1.config(style="Custom.TButton")

        close_button = ttk.Button(self, text="Exit", command=controller.destroy)
        close_button.pack(pady=30, ipadx=20, ipady=10)
        close_button.config(style="Custom.TButton")

