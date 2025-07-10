import pygetwindow as gw
from PIL import ImageGrab
import pyautogui

def init_screen():
    win = gw.getWindowsWithTitle("Tic-Tac-Toe")
    if not win:
        return None
    win = win[0]
    win.restore()
    win.activate()
    win.resizeTo(650, 800)
    win.moveTo(620, 85)

    return win


def scan_screen(win):
    pyautogui.sleep(1)
    img = ImageGrab.grab(bbox=(win.left + 138, win.top + 219, win.right - 137, win.bottom - 206))

    tabel = [[0 for i in range(3)] for j in range(3)]
    cell = 123 + 3
    xi, xj, oi, oj = 62, 62, 62, 25

    for i in range(3):
        for j in range(3):
            if img.getpixel((xi + cell * j, xj + cell * i)) == (255, 255, 255):
                tabel[i][j] = 'x'
            elif img.getpixel((oi + cell * j, oj + cell * i)) == (255, 255, 255):
                tabel[i][j] = 'o'
            else:
                tabel[i][j] = '-'

            print(f"{tabel[i][j]}", end=" ")
        print()
    print("----------")

    return tabel


def click_on_screen(i, j):
    if 0 <= i < 3 and 0 <= j < 3:
        cell = 123 + 3
        xi, xj = 62, 62
        pyautogui.moveTo(620 + 138 + xi + cell * j, 85 +  219 + xj + cell * i, duration=1)
        pyautogui.click()
    else:
        return

def restart():
    pyautogui.click()

def main():
    win = init_screen()

    x = win.left
    y = win.top

    width = win.width
    height = win.height

    print(f"Position: ({x}, {y})")
    print(f"Dimension: {width}x{height}")

    scan_screen(win)

    click_on_screen(2, 0)

if __name__ == '__main__':
    main()

