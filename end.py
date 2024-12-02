import tkinter as tk
from tkinter import ttk

class End_frame(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, padding=20)
        self.controller = controller
        self.configure(relief="ridge", borderwidth=5)

        self.label_text = tk.StringVar()
        self.winner_label = ttk.Label(self, textvariable=self.label_text, font=("Helvetica", 35, "bold"))
        self.winner_label.pack(pady=70)

        self.player_score = tk.IntVar()
        self.player_label = ttk.Label(self, textvariable=self.player_score, font=("Helvetica", 25, "bold"))
        self.player_label.pack(pady=30)

        self.agent_score = tk.IntVar()
        self.agent_label = ttk.Label(self, textvariable=self.agent_score, font=("Helvetica", 25, "bold"))
        self.agent_label.pack(pady=30)

        button1 = ttk.Button(self, text="New Game", command=lambda: self.controller.show_frame("GameConfig"))
        button1.pack(pady=40, ipadx=20, ipady=10)
        button1.config(style="Custom.TButton")

        close_button = ttk.Button(self, text="Exit", command=self.controller.destroy)
        close_button.pack(pady=30, ipadx=20, ipady=10)
        close_button.config(style="Custom.TButton")

    def initialize_score(self, player_score, agent_score):
        self.label_text.set("Winner: Player") if player_score>agent_score else self.label_text.set("Winner: Agent") if agent_score>player_score else self.label_text.set("Draw")
        self.player_score.set("Player score: "+str(player_score))
        self.agent_score.set("Player score: "+str(agent_score))
