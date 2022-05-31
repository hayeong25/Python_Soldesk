# DB 연동
# 파이썬에는 내장 DB가 있음

import sqlite3

from datetime import datetime

# print(sqlite3.version)
# print(sqlite3.sqlite_version)

# 날짜 생성
now = datetime.now()
# print("now", now)
now_date_time = now.strftime("%Y-%m-%d %H:%M:%S")
# print("now_date_time", now_date_time)

conn = sqlite3.connect("data/database.db", isolation_level=None)

# 커서
cursor = conn.cursor()
print(type(cursor))  # <class 'sqlite3.Cursor'>

# 테이블 생성
cursor.execute(
    "CREATE TABLE IF NOT EXISTS users(id integer primary key, username text, phone text, website text, regdate text)"
)

# insert - 하나씩 삽입
cursor.execute(
    "INSERT INTO users VALUES(1, 'Kim', '010-1234-1234', 'kim.com', ?)",
    (now_date_time,),
)
cursor.execute(
    "INSERT INTO users VALUES(?, ?, ?, ?, ?)",
    (2, "Park", "010-1234-1234", "park.com", now_date_time),
)

# 여러 개를 한 번에 삽입
user_list = (
    (3, "Choi", "010-1234-1234", "choi.com", now_date_time),
    (4, "Lee", "010-1234-1234", "lee.com", now_date_time),
    (5, "Yang", "010-1234-1234", "yang.com", now_date_time),
)
cursor.executemany("INSERT INTO users VALUES(?, ?, ?, ?, ?)", user_list)

conn.commit()
