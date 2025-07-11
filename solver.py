import chess

def evaluate_board(board, ply):
    if board.is_checkmate():
        # Mate found: positive for delivering mate, negative for being mated
        return 10000 - ply if not board.turn else -10000 + ply
    return 0

def minimax(board, depth, alpha, beta, maximizing, selected_piece_types, ply=0):
    if depth == 0 or board.is_game_over():
        return evaluate_board(board, ply), []

    best_line = []

    if maximizing:
        max_eval = -float('inf')
        for move in board.legal_moves:
            if selected_piece_types is not None:
                piece = board.piece_at(move.from_square)
                if piece is None or piece.piece_type not in selected_piece_types:
                    continue
            board.push(move)
            eval_score, line = minimax(board, depth-1, alpha, beta, False, selected_piece_types, ply+1)
            board.pop()
            if eval_score > max_eval:
                max_eval = eval_score
                best_line = [move] + line
            alpha = max(alpha, eval_score)
            if beta <= alpha:
                break
        return max_eval, best_line
    else:
        min_eval = float('inf')
        for move in board.legal_moves:
            board.push(move)
            eval_score, line = minimax(board, depth-1, alpha, beta, True, selected_piece_types, ply+1)
            board.pop()
            if eval_score < min_eval:
                min_eval = eval_score
                best_line = [move] + line
            beta = min(beta, eval_score)
            if beta <= alpha:
                break
        return min_eval, best_line

def find_forced_mate(board, mate_in, selected_piece_types):
    depth = mate_in * 2
    score, line = minimax(board, depth, -float('inf'), float('inf'), True, selected_piece_types)
    # Accept only if it's a forced mate in the given depth
    if (board.turn and score >= 10000 - depth) or (not board.turn and score <= -10000 + depth):
        return line
    return None
