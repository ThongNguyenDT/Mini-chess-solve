# ♟️ Chess Solver and Engine Competition 🎮

This repository contains two Python scripts, each designed to enhance your chess experience:
- **`solve_chess.py`**: 🧠 A chess puzzle solver.
- **`main.py`**: ⚔️ A chess engine competition manager.

## 🌟 Features
### `solve_chess.py`
- 📜 Loads chess positions from a file and calculates the best move(s) using the **Stockfish** chess engine.
- ♟️ Handles chess positions in [FEN](https://en.wikipedia.org/wiki/Forsyth%E2%80%93Edwards_Notation) format.
- ⏱️ Configurable engine time limit for calculating the best move.

### `main.py`
- 🤖 Facilitates chess matches between engines (e.g., Stockfish) or between a player and an engine.
- 🎲 Supports different engines for AI-vs-AI matches.
- 🎨 Customizable player color and engine settings.
- 📝 Logs game moves, determines the winner, and tracks performance.

## 🚀 Getting Started

### Prerequisites
1. Install the `python-chess` library for chess logic handling:
   ```bash
   pip install python-chess
    ```
2. Download and install the Stockfish engine (or any other chess engine you wish to use).
- You can download Stockfish from here.

3. Adjust the path to the Stockfish executable in the code:
     ```python
    stockfish_path = "/path/to/stockfish"
    ```
### 💻 Running the Scripts
###### Solve Chess Puzzles with `solve_chess.py`
1. Adjust the chess positions in FEN format (one per line) like:
    ```python
   # Initialize custom FEN (custom map). Here, we use the standard starting position for simplicity.
   # Replace with your desired custom FEN.
    custom_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
   ```
2. Run the script:
    ```bash
   python solve_chess.py
   ```
    This will output the best moves for each position provided.
###### Chess Engine Competition with `main.py`
1. You can configure `main.py` to run two engines against each other or a player vs engine.
2. Run the script:
   ```bash
   python main.py
   ```
## 🛠️ Example Usage

*Sample usage and output examples will be added soon.*

## 📂 File Descriptions

### `solve_chess.py`
This script is designed to solve chess puzzles by reading chess positions from a file in FEN format and determining the best move using the Stockfish engine.

- **Input**: A text file containing chess positions in FEN format (one position per line).
- **Output**: The best move for each position as computed by the Stockfish engine.

### `main.py`
This script runs chess matches either between two engines or between a human player and an engine, logging all moves and determining the winner.

- **Modes**:
  - 🆚 **Engine vs Engine**: Two engines play against each other.
  - 👤🆚🤖 **Player vs Engine**: A human player competes against an AI chess engine.

## 🔧 Customization

- Adjust the FEN positions in `solve_chess.py` to solve custom chess puzzles.
- In `main.py`, you can modify engine paths, player color, time limits, and other parameters to tailor the match setup.

## 🧑‍💻 Requirements

- Python 3.x
- `python-chess` library
- **Stockfish** or another UCI-compatible chess engine

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

🤖 **Explanation**:

- **`solve_chess.py`** is used to solve chess puzzles based on positions you provide.
- **`main.py`** lets you simulate chess matches between engines or between a player and an engine.
- The README outlines how to set up, customize, and use these scripts.

🎯 *Happy coding and chess playing!*
