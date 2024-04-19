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
        order = PIECE_VALUES[captured_piece.piece_type] - PIECE_VALUES[moving_piece.piece_type]
    return order

# Minimax (Negamax variant) with Alpha-beta pruning
def search(board, depth, alpha, beta):
    if depth <= 0:
        return positional_advantage(board), []
    
    if board.is_checkmate():
        return -MATE, []
    
    if is_drawn(board):
        return 0, []
    
    legal_moves = sorted(board.legal_moves, reverse = True,
                         key = lambda m: move_sorting_policy(board, m))
    
    best_score = -INFINITY
    best_moves = []
    for move in legal_moves:
        board.push(move)

        child_score, child_moves = search(board, depth - 1, -beta, -alpha)
        child_score = -child_score
        board.pop()

        if child_score >= beta:
            return beta, []
        
        if child_score > best_score:
            best_score = child_score
            if best_score > alpha:
                alpha = best_score
                best_moves = [move] + child_moves

        return alpha, best_moves