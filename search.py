import chess
from constants import MATE, PIECE_VALUES, INFINITY
from evaluate import positional_advantage


# Conditions that can cause the game to end in a draw.
def is_drawn(board):
    return board.is_fivefold_repetition() \
        or board.is_insufficient_material() \
            or board.is_seventyfive_moves() \
                or board.is_stalemate()


# Move sorting policy based that prioritizes capturing moves. Used in the
# alpha-beta pruning technique.
def move_sorting_policy(board, move):
    moving_piece = board.piece_at(move.from_square)
    captured_piece = board.piece_at(move.to_square)
    order = 0 
    if captured_piece:
        order = PIECE_VALUES[captured_piece.piece_type] - PIECE_VALUES[moving_piece.piece_type]
    return order


# Minimax (Negamax) algorithm. It is a recursive algorithm that computes the
# optimal sequence of moves for both players. The function returns the best
# score and the principal variation (an optimal sequence of moves for both
# players).

# The depth parameter controls the depth of the search tree. A depth of 0
# means the function will evaluate the current position. A depth of 1 means
# the function will evaluate the current position and the next possible moves
# for both players, and so on. The function will stop the search when it
# reaches the specified depth.

# This function is slower and even a depth of 5 takes a long time to compute.
def minimax(board, depth):
    if depth <= 0:
        return positional_advantage(board), []
    
    if board.is_checkmate():
        return -MATE, []
    
    if is_drawn(board):
        return 0, []
    
    best_score = -INFINITY
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


# Minimax (Negamax) algorithm with alpha-beta pruning. It is a recursive
# algorithm that computes the optimal sequence of moves for both players. It
# works the same way as the minimax algorithm, but it prunes the search tree
# by eliminating branches that will not affect the final result.

# This is tracked by the additional variables alpha and beta. Alpha is the
# best score that the maximizing player can achieve, and beta is the best score
# that the minimizing player can achieve. If the algorithm finds a move that
# is better than the current best move for the maximizing player, it updates
# alpha. If the algorithm finds a move that is better than the current best move
# for the minimizing player, it updates beta.

# If the algorithm finds a move that is worse than the current best move for
# the maximizing player, it stops searching that branch because the minimizing
# player will not choose that move. If the algorithm finds a move that is worse
# than the current best move for the minimizing player, it stops searching that
# branch because the maximizing player will not choose that move.

# Since the pruning depends on the order of the moves, the function uses a move
# sorting policy to prioritize capturing moves. With these optimizations, the
# alpha-beta pruning algorithm is much faster than the minimax algorithm.
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

    pv = []
    for move in legal_moves:
        board.push(move)
        child_score, child_pv = alphabeta(board, depth - 1, -beta, -alpha)
        child_score = -child_score
        board.pop()

        if child_score >= beta:
            return beta, pv
        if child_score > alpha:
            alpha = child_score
            pv = [move] + child_pv

    return alpha, pv