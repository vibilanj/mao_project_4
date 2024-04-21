import chess

def print_board(board):
    print(board.unicode(
        invert_color = True,
        borders = False,
        empty_square = ".",
        orientation = board.turn
        ), "\n")

def print_outcome(board):
        board.outcome().winner
        if board.is_checkmate():
            color = "White" if board.outcome().winner else "Black"
            print(f"Checkmate by {color}!")
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