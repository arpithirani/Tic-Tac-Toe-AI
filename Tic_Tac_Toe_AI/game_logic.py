import random


class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            return True
        return False
        
    def is_winner(self, player):
        # Check rows
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] == player:
                return True

        # Check columns
        for i in range(3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i] == player:
                return True

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == player:
            return True

        return False

    def is_board_full(self):
        return all(cell != ' ' for row in self.board for cell in row)

    def is_game_over(self):
        return self.is_winner('X') or self.is_winner('O') or self.is_board_full()
    
    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"
    
    def minimax(self, board, depth, is_maximizing):
        winner = self.is_winner("X") # Check for 'X' winner based on the current board state
        if winner:
            return -1
        winner = self.is_winner("O") # Check for 'O' winner based on the current board state
        if winner:
            return 1
        if self.is_board_full():
            return 0

        if is_maximizing:
            max_eval = -float("inf")
            for i in range(3):
                for j in range(3):
                    if board[i][j] == " ":
                        board[i][j] = "O"
                        eval_score = self.minimax(board, depth + 1, False)
                        board[i][j] = " "
                        max_eval = max(max_eval, eval_score)
            return max_eval
        else:
            min_eval = float("inf")
            for i in range(3):
                for j in range(3):
                    if board[i][j] == " ":
                        board[i][j] = "X"
                        eval_score = self.minimax(board, depth + 1, True)
                        board[i][j] = " "
                        min_eval = min(min_eval, eval_score)
            return min_eval
    
    def make_easy_ai_move(self):
        # Easy mode: Random move
        available_moves = [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == ' ']
        if available_moves:
            row, col = random.choice(available_moves)
            self.board[row][col] = 'O'

    def make_medium_ai_move(self):
        # Medium mode: Simplified minimax (one-ply lookahead)
        best_score = float('-inf')
        best_move = None
        depth = 2 # Modify the depth to make it less aggressive
        noise_probability = 0.2  # Adjust the probability of making a noisy move

        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    self.board[i][j] = 'O'
                    score = self.minimax(self.board, depth, False)
                    self.board[i][j] = ' '

                    if score > best_score:
                        best_score = score
                        best_move = (i, j)

        if best_move and random.random() > noise_probability:
            row, col = best_move
            self.board[row][col] = 'O'
        else:
            available_moves = [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == ' ']
            if available_moves:
                row, col = random.choice(available_moves)
                self.board[row][col] = 'O'

    def make_hard_ai_move(self):
        # Hard mode: Full minimax
        best_score = float('-inf')
        best_move = None
        depth = 4

        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    self.board[i][j] = 'O'
                    score = self.minimax(self.board, depth, False)
                    self.board[i][j] = ' '

                    if score > best_score:
                        best_score = score
                        best_move = (i, j)

        if best_move:
            row, col = best_move
            self.board[row][col] = 'O'
