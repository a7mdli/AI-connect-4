import tkinter as tk
from tkinter import ttk

class GameConfig(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, padding=20)
        self.controller = controller
        self.configure(relief="ridge", borderwidth=5)

        title_label = ttk.Label(self, text="New Game Configuration", font=("Helvetica", 35, "bold"))
        title_label.pack(pady=60)

        self.selected_algorithm = tk.StringVar()
        option_frame = ttk.Frame(self, width=50) 
        option_frame.pack(pady=15)
        option_label = ttk.Label(option_frame, text="Choose Algorithm:", font=("Helvetica", 20)) 
        option_label.pack(side="left", padx=10)

        self.option_combobox = ttk.Combobox(option_frame, textvariable=self.selected_algorithm, font=("Helvetica", 20), state="readonly", width=30) 
        self.option_combobox['values'] = ("Minimax without alpha-beta pruning", "Minimax with alpha-beta pruning", "Expected Minimax") 
        self.option_combobox.current(0) 
        self.option_combobox.pack(side="left", padx=10, pady=10)

        line_frame = ttk.Frame(self, width=50) 
        line_frame.pack(pady=15)
        first_label = ttk.Label(line_frame, text="The function truncates the game tree after", font=("Helvetica", 20)) 
        first_label.pack(side="left", padx=5)
        entry = ttk.Entry(line_frame, font=("Helvetica", 15), width=5) 
        entry.pack(side="left", padx=5)
        vcmd = (self.register(self.on_validate), '%P') 
        entry.config(validate='key', validatecommand=vcmd)
        second_label = ttk.Label(line_frame, text="levels.(Default:10)", font=("Helvetica", 20)) 
        second_label.pack(side="left", padx=5)

        self.selected_player = tk.StringVar()
        option_2_frame = ttk.Frame(self, width=50) 
        option_2_frame.pack(pady=15)
        option_2_label = ttk.Label(option_2_frame, text="Choose Which Player Starts:", font=("Helvetica", 20)) 
        option_2_label.pack(side="left", padx=10)

        self.option_2_combobox = ttk.Combobox(option_2_frame, textvariable=self.selected_player, font=("Helvetica", 20), state="readonly", width=30) 
        self.option_2_combobox['values'] = ("Player", "Agent") 
        self.option_2_combobox.current(0) 
        self.option_2_combobox.pack(side="left", padx=10, pady=10)

        
        button1 = ttk.Button(self, text="Start Game", command=lambda: controller.show_frame("GameFrame","initialize_game",self.selected_algorithm.get()
                            , self.selected_player.get(), int(entry.get()) if entry.get() != '' else 10))
        button1.pack(pady=20, ipadx=20, ipady=10)
        button1.config(style="Custom.TButton")

    def on_validate(self, new_value):
        if new_value.isdigit() or new_value == '': 
            return True 
        return False
