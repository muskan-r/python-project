import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")

        self.current_player = "X"
        self.board = [""] * 9

        self.buttons = []
        self.create_buttons()

    def create_buttons(self):
        for i in range(9):
            button = tk.Button(
                self.root, text="", font=("Arial", 32), width=5, height=2,
                command=lambda i=i: self.make_move(i)
            )
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

    def make_move(self, index):
        if self.board[index] == "" and not self.check_winner():
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)

            winning_combo = self.check_winner()
            if winning_combo:
                for i in winning_combo:
                    self.buttons[i].config(bg="lightgreen")
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.root.after(1000, self.reset_game)
            elif "" not in self.board:
                messagebox.showinfo("Game Over", "It's a draw!")
                self.root.after(1000, self.reset_game)
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        b = self.board
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        for condition in win_conditions:
            if b[condition[0]] == b[condition[1]] == b[condition[2]] != "":
                return condition  # Return winning combo
        return None

    def reset_game(self):
        self.board = [""] * 9
        self.current_player = "X"
        for button in self.buttons:
            button.config(text="", bg="SystemButtonFace")  # Reset color too

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
