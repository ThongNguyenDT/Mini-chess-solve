import chess
import chess.engine
import time

# Initialize custom FEN (custom map). Here, we use the standard starting position for simplicity.
# Replace with your desired custom FEN.
custom_fen = "6k1/4K1p1/6Pp/5N1P/8/8/8/8 w - - 0 1"

# Load the board with the custom FEN.
board = chess.Board(custom_fen)

# Path to Stockfish executable
stockfish_path = "stockfish-windows-x86-64-avx2.exe"  # Replace with your Stockfish path

# Load the Stockfish engine.
engine_1 = chess.engine.SimpleEngine.popen_uci(stockfish_path)
engine_2 = chess.engine.SimpleEngine.popen_uci(stockfish_path)

# Choose color to track win (True for white, False for black)
chosen_color = True  # Change to False if you want to track black's win

# Set thinking time per move (in seconds)
time_limit = 1

# Function to log moves
def log_move(board, move, chosen_color):
    if board.is_checkmate():
        if board.turn != chosen_color:  # Check if the chosen color won
            print(f"{'White' if chosen_color else 'Black'} won!")
        else:
            print(f"{'Black' if chosen_color else 'White'} won!")
        return True
    return False

# Play two engines against each other
def play_chess(board, engine_1, engine_2, chosen_color):
    move_log = []

    # Play until the game is over
    while not board.is_game_over():
        # Determine which engine to play based on the turn
        if board.turn == chess.WHITE:
            result = engine_1.play(board, chess.engine.Limit(time=time_limit))
        else:
            result = engine_2.play(board, chess.engine.Limit(time=time_limit))

        move = result.move
        move_log.append(move)

        # Apply the move to the board
        board.push(move)

        # Log the move and check for a win
        if log_move(board, move, chosen_color):
            break

        # Avoid stalemate by adding conditions or using engine-specific configuration

    return move_log
    # return None

# Run the game
move_log = play_chess(board, engine_1, engine_2, chosen_color)

# Output the moves in standard algebraic notation
for i, move in enumerate(move_log):
    print(f"Move {i+1}: {move}")

# Quit the engines
engine_1.quit()
engine_2.quit()
