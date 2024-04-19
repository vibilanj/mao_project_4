import chess
from constants import INFINITY
from search import search

board = chess.Board()

while not board.is_game_over():
    print(board)
    depth = 5

    score, moves = search(board, depth, -INFINITY, +INFINITY)
    print(chess.COLOR_NAMES[board.turn], score, " ".join(map(str, moves)))

    best_move = moves[0]
    board.push(best_move)

print(board)
if board.is_checkmate():
    print("Checkmate!")
elif board.is_stalemate():
    print("Draw by stalemate!")
elif board.is_insufficient_material():
    print("Draw by insufficient material!")
elif board.is_seventyfive_moves():
    print("Draw by seventyfive moves!")
elif board.is_fivefold_repetition():
    print("Draw by fivefold repetition!")
else:
    print("Unknown game over!")