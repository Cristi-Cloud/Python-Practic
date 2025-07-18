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


import Chess.CtrlScr
import Chess.Algo

def chess():
    win = Chess.CtrlScr.init_screen()
    img = Chess.CtrlScr.take_screenshot(win)
    coord, team = Chess.CtrlScr.get_table(img)

    prime_chessboard = Chess.CtrlScr.get_table_status(img.crop((coord[0], coord[1], coord[0] + 752, coord[1] + 752)))
    #board = [[]]
    #black_board = [[f"{col}{row}" for col in "hgfedcba"] for row in range(1, 9)]
    board = [[f"{col}{row}" for col in "abcdefgh"] for row in range(8, 0, -1)]
    current_status = []

    move = Chess.Algo.get_next_move(current_status)
    current_status.append(move)
    part1 = move[:2]
    part2 = move[2:]
    Chess.CtrlScr.make_a_move(board, win.left + coord[0], win.top + coord[1], part1)
    Chess.CtrlScr.make_a_move(board, win.left + coord[0], win.top + coord[1], part2)
    img = Chess.CtrlScr.take_screenshot(win)
    prime_chessboard = Chess.CtrlScr.get_table_status(img.crop((coord[0], coord[1], coord[0] + 752, coord[1] + 752)))

    running = True
    while running:
        img = Chess.CtrlScr.take_screenshot(win)
        temp_chessboard = Chess.CtrlScr.get_table_status(img.crop((coord[0], coord[1], coord[0] + 752, coord[1] + 752)))
        moves = Chess.CtrlScr.move_done(prime_chessboard, temp_chessboard)
        if moves == []:
            continue
        else:
            movement = ''
            for move in moves:
                print(board[move[0]][move[1]])
                movement += board[move[0]][move[1]]
            current_status.append(movement)
            print(current_status)
            move = Chess.Algo.get_next_move(current_status)
            current_status.append(move)
            if move is None:
                running = False
            else:
                part1 = move[:2]
                part2 = move[2:]
                Chess.CtrlScr.make_a_move(board, win.left + coord[0], win.top + coord[1], part1)
                Chess.CtrlScr.make_a_move(board, win.left + coord[0], win.top + coord[1], part2)
                img = Chess.CtrlScr.take_screenshot(win)
                prime_chessboard = (
                    Chess.CtrlScr.get_table_status(
                    img.crop((coord[0], coord[1], coord[0] + 752, coord[1] + 752))))

    return

if __name__ == '__main__':
    print("\n     !!! WELCOME to the BOTMASTER !!! \n")
    print("Choose your game: ")
    print(" 1) TicTacToe")
    print(" 2) Chess")

    game = int(input("\nYour choice (1 or 2): "))

    if game == 1:
        tictactoe(3)
    elif game == 2:
        chess()
    else:
        print("\n->Invalid input")
