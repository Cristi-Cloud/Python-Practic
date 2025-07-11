from stockfish import Stockfish

stockfish = Stockfish(path="D:\\Windows Programs\\stockfish\\stockfish-windows-x86-64-avx2.exe")

stockfish.set_position([])

best_move = stockfish.get_best_move()
print("Cea mai bună mutare:", best_move)