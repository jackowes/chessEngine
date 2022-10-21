import chess
import chess.svg
import chess.engine
import random
import time

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

def stockfish(board):
    stockfish_exe_file = r"C:\Users\Jackson Bowes\OneDrive\Desktop\Chess\chessEngine\engines\stockfish_15_x64_avx2.exe"
    engine = chess.engine.SimpleEngine.popen_uci()

if __name__ == "__main__":
    board = chess.Board()

    stockfish_exe_file = r"C:\Users\Jackson Bowes\OneDrive\Desktop\Chess\chessEngine\engines\stockfish_15_x64_avx2.exe"
    engine = chess.engine.SimpleEngine.popen_uci(stockfish_exe_file)

    while not board.is_game_over():
        # Stockfish is black
        if board.turn == chess.BLACK:
            result = engine.play(board, chess.engine.Limit(time=0.1))
            board.push(result.move)

        # Random engine is white
        elif board.turn == chess.WHITE:
            move = random_engine(board)
            board.push_san(move)

        

        #time.sleep(1)
        
        print(render(board))

    #convert winner to string
    if board.outcome().winner == False: winner = "Black"
    else: winner = "White"

    #Print outcome
    print("Winner is: {0}".format(winner))

    engine.quit()



