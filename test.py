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

def create_engine(engine_file_path):
    return chess.engine.SimpleEngine.popen_uci(engine_file_path)

# -----------------------------------------------------------
# MAIN
# -----------------------------------------------------------

if __name__ == "__main__":
    #Load board
    board = chess.Board()

    #Load file paths
    stockfish_exe_file = r".\engines\stockfish_15_x64_avx2.exe"
    stockfish_mac_file = r"engines/stockfish"
    komodo_mac_file = r"engines/komodo.02-64-osx"
    komodo_exe_file = r".\engines\komodo-13.02-64bit.exe"
    lc0_mac_file = r"engines/lc0"

    #Create engines
    white_engine = create_engine(stockfish_exe_file)
    black_engine = create_engine(komodo_exe_file)

    #Play chess
    while not board.is_game_over():
        if board.turn == chess.WHITE:
            white_engine_result = white_engine.play(board, chess.engine.Limit(time=0.5))
            board.push(white_engine_result.move)  

        elif board.turn == chess.BLACK:
            black_engine_result = black_engine.play(board, chess.engine.Limit(time=0.5))
            board.push(black_engine_result.move)

        # # Random engine is white
        # elif board.turn == chess.WHITE:
        #     random_move = random_engine(board)
        #     board.push_san(random_move)

        time.sleep(0.5)
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
    white_engine.quit()
    black_engine.quit()
