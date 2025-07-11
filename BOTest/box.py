import pygetwindow as gw
from PIL import ImageGrab
import pyautogui

def main():
    win = gw.getWindowsWithTitle("YouTube")
    if not win:
        return None
    win = win[0]
    win.restore()
    win.activate()
    win.resizeTo(650, 800)
    win.moveTo(620, 85)

    pyautogui.sleep(1)
    img = ImageGrab.grab(bbox=(win.left + 138, win.top + 219, win.right - 137, win.bottom - 206))

    pyautogui.moveTo(620, 85 + 219 , duration=1)
    pyautogui.click()

    return img

if __name__ == '__main__':
    main()

