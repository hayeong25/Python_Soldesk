import sqlite3

conn = sqlite3.connect(
    "data/database.db",
    isolation_level=None
    # isolation_level=None 을 사용하지 않으면 강제로 commit 해 주어야 함
)

cursor = conn.cursor()

# 조회
sql = """
    select * from users
"""
cursor.execute(sql)

# fetchone(), fetchmany(), fetchall()
# print("1", cursor.fetchone())
# print("3", cursor.fetchmany(size=3))
# print("4", cursor.fetchall())
for row in cursor.fetchall():
    print("rows", row)

sql = """
    select * from users where id = ?
"""
cursor.execute(sql, (3,))
for row in cursor.fetchall():
    print("rows", row)

sql = """
    select * from users where id = %s
"""
param = 4
cursor.execute(sql % param)
for row in cursor.fetchall():
    print("rows", row)

sql = """
    select * from users where id = :id
"""
param = 4
cursor.execute(sql, {"id", 5})  # dictionary 형태
for row in cursor.fetchall():
    print("rows", row)

sql = """
    select * from users where id in (?, ?)
"""
param = (3, 6)  # 3번과 6번 조회
cursor.execute(sql, param)
for row in cursor.fetchall():
    print("rows", row)
