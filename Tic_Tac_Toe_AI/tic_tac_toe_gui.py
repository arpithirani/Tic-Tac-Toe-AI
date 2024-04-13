import tkinter as tk
from tkinter import messagebox
from game_logic import TicTacToe

class TicTacToeGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic-Tac-Toe AI")

        self.game = TicTacToe()
        self.current_mode = tk.StringVar(self.root)
        self.current_mode.set("Easy")  # Default mode is Easy

        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.root, text=' ',
                                               font=('normal', 20), width=5, height=2,
                                               command=lambda row=i, col=j: self.make_move(row, col))
                self.buttons[i][j].grid(row=i, column=j)

        self.status_label = tk.Label(self.root, text=f"Player {self.game.current_player}'s turn", font=('normal', 14))
        self.status_label.grid(row=3, columnspan=3)

        # Dropdown menu for selecting game mode
        modes = ["Easy", "Medium", "Hard"]
        mode_dropdown = tk.OptionMenu(self.root, self.current_mode, *modes)
        mode_dropdown.grid(row=4, columnspan=3)

        #Reset Button
        reset_button = tk.Button(self.root, text="Reset", command=self.reset_game)
        reset_button.grid(row=5, column=0, columnspan=3, pady=10)

    def update_board(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]['text'] = self.game.board[i][j]

        if self.game.is_winner('X'):
            self.status_label.config(text="Player X wins!")
            messagebox.showinfo("Tic-Tac-Toe", f"Player 'X' wins!")
        elif self.game.is_winner('O'):
            self.status_label.config(text="Player O wins!")
            messagebox.showinfo("Tic-Tac-Toe", f"Player 'O' wins!")
        elif self.game.is_board_full():
            self.status_label.config(text="It's a draw!")
            messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
        else:
            self.status_label.config(text=f"Player {self.game.current_player}'s turn")

    def reset_game(self):
        # Clear the board and update buttons to initial state
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]['text'] = ' '  # Reset button text to empty
                self.game.board[i][j] = ' '  # Reset the game board to empty

        # Reset status label to current player's turn
        self.status_label.config(text=f"Player {self.game.current_player}'s turn")

    def ai_move(self):
        if self.current_mode.get() == "Easy":
            # Implement easy AI move (random move)
            self.game.make_easy_ai_move()
        elif self.current_mode.get() == "Medium":
            # Implement medium AI move (simplified minimax)
            self.game.make_medium_ai_move()
        elif self.current_mode.get() == "Hard":
            # Implement hard AI move (full minimax)
            self.game.make_hard_ai_move()

    def make_move(self, row, col):
        if self.game.make_move(row, col):
            self.update_board()
            if not self.game.is_game_over():
                self.ai_move()
                self.update_board()

    def run(self):
        self.root.mainloop()
