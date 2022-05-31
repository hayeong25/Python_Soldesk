import sqlite3

conn = sqlite3.connect("data/database.db")
cursor = conn.cursor()

# 수정
# id가 2번인 user 이름을 John으로 변경
sql = """
    update users set username = ? where id = ?
"""
cursor.execute(sql, ("John", 2))
conn.commit()

sql = """
    update users set username = :username where id = :id
"""
cursor.execute(sql, {"username": "kim", "id": 2})
conn.commit()

sql = """
    update users set username = %s where id = %s
"""
cursor.execute(sql % ("John", 2))
conn.commit()

# 삭제
cursor.execute("delete from users where id = ?", (2,))
cursor.execute("delete from users where id = :id", {"id": 3})
cursor.execute("delete from users where id = %d" % 4)

conn.commit()
