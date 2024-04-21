import chess
from constants import INFINITY
from search import minimax, alphabeta
from evaluate import material_advantage, positional_advantage

board = chess.Board()

# board.push_san("e4")
# board.push_san("e5")
# board.push_san("Nf3")
# board.push_san("Nc6")
# board.push_san("Bb5")
# board.push_san("a6")

# print(board)
# print("WHITE to play" if board.turn else "BLACK to play")
# print(-material_advantage(board), -positional_advantage(board))

while not board.is_game_over():
    print(board)
    depth = 5

    # score, pv = minimax(board, depth)
    score, pv = alphabeta(board, depth, -INFINITY, INFINITY)
    print(chess.COLOR_NAMES[board.turn], score, " ".join(map(str, pv)))
    print("\n")

    best_move = pv[0]
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