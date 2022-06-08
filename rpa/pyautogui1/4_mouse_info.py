import pyautogui

pyautogui.mouseinfo()

for i in range(10):
    pyautogui.moveTo(100, 100)
    pyautogui.sleep(1)
