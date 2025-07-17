from stockfish import Stockfish
stockfish = Stockfish(path="D:\\Windows Programs\\stockfish\\stockfish-windows-x86-64-avx2.exe")

def get_next_move(current_status):
    stockfish.set_position(current_status)
    best_move = stockfish.get_best_move()
    return best_move
