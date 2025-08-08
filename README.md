# Chess Puzzle Generator

This is a web-based chess puzzle generator where users can select chess pieces and provide a board position using FEN notation. The app then searches for forced mate-in-2 or mate-in-3 solutions and displays the solution with the move sequence on an interactive chessboard.

## Features

- Accepts any valid chess position via FEN notation.
- Allows selection of one or more chess pieces to focus the search.
- Automatically finds forced checkmates in 2 or 3 moves, if available.
- Displays the solving move sequence visually on a chessboard.

## Tech Stack

- Streamlit for the web interface.
- python-chess for board representation and move generation.
- Minimax algorithm with alpha-beta pruning for move search and mate detection.
- chess.svg for rendering the board.
<img width="3392" height="1943" alt="image" src="https://github.com/user-attachments/assets/566971dd-1bad-4b70-8adc-023bf8a17626" />



<img width="3395" height="1950" alt="image" src="https://github.com/user-attachments/assets/758a7656-56e8-431b-a787-973143eb870c" />



<img width="3393" height="1949" alt="image" src="https://github.com/user-attachments/assets/a3d1331b-d79e-41a0-86f0-4200f6ab28c5" />

