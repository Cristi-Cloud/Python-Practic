import TicTacToe.CtrlScr
import TicTacToe.Algo

def tictactoe(rounds:int = 1):

    win = TicTacToe.CtrlScr.init_screen()
    if win:
        running = True
        while running:
            tabel = TicTacToe.CtrlScr.scan_screen(win)
            move = TicTacToe.Algo.nextmove(tabel)
            if move is not None:
                TicTacToe.CtrlScr.click_on_screen(move[0], move[1])
            else:
                rounds -= 1
                TicTacToe.CtrlScr.restart()

            if rounds == 0:
                running = False
    else:
        print("No Tac Tac Tac Tac Tac")

tictactoe(3)
