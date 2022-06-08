import pyautogui

# 마우스 액션
# click(), doubleclick(), drag and drop(), scroll()

# click() : 현재 위치에서 클릭
pyautogui.click()

# click(x, y) : 좌표 (x, y)에서 클릭
pyautogui.sleep(3)  # 3초 정지
print(pyautogui.position())  # File 클릭할 위치 좌표 알아내기
pyautogui.click(60, 20, duration=0.5)

# click(clicks=n) : n=2인 경우 더블클릭
pyautogui.click(clicks=5)

# 2초 간격으로 우클릭 2번
pyautogui.click(clicks=2, interval=2, button="right")

# 더블클릭
pyautogui.doubleClick(x=60, y=20)

# mouseDown() / mouseUp()
pyautogui.moveTo(200, 200)
pyautogui.mouseDown()
pyautogui.moveTo(300, 300)
pyautogui.mouseUp()

# drag(x, y) : 절대 좌표
pyautogui.drag(100, 0, duration=0.5)

# dragTo(x, y) : 상대 좌표
pyautogui.dragTo(x=885, y=389)

# scroll(값) : 값이 음수면 아래로, 양수면 위로 스크롤
pyautogui.scroll(-1000)
