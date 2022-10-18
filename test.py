# -----------------------------------------------------------
# IMPORTS
# -----------------------------------------------------------

import chess
import chess.svg
import chess.engine
import random
import time

# -----------------------------------------------------------
# FUNCTIONS
# -----------------------------------------------------------

def render(board: chess.Board) -> str:
    """
    Print a chess board with special chess characters.
    Taken from github.com/thomasahle/sunfish/blob/master/fancy.py
    """
    board_string = list(str(board))
    uni_pieces = {
        "R": "♖",
        "N": "♘",
        "B": "♗",
        "Q": "♕",
        "K": "♔",
        "P": "♙",
        "r": "♜",
        "n": "♞",
        "b": "♝",
        "q": "♛",
        "k": "♚",
        "p": "♟",
        ".": "·",
    }
    for idx, char in enumerate(board_string):
        if char in uni_pieces:
            board_string[idx] = uni_pieces[char]

    ranks = ["1", "2", "3", "4", "5", "6", "7", "8"]
    display = []

    for rank in "".join(board_string).split("\n"):
        display.append(f"  {ranks.pop()} {rank}")

    # if board.turn == chess.BLACK:
    #     display.reverse()

    display.append("    a b c d e f g h")

    return "\n" + "\n".join(display)

def chess_svg(board):
    """
    Returns an SVG file of the current state of the chess board
    """
    
    svg = chess.svg.board(board, size=350)  
    return svg

def random_engine(board):
    moves = list(board.legal_moves)
    return str(random.choice(moves))

def stockfish_engine(stockfish_file_path):
    return chess.engine.SimpleEngine.popen_uci(stockfish_file_path)

# -----------------------------------------------------------
# MAIN
# -----------------------------------------------------------

if __name__ == "__main__":
    #Load board
    board = chess.Board()

    #Load file paths
    stockfish_exe_file = r"C:\Users\Jackson Bowes\OneDrive\Desktop\Chess\chessEngine\engines\stockfish_15_x64_avx2.exe"
    stockfish_mac_file = r"engines/stockfish"

    #Create engines
    stockfish1 = stockfish_engine(stockfish_mac_file)
    stockfish2 = stockfish_engine(stockfish_mac_file)

    #Play chess
    while not board.is_game_over():
        # Stockfish1 is black
        if board.turn == chess.BLACK:
            stockfish1_result = stockfish1.play(board, chess.engine.Limit(time=0.5))
            board.push(stockfish1_result.move)

        # Stockfish2 is white
        elif board.turn == chess.WHITE:
            stockfish2_result = stockfish2.play(board, chess.engine.Limit(time=0.5))
            board.push(stockfish2_result.move)      

        # # Random engine is white
        # elif board.turn == chess.WHITE:
        #     random_move = random_engine(board)
        #     board.push_san(random_move)

        time.sleep(1)
        print(render(board))

    #Print outcome
    win_result = board.outcome().winner
    if win_result == None:
        print("Draw")
    elif win_result == True:
        print("Winner is white")
    else:
        print("Winner is black")

    #Quit engines
    stockfish1.quit()
    stockfish2.quit()
