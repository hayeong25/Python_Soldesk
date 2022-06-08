import pyautogui as p

# 이미지 인식 - 파일명은 영문
# locateOnScreen() : 캡쳐한 이미지의 화면상 좌표 구하기
# 이미지 기반이라 해상도가 바뀌거나 하면 잘 안 됨
# screen_locate = p.locateOnScreen("./rpa/pyautogui1/screen.png")
# print(screen_locate)

screen_locate = p.locateOnScreen("./rpa/pyautogui1/file_menu.PNG")
# print(screen_locate)  # Box(left=39, top=0, width=50, height=40)
p.click(screen_locate)
