# 모듈 : 함수나 변수 또는 클래스들을 모아놓은 파일

import sys
import math
import random
import time

print(sys.builtin_module_names)

print(dir(math))

print(random.random())  # 0 ~ 1 사이의 실수

print(random.uniform(10, 20))  # 지정한 범위 사이의 임의의 수

# randrange(max) : 0 ~ max 사이의 임의의 수
# randrange(min, max) : min ~ max 사이의 임의의 수
print(random.randrange(10))

# choice(list) : list 요소 중 임의의 수
print(random.choice([1, 2, 3, 4, 5, 6, 7]))

# shuffle(list) : list 요소 섞기
list1 = [1, 2, 3, 4, 5, 6, 7]
print(random.shuffle(list1))

# sample(list, 숫자) : list 요소 중 숫자만큼 추출
print(random.sample([1, 2, 3, 4, 5, 6, 7], k=2))

print("지금부터 5초간 정지")
time.sleep(5)
print("프로그램 종료")
