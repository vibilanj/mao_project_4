import argparse
import chess

from constants import INFINITY
from search import minimax, alphabeta
from utils import print_outcome

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
    default = 5,
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

board = chess.Board()
if args.algorithm == "minimax":
    search = lambda board: minimax(board, args.depth)
elif args.algorithm == "alphabeta":
    search = lambda board: alphabeta(board, args.depth, -INFINITY, INFINITY)

match args.mode:
    case "watch":
        while not board.is_game_over():
            print(board)
            score, pv = search(board)
            print(chess.COLOR_NAMES[board.turn], score, " ".join(map(str, pv)))
            print("\n")
            best_move = pv[0]
            board.push(best_move)

        print(board)
        print_outcome(board)

    case "play":
        if args.side == "black":
            print(board, "\n")
            _, pv = search(board)
            best_move = pv[0]
            board.push(best_move)
            print(f"Engine plays {best_move.uci()}")

        while not board.is_game_over():
            print(board, "\n")
            move = input("Enter your move: ")
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
            print(board, "\n")

            _, pv = search(board)
            best_move = pv[0]
            board.push(best_move)
            print(f"Engine plays {best_move.uci()}")
