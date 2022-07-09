# 키보드 핸들링
import pyautogui as p

# 입력 : write()

# p.write("write")

# 메모장에 문자열 타이핑
# 현재 화면에 메모장 활성화 ( .getWindowsWithTitle(프로그램 Title)[index] :: 중복된 이름이 있을경우를 대비해 index 값 지정 )

notepad = p.getWindowsWithTitle("제목 없음")[0]
notepad.activate()
p.write("write")
p.write("pyautogui", interval=0.5)
# p.write("안녕하세요") # 한글 지원 X
p.write(
    ["h", "e", "l", "l", "o", "left", "left", "left", "right", "l", "o", "enter"],
    interval=0.25,
)

import pyperclip  # 클립 보드 -> 한글 처리

pyperclip.copy("안녕하세요")

# hotkey(조합키)
p.hotkey("ctrl", "v")
p.hotkey("ctrl", "a")
p.hotkey("ctrl", "shift", "esc")

# keyDown(), keyUp()
p.keyDown("shift")
p.press("4")
p.keyUp("shift")

p.press(["a", "b", "c"], 2)
