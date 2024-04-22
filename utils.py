import chess


# Conditions that can cause the game to end in a draw.
def is_drawn(board):
    return board.is_fivefold_repetition() \
        or board.is_insufficient_material() \
            or board.is_seventyfive_moves() \
                or board.is_stalemate()


# Prints the chess board. It defaults to printing unicode characters with no
# borders. If unicode is set to False, it will print ASCII characters instead.
# If borders is set to True, it will print borders around the board.
def print_board(board, unicode = True, borders = False):
    if unicode:
        print(board.unicode(
            invert_color = True,
            borders = borders,
            empty_square = ".",
            orientation = board.turn
            ), "\n")
    else:
        print(board, "\n")


# Prints the outcome of the game based on the various conditions that can
# cause the game to end.
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
            print("Game not over!")