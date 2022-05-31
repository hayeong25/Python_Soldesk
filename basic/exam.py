# data/word.txt load 후 words 리스트에 넣고 단어들 섞기
# 섞은 단어들 중 하나를 뽑아 화면에 출력
# 출력된 단어를 보고 빨리 똑같이 타이핑 하는 프로그램

import random
import time
import sqlite3
from datetime import datetime

conn = sqlite3.connect("data/records.db", isolation_level=None)
cursor = conn.cursor()
# 테이블 생성
sql = """
    create table if not exists records (id integer primary key autoincrement, cnt integer, record text, regdate text)
"""
cursor.execute(sql)

words = []
with open("data/word.txt", "r") as f:
    for w in f:
        words.append(w.strip())
random.shuffle(words)
start = time.time()
x = 0
for w in range(5):
    word = input(words[w] + " : ")
    if words[w] != word:
        print("틀렸습니다")
    else:
        x += 1
end = time.time()
print("걸린 시간 : ", end - start)
print("점수 :", x)

# n = 1
# input("Ready? Press Enter Key")
# # 시작 시간
# start = time.time()  # 초 단위 return (1970-01-01 00:00:00 기준으로 지난 시간)
# # 정답 개수
# cnt = 0
# while n <= 5:
#     # 리스트 속의 단어 섞기
#     random.shuffle(words)
#     # 임의의 단어 추출
#     q = random.choice(words)
#     print()
#     print("Question #{}".format(n))
#     # 문제(단어) 보여주기
#     print(q)
#     # 사용자로부터 입력받기
#     x = input()
#     print("입력값 :", x)
#     # 사용자의 입력값과 문제가 일치하는지 확인 - 일치하면 pass 출력하고 정답 개수 추가 / 틀리면 wrong 출력
#     if q == x:
#         print("pass")
#         cnt += 1
#     else:
#         print("wrong")
#     n += 1
# # 종료 시간
# end = time.time()
# # 게임하는 데 걸린 시간 출력
# print("게임 시간 :", end - start)
# print("정답 개수 :", cnt)
# # 정답 개수가 4개 이상이면 합격
# if cnt >= 4:
#     print("합격!")
# else:
#     print("불합격...")

# DB에 기록 삽입
sql = """
    insert into records(cnt, record, regdate) values(?, ?, ?)
"""
cursor.execute(
    sql,
    (x, (end - start), datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
)
