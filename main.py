import tkinter as tk
import chess
import chess.svg
import subprocess
import cairosvg
from PIL import Image, ImageTk
from tkinter import filedialog, messagebox
import threading

class ChessApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chess Game")
        # self.board = chess.Board()
        self.board = chess.Board("6k1/4K1p1/6Pp/5N1P/8/8/8/8 w - - 0 1")
        self.engine = None
        self.player_color = chess.WHITE
        self.engine_color = chess.BLACK
        self.engine_path = None

        self.create_ui()

    def create_ui(self):
        # Create buttons, canvas, and input for moves
        self.canvas = tk.Canvas(self.root, width=480, height=480)
        self.canvas.grid(row=0, column=0, columnspan=3)

        self.btn_stockfish = tk.Button(self.root, text="Stockfish", command=self.select_stockfish)
        self.btn_stockfish.grid(row=1, column=0)

        self.btn_leela = tk.Button(self.root, text="Leela Chess Zero", command=self.select_leela)
        self.btn_leela.grid(row=1, column=1)

        self.btn_start_game = tk.Button(self.root, text="Start Game", command=self.start_game)
        self.btn_start_game.grid(row=1, column=2)

        # Entry for move input
        self.move_entry = tk.Entry(self.root, width=10)
        self.move_entry.grid(row=2, column=0)

        self.btn_play_move = tk.Button(self.root, text="Play Move", command=self.play_move)
        self.btn_play_move.grid(row=2, column=1)

        self.update_board_svg()

    def select_stockfish(self):
        self.engine_path = filedialog.askopenfilename(title="Select Stockfish Executable")
        if self.engine_path:
            messagebox.showinfo("Engine Selected", "Stockfish selected!")

    def select_leela(self):
        self.engine_path = filedialog.askopenfilename(title="Select Leela Chess Zero Executable")
        if self.engine_path:
            messagebox.showinfo("Engine Selected", "Leela Chess Zero selected!")

    def start_game(self):
        if not self.engine_path:
            messagebox.showwarning("No Engine", "Please select a chess engine first!")
            return

        # Ask user to choose color
        color_choice = messagebox.askquestion("Color", "Do you want to play as white?")
        self.player_color = chess.WHITE if color_choice == "yes" else chess.BLACK
        self.engine_color = chess.BLACK if self.player_color == chess.WHITE else chess.WHITE

        self.engine = subprocess.Popen([self.engine_path], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

        # Start the game if the engine is black
        if self.engine_color == chess.WHITE:
            self.engine_move()

    def engine_move(self):
        if self.engine:
            self.engine.stdin.write(f"position fen {self.board.fen()}\n".encode())
            self.engine.stdin.write("go\n".encode())
            self.engine.stdin.flush()

            threading.Thread(target=self.get_engine_move).start()

    def get_engine_move(self):
        while True:
            line = self.engine.stdout.readline().decode().strip()
            if line.startswith("bestmove"):
                move = line.split()[1]
                if chess.Move.from_uci(move) in self.board.legal_moves:
                    self.board.push(chess.Move.from_uci(move))
                    self.update_board_svg()
                break

    def play_move(self):
        user_move = self.move_entry.get()
        if user_move:
            move = chess.Move.from_uci(user_move)
            if move in self.board.legal_moves:
                self.board.push(move)
                self.update_board_svg()

                # After player's move, it's the engine's turn
                if not self.board.is_game_over():
                    self.engine_move()
            else:
                messagebox.showerror("Invalid Move", "This move is not valid!")
            self.move_entry.delete(0, tk.END)  # Clear the entry after submission

    def update_board_svg(self):
        # Render board as SVG
        board_svg = chess.svg.board(self.board, size=480)
        cairosvg.svg2png(bytestring=board_svg, write_to="board.png")

        # Display board on tkinter canvas
        img = Image.open("board.png")
        img = ImageTk.PhotoImage(img)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=img)
        self.canvas.image = img

def main():
    root = tk.Tk()
    app = ChessApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
