import streamlit as st
import chess
import chess.svg
from solver import find_forced_mate

st.set_page_config(page_title="♥️ AI Chess Puzzle Generator", layout="wide")
st.title("♥️ AI Chess Puzzle Generator (Mate in 2 or 3)")

piece_map = {
    "King": chess.KING,
    "Queen": chess.QUEEN,
    "Rook": chess.ROOK,
    "Bishop": chess.BISHOP,
    "Knight": chess.KNIGHT,
    "Pawn": chess.PAWN,
}

selected = st.multiselect(
    "Select at least 1 piece to use for generating the puzzle:",
    options=list(piece_map.keys()),
)

mate_depth = st.selectbox(
    "Mate in how many moves?",
    options=[2, 3],
    index=0
)

fen_input = st.text_input("Enter FEN (leave blank for starting position):")
board = chess.Board(fen_input) if fen_input else chess.Board()

st.write("### Current Board:")
st.image(chess.svg.board(board=board, size=400), use_container_width=True)

if st.button("🔍 Find Mate Puzzle"):
    if len(selected) < 1:
        st.error("Please select at least 1 piece.")
    else:
        selected_piece_types = [piece_map[p] for p in selected]
        result = find_forced_mate(board, mate_depth, selected_piece_types)
        if result:
            st.success(f"🎉 Found a forced mate in {mate_depth}!")
            st.write("Move sequence (SAN):")
            temp_board = board.copy()
            for i, move in enumerate(result, 1):
                st.write(f"{i}. {temp_board.san(move)}")
                temp_board.push(move)
            st.image(chess.svg.board(board=temp_board, size=400), use_container_width=True)
        else:
            st.warning(f"No forced mate in {mate_depth} found using only the selected pieces.")
