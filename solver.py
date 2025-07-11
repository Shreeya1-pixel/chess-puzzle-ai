import chess

def evaluate_board(board):
    if board.is_checkmate():
        return 9999 if board.turn == chess.BLACK else -9999
    return 0  # No mate

def minimax(board, depth, alpha, beta, maximizing, selected_pieces):
    if depth == 0 or board.is_game_over():
        return evaluate_board(board), []

    best_line = []
    if maximizing:
        max_eval = -float('inf')
        for move in board.legal_moves:
            piece = board.piece_type_at(move.from_square)
            if piece in selected_pieces:
                board.push(move)
                eval_score, line = minimax(board, depth-1, alpha, beta, False, selected_pieces)
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
            eval_score, line = minimax(board, depth-1, alpha, beta, True, selected_pieces)
            board.pop()
            if eval_score < min_eval:
                min_eval = eval_score
                best_line = [move] + line
            beta = min(beta, eval_score)
            if beta <= alpha:
                break
        return min_eval, best_line

