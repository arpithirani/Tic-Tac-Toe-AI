**Understanding Tic-Tac-Toe**
• Tic-Tac-Toe is a game of two player. It is an "Xs and Os," board game often played on a 3x3 grid. \n
• The game is simple, yet it can be quite challenging and strategic. \n
• The objective of Tic-Tac-Toe is to form a line of three of your own symbols (either "X" or "O") either horizontally, vertically, or diagonally on the game board. \n

**Project Background**
• The primary objective of this project is to create a Tic-Tac-Toe AI capable of playing the game optimally and providing a challenging opponent for human players. \n
• The AI will play against a human opponent, making optimal decisions to achieve victory or a draw. \n
• The game allows you to play in three different modes: Easy, Medium, and Hard. \n
• In order to make strategic decisions in the game I have implemented minimax algorithm. \n
• Based on the selected difficulty level of the AI by I have adjusted the search depth. \n

**Project UI**
• Implemented using Tkinter library. \n
• The dropdown list allows you to adjust the difficulty of the AI. \n
• By Default the user is “X” and the AI is “O”. \n
• Clicking Reset clears the boards, and update it to the initial state. \n

**Minimax Algorithm**
• The AI will utilize the minimax algorithm to provide challenging gameplay and offer different levels of difficulty based on user preferences. \n
• From a given game state, it explores all possible moves, assigning scores based on the resulting board states. The AI player selects the move with the highest score (maximizing its advantage) while considering the opponent's best counter-move (minimizing AI's disadvantage).  \n
• When reaching terminal states (win, lose, or draw), the algorithm assigns scores (-1 for loss, 0 for draw, 1 for win), reflecting the outcome. \n
• Based on the difficulty level I have adjusted the depth of search. \n

**Easy AI Move**
• The Easy AI Mode selects a random move from the available moves on the board. \n
• At each turn, the AI identifies all empty or unoccupied positions on the game grid. It then randomly chooses one of these available spots to make its move. \n
• The opponent’s winning percentage is very high. \n

**Medium AI Move**
• The Medium AI Mode uses simplified version of minimax algorithm. \n
• To balance the difficulty the algorithm has a 2 moves depth of lookahead instead of exhaustively exploring all possible future scenarios. \n
• In addition, the mode introduces an element of unpredictability. It incorporates a probability-based noise factor, allowing for random moves to be made occasionally. \n

**Hard AI Move**
• The Hard AI Mode uses full-fledged minimax algorithm. \n
• It explores 4 moves ahead for all the possible future scenarios and evaluates the best course of action. \n
• This AI mode aims for precision and accuracy in decision-making, using calculated moves that prioritize long-term gains over immediate gains. \n
