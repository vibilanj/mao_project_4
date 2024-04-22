# Modelling and Optimization Project 4

## Introduction

This project is a chess engine that uses the minimax algorithm with alpha-beta pruning to select the best move. The engine uses a heuristic evaluation function to evaluate the board position and make the best move. The engine is capable of playing against another human or against itself.

## Implementation Details

The project is implemented in Python. The chess engine uses the `python-chess` library to represent the board and generate moves. Although this could have been done as a part of the project, it would have taken more time to get the implementation right, especially with the various rules of chess. This also meant that I could spend more time on the position evaluation and move selection algorithms.

Another change that was made from the proposal was that the engine does not use the UCI protocol. Instead, the engine can be played against using the terminal. This was done to simplify the project and focus on the core functionalities. However, adding the UCI functionality should be relatively straightforward if needed.

Here are the descriptions of the five Python files in the project. Furthermore, the code in each file is documented with comments to explain each part in greater detail.

### `constants.py`

This file contains the constants used throughout the project. The constants include the values assigned to each piece, each position of each piece, checkmate and infinity.

The values for checkmate and infinity were chosen to be large values to ensure that the engine would always choose a move that would avoid checkmate and lead to a win.

The values assigned to each piece was chosen based on the standard values used in chess. The values were chosen to reflect the relative strength of each piece. For instance, a pawn is worth 100 points while a queen is worth 900 points.

The position values for each piece were chosen based on the standard values used in chess. The values were chosen to reflect the relative strength of each piece in each position. For instance, a knight in the center of the board is worth more points than a knight on the edge or corner of the board. This reflects the idea that a knight in the center controls more squares and is more active than a knight on the edge or corner.

### `evaluate.py`

This file contains the evaluation functions used to evaluate the board position. The evaluation functions are used to determine the value of the board position and help the engine understand whether a move is good or bad.

There are two evaluation functions in this file. The first evaluation function is a simple evaluation function called `material_advantage`. It counts the number of pieces on the board and multiplies them by the value of each piece to get the total value of the board position.

The second evaluation function `position_advantage` is a more complex evaluation function that also takes into account the position of each piece. It builds on the first evaluation function by adding the position values of each piece to the total value of the board position.

The evaluation functions return a positive value if the board position is good for white and a negative value if the board position is good for black. The evaluation functions return zero if the board position is equal for both players.

### `search.py`

This file contains the search functions used to search for the best move. They look at all the possible moves and evaluate the board position after each move to determine the best move. In essence this represents a tree search algorithm as the engine continually looks at the possible moves for each previous move. This is a non-trivial task as the number of possible moves increases exponentially with the depth of the search.

First, there is a helper function `move_sorting_policy` that is used to sort the generated moves by prioritizing attacking moves like captures and checks. The importance of this function will be explained later.

There are two search functions in this file. Both search functions return the best score and the principal variation. The principal variation is the optimal sequence of moves that lead to the best score. They evaluate the board up to a specificed depth and return the best move found. A depth of 0 means that the engine only evaluates the current board position and returns the best move without looking ahead.

#### Minimax Algorithm

The first search function `minimax` uses the minimax algorithm to recursively search the tree of possible moves. Specifically, it uses the negamax algorithm which differs from minimax in that instead of using a maximising and minimising player, it always tries to maximise the score. However, when it is the minimizing players turn, it uses the negative of the score which essentially minimizes the score. This works because chess is a zero-sum game.

There are multiple base cases for the function. The first base case is when the depth is 0, in which case the function evaluates the board position using the evaluation function. The second base case is when the game ends in checkmate, in which case a large negative value is returned. Lastly, the third base case is when the game ends in a draw, in which case a value of 0 is returned.

The recursive step involves generating all the possible moves and evaluating the board position at `depth - 1`. The negation of the child's score is taken as the score for the current board position. If the child's score is better than the current best score, the best score is updated and the principal variation is updated with the current move.

#### Alpha-Beta Pruning

The second search function `alphabeta` builds on the previous algorithm by using the alpha-beta pruning technique to reduce the number of nodes that need to be evaluated. It stops evaluating a move when at least one possibility has been found that proves the move to be worse than a previously examined move. This 'prunes' the tree of possible moves and reduces the number of nodes that need to be evaluated.

The algorithm maintains two values, `alpha` and `beta`, which respectively represent the minimum score that the maximizing player is assured of and the maximum score that the minimizing player is assured of.  Initially, `alpha` is negative infinity and `beta` is positive infinity, i.e. both players start with their worst possible score. Whenever the maximum score that the minimizing player (the `beta` player) is assured of becomes less than the minimum score that the maximizing player (the `alpha` player) is assured of (`beta < alpha`), the maximizing player need not consider further descendants of this node, as they will never be reached in the actual play.

Since the effectiveness of alpha-beta pruning depends on the order of the moves (if a good move is found early on, it can prune moves worse than it), the function uses the move-sorting policy introduced earlier. With these optimizations, the alpha-beta pruning algorithm is much faster than the minimax algorithm. The minimax algorithm becomes quite slow at a depth of $5$, while the alpha-beta pruning algorithm can go up to a depth of $5$. This translates to the alpha-beta search algorithm playing better as it can look further ahead and evaluate more moves in the same amount of time.

### `utils.py`

This file contains utility functions used throughout the project. The `is_drawn` function checks whether any of the four conditions that result in a draw are satisfied. The `print_board` function prints the board in a human-readable format. It defaults to a unicode representation with no borders, but can be changed to a text representation or a unicode representation with borders. Lastly, the `print_outcome` function prints the outcome of the game based on the various conditions that can cause a game to end.

### `main.py`

This file is the main runner file. It contains the command line argument parsing logic and the main program flow. The user can provide the mode to run the program in but the default is `watch`. The `watch` mode makes the engine play against itself, while the `play` mode allows the user to play against the engine.

The user can provide the depth to search to using the `--d` or `--depth` flag and the algorithm to use using the `-a` or `--algorithm` flag. The algorithms available are `minimax` and `alphabeta`. The default depth is $3$ and the default algorithm is `alphabeta`.

Lastly, when playing against the engine, the user can provide the color to play as using the `-s` or `--side` argument and the engine will play as the opposite color. The options are `white` and `black`. The default side is `white`.

The program flow involves initializing the board and search algorithm, running the game loop, and printing the outcome of the game. When the mode is `watch`, the engine plays both sides against itself. It prints the board in each step, Additionally it prints information about whose turn it is to move next, the computer score and principal variation.

When the mode is `play`, the user can play against the engine. The user can input moves in algebraic notation and the engine will respond with its move. The game continues until the game ends in checkmate or a draw.

#### Algebraic Notation

Algebraic notation is a standard way to represent chess moves. It is a system for recording chess moves using the position of the pieces on the board. Each square on the board is represented by a unique combination of a letter and a number. The letters represent the files (columns from A to H) and the numbers represent the ranks (rows from 1 to 8). White starts on the bottom (rows 1 and 2) while black starts on the top (rows 7 and 8).

The pieces are (usually) represented by their first letter (K for king, Q for queen, R for rook, B for bishop, N for knight, and no letter for pawn). Captures are represented by an 'x' and check is represented by a '+'. The move is represented by the piece letter followed by the destination square. For example, the move `e4` means moving the pawn in the e file to the 4th rank. The move `Nf3` means moving the knight to the f3 square. The move `Qxb7` means moving the queen to capture the piece on the b7 square.

However, in this program, you can simply input the starting square and the ending square. For example if you want to move the pawn from e2 to e4, you can simply input `e2e4`. If you want to move the knight from g1 to f3, you can input `g1f3`.

## Further Improvements

The program can be improved in several ways. Some of the improvements that can be made include search optimizations such as iterative deepening where the engine searches to a certain depth and then increases the depth until a time limit is reached. This allows the engine to search deeper in the same amount of time. Additionally, the engine can be improved by using time constraints to limit the amount of time spent on each move. This allows the engine to play at a competitive level against human players.

The engine can be further improved by improvings its evaluation functions and heuristics. The evaluation functions can be improved by taking into account more features of the board position such as pawn structure, king safety, and piece activity. The heuristics can be improved by using more advanced techniques such as neural networks or machine learning.

Performance of the engine can be optimized by parallelizing the search algorithm. This allows the engine to search multiple branches of the tree in parallel and find the best move faster. Additionally, the engine can be optimized by using memoization to store the results of previous searches and avoid recomputing them.

Lastly, the user experience can be improved by adding a graphical interface to play against the engine. This allows the user to see the board position and move pieces using a mouse. Additionally, the engine can be connected to the Lichess API to play against other players online. This would allow anyone to easily play against the engine and test their skills. The engine could also learn from the games it plays and improve its play over time.

Overall, the program is a good starting point for a chess engine and can be improved in many ways to make it more competitive and user-friendly. However, the main goal of learning and applying techniques from optimization, such as heuristic evaluation and search algorithms, has been achieved. The engine is capable of playing chess at a decent level in a reasonable amount of time.

## How to Run

### Setting up the environment

1. Ensure that you have a working install of Python 3.11.8.
2. Navigate to the directory containing the project in your terminal.
3. Create a Python virtual environment by running `python3 -m venv .venv`.
4. Use the virtual environment with `source .venv/bin/activate`.
5. Install the necessary packages using `pip install -r requirements.txt`.

### Running the program (CHANGE LATER)

1. Navigate to the project directory.
2. Make sure that the virtual environment is activated. If it is not, use `source .venv/bin/activate`.
3. Run the program using `python main.py` and pass in any optional arguments.
    - You can use the `-h` flag to see the help message and the available arguments.
4. By default, the program will run in `watch` mode with a depth of 3 and the alpha-beta algorithm.
    - You can change the depth and algorithm using the `-d` and `-a` flags. For example, `python main.py -d 4 -a minimax` would run the program with a depth of 4 and the minimax algorithm.
    - You can change the mode to `play` to play against the engine. You can additionally specify the side to play as using the `-s` flag. For example, `python main.py play -s black` would play as black against the engine.
4. Watch the engine play against itself or play against the engine using algebraic notation.
