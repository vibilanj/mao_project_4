import chess
from constants import PIECE_VALUES, PIECE_POSITION_VALUES


# Evaluate the board based on the material advantage of the pieces. Piece
# values are based on the standard piece value system. White has a positive
# score if it has the advantage, and black has a negative score if it has the
# advantage. The score is the sum of the value of all the pieces on the board.
def material_advantage(board: chess.Board) -> int:
    score = 0
    for piece_type in chess.PIECE_TYPES:
        piece_mask = board.pieces_mask(piece_type, chess.WHITE)
        score += chess.popcount(piece_mask) * PIECE_VALUES[piece_type]
    for piece_type in chess.PIECE_TYPES:
        piece_mask = board.pieces_mask(piece_type, chess.BLACK)
        score -= chess.popcount(piece_mask) * PIECE_VALUES[piece_type]
    
    if board.turn == chess.BLACK:
        score = -score
    return score


# Evaluate the board based on the positional advantage of the pieces. Piece
# position values are based on the standard piece-square tables. White has a
# positive score if it has the advantage, and black has a negative score if it
# has the advantage. The score is the sum of the value of all the pieces on the
# board based on their position (includes both material and positional).
def positional_advantage(board: chess.Board) -> int:
    score = 0
    for piece_type in chess.PIECE_TYPES:
        for square in board.pieces(piece_type, chess.WHITE):
            score += PIECE_POSITION_VALUES[piece_type][square]
        for square in board.pieces(piece_type, chess.BLACK):
            score -= PIECE_POSITION_VALUES[piece_type][square ^ 56]

    if board.turn == chess.BLACK:
        score = -score
    return score + material_advantage(board)