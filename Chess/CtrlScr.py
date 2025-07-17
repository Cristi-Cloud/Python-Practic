from typing import Any
from unittest import case

from PIL import ImageGrab
import pygetwindow as gw
import pyautogui as autogui
import numpy as np
import cv2

def init_screen():
    win = gw.getWindowsWithTitle("Lucas Chess")

    if win:

        win = win[0]
        win.restore()
        win.activate()
        win.resizeTo(850, 950)
        win.moveTo(500, 50)

        return win

    else:
        print("Window not found")
        return None

def take_screenshot(win):
    autogui.sleep(1)
    img = ImageGrab.grab(bbox=(win.left, win.top, win.right, win.bottom))

    return img

def get_table(img: object) -> tuple[Any, str]:
    screenshot = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

    white_team = cv2.imread("Chess//tabla_white_team.png")
    black_team = cv2.imread("Chess//tabla_black_team.png")

    res1 = cv2.matchTemplate(screenshot, white_team, cv2.TM_CCOEFF_NORMED)
    res2 = cv2.matchTemplate(screenshot, black_team, cv2.TM_CCOEFF_NORMED)
    _, max_val1, _, top_left1 = cv2.minMaxLoc(res1)
    _, max_val2, _, top_left2 = cv2.minMaxLoc(res2)

    if max_val1 > max_val2:
        return top_left1, "white"
    else:
        return top_left2, "black"


def move_done(old, new):
    moves = []
    for row in range(8):
        for col in range(8):
            if old[row][col] != new[row][col]:
                moves.append((row, col))
    return moves

def get_table_status(img):
    piece = 94
    chessboard = [['' for _ in range(8)] for _ in range(8)]
    for row in range(8):
        for col in range(8):
            crop = img.crop((col * piece, row * piece, (col + 1) * piece, (row + 1) * piece))
            p = find_piece(crop)
            chessboard[row][col] = p

    return chessboard


def find_piece(piece):
    ok = False
    for row in range(94):
        for col in range(94):
            pixel = piece.getpixel((row, col))
            if pixel == (255, 255, 255) or pixel == (0, 0, 0):
                ok = True
                break
        if ok:
            break

    if ok == False:
        return '+'

    #alb_gol = cv2.imread("alb_gol.png")
    pion_alb = cv2.imread("Chess//pion_alb.png")
    cal_alb = cv2.imread("Chess//cal_alb.png")
    turn_alb = cv2.imread("Chess//turn_alb.png")
    nebun_alb = cv2.imread("Chess//nebun_alb.png")
    regina_alba = cv2.imread("Chess//regina_alba.png")
    rege_alb = cv2.imread("Chess//rege_alb.png")

    #negru_gol = cv2.imread("negru_gol.png")
    cal_negru = cv2.imread("Chess//cal_negru.png")
    nebun_negru = cv2.imread("Chess//nebun_negru.png")
    pion_negru = cv2.imread("Chess//pion_negru.png")
    rege_negru = cv2.imread("Chess//rege_negru.png")
    regina_neagra = cv2.imread("Chess//regina_neagra.png")
    turn_negru = cv2.imread("Chess//turn_negru.png")

    piece = cv2.cvtColor(np.array(piece), cv2.COLOR_RGB2BGR)

    templates = {
        #"alb_gol": alb_gol,
        "pion_alb": pion_alb,
        "cal_alb": cal_alb,
        "turn_alb": turn_alb,
        "nebun_alb": nebun_alb,
        "regina_alba": regina_alba,
        "rege_alb": rege_alb,
        #"negru_gol": negru_gol,
        "cal_negru": cal_negru,
        "nebun_negru": nebun_negru,
        "pion_negru": pion_negru,
        "rege_negru": rege_negru,
        "regina_neagra": regina_neagra,
        "turn_negru": turn_negru
    }

    scores = {}
    for name, template in templates.items():
        result = cv2.matchTemplate(piece, template, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, _ = cv2.minMaxLoc(result)
        scores[name] = max_val

    best_match = max(scores, key=scores.get)

    match best_match:
        case "pion_alb":
            return 'P'
        case "cal_alb":
            return 'C'
        case "turn_alb":
            return 'T'
        case "nebun_alb":
            return 'N'
        case "regina_alba":
            return 'R'
        case "rege_alb":
            return 'E'
        case "cal_negru":
            return 'c'
        case "nebun_negru":
            return 'n'
        case "pion_negru":
            return 'p'
        case "rege_negru":
            return 'e'
        case "regina_neagra":
            return 'r'
        case "turn_negru":
            return 't'

    return ''


def click_on_screen(x, y, i, j):

    autogui.moveTo(x + i * 94 + 45, y + j * 94 + 45, duration=1)
    autogui.click()

def make_a_move(board, x_coord, y_coord, cell):
    for row in range(8):
        for col in range(8):
            if board[row][col] == cell:
                click_on_screen(x_coord, y_coord, col, row)

def main():
    win = init_screen()
    img = take_screenshot(win)
    coord, team = get_table(img)

    x = win.left
    y = win.top

    width = win.width
    height = win.height

    print(f"Position: ({x}, {y})")
    print(f"Dimension: {width}x{height}")

    if team == "white":
        print("white_team")
    elif team == "black":
        print("black_team")

    img = take_screenshot(win)
    chessboard = get_table_status(img.crop((coord[0], coord[1], coord[0] + 752, coord[1] + 752)))

    for row in range(8):
        for col in range(8):
            print(chessboard[row][col], end=' ')
        print()

    white_board = [[f"{col}{row}" for col in "hgfedcba"] for row in range(1, 9)]
    black_board = [[f"{col}{row}" for col in "abcdefgh"] for row in range(8, 0, -1)]

    make_a_move(white_board, win.left + coord[0], win.top + coord[1], "g7")


if __name__ == "__main__":
    main()
