import chess
from constants import MATE, PIECE_VALUES, INFINITY
from evaluate import positional_advantage

def is_drawn(board):
    return board.is_fivefold_repetition() \
        or board.is_insufficient_material() \
            or board.is_seventyfive_moves() \
                or board.is_stalemate()

def move_sorting_policy(board, move):
    moving_piece = board.piece_at(move.from_square)
    captured_piece = board.piece_at(move.to_square)
    order = 0 
    if captured_piece:
        # order = PIECE_VALUES[captured_piece.piece_type] - PIECE_VALUES[moving_piece.piece_type]
        order = PIECE_VALUES[captured_piece.piece_type] - moving_piece.piece_type
    return order

# Minimax (negamax) algorithm. Depth of 5 is already quite slow.
def minimax(board, depth):
    if depth <= 0:
        return positional_advantage(board), []
    
    if board.is_checkmate():
        return -MATE, []
    
    if is_drawn(board):
        return 0, []
    
    best_score = -INFINITY
    # Principal variation (an optimal sequence of moves for both players)
    pv = []
    for move in board.legal_moves:
        board.push(move)
        child_score, child_pv = minimax(board, depth - 1)
        child_score = -child_score
        board.pop()

        if child_score > best_score:
            best_score = child_score
            pv = [move] + child_pv

    return best_score, pv

def alphabeta(board, depth, alpha, beta):
    if depth <= 0:
        return positional_advantage(board), []

    if board.is_checkmate():
        return -MATE, []

    if is_drawn(board):
        return 0, []

    legal_moves = sorted(board.legal_moves,
                         key = lambda m: move_sorting_policy(board, m),
                         reverse=True)

    best_score = -INFINITY
    pv = []
    for move in legal_moves:
        board.push(move)
        child_score, child_pv = alphabeta(board, depth - 1, -beta, -alpha)
        child_score = -child_score
        board.pop()

        if child_score >= beta:
            best_score = child_score
            if best_score > alpha:
                alpha = best_score
                pv = [move] + child_pv

    return alpha, pv