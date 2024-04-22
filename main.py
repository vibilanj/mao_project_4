import argparse
import chess

from constants import INFINITY
from search import minimax, alphabeta
from utils import print_board, print_outcome

# Parses the command line arguments.
parser = argparse.ArgumentParser("Chess engine")
parser.add_argument(
    "mode",
    type = str,
    default = "watch",
    choices = ["watch", "play"],
    help = "the mode to run the program in"
)
parser.add_argument(
    "-d", "--depth",
    type = int,
    default = 3,
    help = "engine search depth"
)
parser.add_argument(
    "-a", "--algorithm",
    type = str,
    default = "alphabeta",
    choices = ["minimax", "alphabeta"],
    help = "the engine search algorithm"
)
parser.add_argument(
    "-s", "--side",
    type = str,
    default = "white",
    choices = ["white", "black"],
    help = "the side to play",
)
args = parser.parse_args()

# Initializes the chess board and the search algorithm.
board = chess.Board()
if args.algorithm == "minimax":
    search = lambda board: minimax(board, args.depth)
elif args.algorithm == "alphabeta":
    search = lambda board: alphabeta(board, args.depth, -INFINITY, INFINITY)

# Runs the program based on the mode.
match args.mode:
    # Watch mode: the engine plays against itself.
    case "watch":
        while not board.is_game_over():
            print_board(board)
            score, pv = search(board)
            print(chess.COLOR_NAMES[board.turn], score, " ".join(map(str, pv)))
            best_move = pv[0]
            board.push(best_move)

        print_board(board)
        print_outcome(board)

    # Play mode: the engine plays against the user.
    case "play":
        # If the engine is playing as black, it will make the first move.
        if args.side == "black":
            print_board(board)
            _, pv = search(board)
            best_move = pv[0]
            board.push(best_move)
            print(f"Engine plays {best_move.uci()}")

        # Captures the user's move and makes the engine's move until the
        # game is over.
        while not board.is_game_over():
            print_board(board)
            move = input("Enter your move: ").strip()
            try:
                board.push_san(move)
            except chess.InvalidMoveError:
                print("Invalid move")
                continue
            except chess.IllegalMoveError:
                print("Illegal move")
                continue
            except chess.AmbiguousMoveError:
                print("Ambiguous move")
                continue
            print_board(board)

            _, pv = search(board)
            best_move = pv[0]
            board.push(best_move)
            print(f"Engine plays {best_move.uci()}")

        print_board(board)
        print_outcome(board)
