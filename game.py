import tkinter as tk
from tkinter import ttk

import test_funcs as test
from Minimax import minimax

class GameFrame(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, padding=20)
        self.controller = controller
        self.configure(relief="ridge", borderwidth=5)

        self.player_score = tk.IntVar(value=0)
        self.agent_score = tk.IntVar(value=0)

        self.player1_name_label = ttk.Label(self, text="Player:", font=("Helvetica", 20), foreground="red")
        self.player1_name_label.grid(row=0, column=0, padx=10, pady=10)
        self.player1_score_label = ttk.Label(self, textvariable=self.player_score, font=("Helvetica", 20))
        self.player1_score_label.grid(row=0, column=1, padx=10, pady=10)
        
        self.player2_name_label = ttk.Label(self, text="Agent:", font=("Helvetica", 20), foreground="#DAA520")
        self.player2_name_label.grid(row=0, column=2, padx=10, pady=10)
        self.player2_score_label = ttk.Label(self, textvariable=self.agent_score, font=("Helvetica", 20))
        self.player2_score_label.grid(row=0, column=3, padx=10, pady=10)

        end_button = ttk.Button(self, text="End Game", command=lambda: controller.show_frame("GameConfig"), width=50)
        end_button.grid(row=2, column=1, columnspan=2)


    def initialize_game(self, algorithm, turn, k):
        self.algorithm = algorithm
        self.turn = turn
        self.k = k
        self.play_count = 0
        self.player_score.set(0)
        self.agent_score.set(0)
        self.game_grid = [["e" for _ in range(7)] for _ in range(6)]
        self.grid_canvas = tk.Canvas(self, width=700, height=600, bg="blue")
        self.grid_canvas.grid(row=1, column=0, columnspan=4, padx=120, pady=20)
        self.grid_canvas.bind("<Button-1>", self.handle_click)

        self.oval_ids = []
        self.draw_grid()
        if self.turn=="Agent":
            self.agent_move()
            self.turn = "Player"
    
    def draw_grid(self):
        rows, cols = 6, 7
        cell_width, cell_height = 100, 100
        oval_padding = 15
        for row in range(rows):
            row_ids = []
            for col in range(cols):
                x1 = col * cell_width + oval_padding 
                y1 = row * cell_height + oval_padding 
                x2 = x1 + cell_width - 2 * oval_padding 
                y2 = y1 + cell_height - 2 * oval_padding
                oval_id = self.grid_canvas.create_oval(x1, y1, x2, y2, fill="white", outline="black")
                row_ids.append(oval_id) 
            self.oval_ids.append(row_ids)
    
    def handle_click(self, event):
        if self.turn=="Agent":
            return
        
        clicked_col = event.x // 100
        if self.game_grid[0][clicked_col]!="e":
            return       
        self.turn = "Agent"
        self.put_disc(clicked_col, "Player")
        if self.play_count==42:
            self.controller.show_frame("End_frame", "initialize_score", self.player_score.get(), self.agent_score.get())
            return
        self.agent_move()
        if self.play_count==42:
            self.controller.show_frame("End_frame", "initialize_score", self.player_score.get(), self.agent_score.get())
            return
        self.turn = "Player"
    
    def agent_move(self):
        if self.algorithm=="Minimax without alpha-beta pruning":
            self.put_disc(minimax(self.game_grid, self.k, False), "Agent")
        elif self.algorithm=="Minimax with alpha-beta pruning":
            self.put_disc(minimax(self.game_grid, self.k, True), "Agent")
        else:
            self.put_disc(test.expected_minimax(self.game_grid), "Agent")

    def put_disc(self, col_num, player):
        if self.game_grid[0][col_num]!="e":
            return
        self.play_count += 1
        row = 0
        while row<6 and self.game_grid[row][col_num]=="e":
            row += 1
        row -= 1
        if player=="Player":
            self.game_grid[row][col_num] = "p"
            self.grid_canvas.itemconfig(self.oval_ids[row][col_num], fill="red")
        else:
            self.game_grid[row][col_num] = "a"
            self.grid_canvas.itemconfig(self.oval_ids[row][col_num], fill="yellow")

        self.update_score(player)
        self.grid_canvas.update_idletasks()

    def update_score(self, player):
        rows = 6
        cols = 7
        count = 0

        if player=="Player":
            value = 'p'
        else :
            value = 'a'

        for row in range(rows):
            for col in range(cols - 3):
                if all(self.game_grid[row][col + i] == value for i in range(4)):
                    count += 1

        for row in range(rows - 3):
            for col in range(cols):
                if all(self.game_grid[row + i][col] == value for i in range(4)):
                    count += 1

        for row in range(3, rows):
            for col in range(cols - 3):
                if all(self.game_grid[row - i][col + i] == value for i in range(4)):
                    count += 1

        for row in range(rows - 3):
            for col in range(cols - 3):
                if all(self.game_grid[row + i][col + i] == value for i in range(4)):
                    count += 1

        if player=="Player":
            self.player_score.set(count)
        else:
            self.agent_score.set(count)
