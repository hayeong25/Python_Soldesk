import pyautogui

# 마우스 좌표 가져오기 - position()
pos = pyautogui.position()
print(pos)  # Point(x=1769, y=65)
print(pos.x, ", ", pos.y)

# 마우스 이동
# moveTo(x, y, 시간) : 절대 좌표로 이동
pyautogui.moveTo(100, 100, duration=1)
pyautogui.moveTo(200, 200, duration=1)
pyautogui.moveTo(300, 300, duration=1)

# moveRel(x, y, 시간) : 상대 좌표로 이동
pyautogui.moveRel(100, 100, duration=0.5)
