import streamlit as st
import chess
import chess.svg
from solver import minimax

st.set_page_config(page_title="♟️ AI Chess Puzzle Generator", layout="wide")

st.title("♟️ AI Chess Puzzle Generator (Mate in 2 or 3)")

piece_map = {
    "Queen": chess.QUEEN,
    "Rook": chess.ROOK,
    "Bishop": chess.BISHOP,
    "Knight": chess.KNIGHT,
    "Pawn": chess.PAWN,
}

selected = st.multiselect(
    "Select at least 2 pieces to use for generating the puzzle:",
    options=list(piece_map.keys()),
)

fen_input = st.text_input("Enter FEN (leave blank for starting position):")
board = chess.Board(fen_input) if fen_input else chess.Board()

st.write("### Current Board:")
st.image(chess.svg.board(board=board, size=400), use_column_width=True)

if st.button("🔍 Find Mate Puzzle"):
    if len(selected) < 2:
        st.error("Please select at least 2 pieces.")
    else:
        selected_pieces = [piece_map[p] for p in selected]
        score, line = minimax(board, depth=6, alpha=-float('inf'), beta=float('inf'),
                              maximizing=True, selected_pieces=selected_pieces)

        if abs(score) >= 9999 and line:
            st.success("🎉 Found a forced mate!")
            st.write("Move sequence (SAN):")
            for i, move in enumerate(line, 1):
                st.write(f"{i}. {board.san(move)}")
                board.push(move)
            st.image(chess.svg.board(board=board, size=400), use_column_width=True)
        else:
            st.warning("No mate-in-2 or 3 found with selected pieces.")
