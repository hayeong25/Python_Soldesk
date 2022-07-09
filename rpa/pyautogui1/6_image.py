import pyautogui as p

# 이미지 인식 - 파일명은 영문
# confidence - default 1 / 신뢰도 100%이기 때문에 완전 정확하지 않으면 잘 못 찾음
# locateOnScreen() : 캡쳐한 이미지의 화면상 좌표 구하기
# 이미지 기반이라 해상도가 바뀌거나 하면 잘 안 됨
# screen_locate = p.locateOnScreen("./rpa/pyautogui1/screen.png")
# print(screen_locate)

screen_locate = p.locateOnScreen(
    "./rpa/pyautogui1/file_menu.PNG", confidence=0.9
)  # 신뢰도 90%
# print(screen_locate)  # Box(left=39, top=0, width=50, height=40)
p.click(screen_locate)

# locateAllOnScreen() :찾아야 하는 이미지가 여러 개 있는 경우
# locateAllOnScreen(path, confidence) : 찾는 이미지가 여러개 있는 경우
screen_locate = p.locateAllOnScreen("./rpa/pyautogui1/checkbox.png", confidence=0.9)

print(screen_locate)

for pos in screen_locate:
    # print(pos)
    p.click(pos, duration=1)

# 일정한 시간 만큼만 기다리기
import time, sys

timeout = 15

start = time.time()
file_menu = p.locateOnScreen("./rpa/pyautogui1/checkbox.png", confidence=0.9)
while file_menu is None:
    file_menu = p.locateOnScreen("./rpa/pyautogui1/checkbox.png", confidence=0.9)

    end = time.time()

    if end - start > timeout:
        print("시간 종료")
        sys.exit()
