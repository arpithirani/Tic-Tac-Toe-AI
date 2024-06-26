**Understanding Tic-Tac-Toe** <br />
• Tic-Tac-Toe is a game of two player. It is an "Xs and Os," board game often played on a 3x3 grid. <br />
• The game is simple, yet it can be quite challenging and strategic. <br />
• The objective of Tic-Tac-Toe is to form a line of three of your own symbols (either "X" or "O") either horizontally, vertically, or diagonally on the game board. <br />

**Project Background** <br />
• The primary objective of this project is to create a Tic-Tac-Toe AI capable of playing the game optimally and providing a challenging opponent for human players. <br />
• The AI will play against a human opponent, making optimal decisions to achieve victory or a draw. <br />
• The game allows you to play in three different modes: Easy, Medium, and Hard. <br />
• In order to make strategic decisions in the game I have implemented minimax algorithm. <br />
• Based on the selected difficulty level of the AI by I have adjusted the search depth. <br />

**Project UI** <br />
• Implemented using Tkinter library. <br />
• The dropdown list allows you to adjust the difficulty of the AI. <br />
• By Default the user is “X” and the AI is “O”. <br />
• Clicking Reset clears the boards, and update it to the initial state. <br />

**Minimax Algorithm** <br />
• The AI will utilize the minimax algorithm to provide challenging gameplay and offer different levels of difficulty based on user preferences. <br />
• From a given game state, it explores all possible moves, assigning scores based on the resulting board states. The AI player selects the move with the highest score (maximizing its advantage) while considering the opponent's best counter-move (minimizing AI's disadvantage). <br />
• When reaching terminal states (win, lose, or draw), the algorithm assigns scores (-1 for loss, 0 for draw, 1 for win), reflecting the outcome. <br />
• Based on the difficulty level I have adjusted the depth of search.

**Easy AI Move** <br />
• The Easy AI Mode selects a random move from the available moves on the board. <br />
• At each turn, the AI identifies all empty or unoccupied positions on the game grid. It then randomly chooses one of these available spots to make its move.  <br />
• The opponent’s winning percentage is very high. <br />

**Medium AI Move** <br />
• The Medium AI Mode uses simplified version of minimax algorithm. <br />
• To balance the difficulty the algorithm has a 2 moves depth of lookahead instead of exhaustively exploring all possible future scenarios. <br />
• In addition, the mode introduces an element of unpredictability. It incorporates a probability-based noise factor, allowing for random moves to be made occasionally. <br />

**Hard AI Move** <br />
• The Hard AI Mode uses full-fledged minimax algorithm. <br />
• It explores 4 moves ahead for all the possible future scenarios and evaluates the best course of action. <br />
• This AI mode aims for precision and accuracy in decision-making, using calculated moves that prioritize long-term gains over immediate gains. <br />
