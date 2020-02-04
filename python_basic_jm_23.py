'''
데이터베이스 업데이트, 삭제
파이썬 데이터베이스 연동(SQLite3)
'''


import sqlite3

# DB파일 생성
conn = sqlite3.connect('D:/Python/python_basic/resource/database.db', isolation_level=None)

# Cursor 연결
cursor = conn.cursor()

# UPDATE(업데이트) 데이터 수정1
conn.execute("UPDATE users SET username = ? WHERE id = ?", ('수정됨','2'))

# UPDATE(업데이트) 데이터 수정2
conn.execute("UPDATE users SET username = :name WHERE id = :id", {"name":"goodman","id":5})

# UPDATE(업데이트) 데이터 수정3
conn.execute("UPDATE users SET username = '%s' WHERE id = '%s'" % ('BadKim', 1))

# 중간 데이터 확인 1
for user in conn.execute("SELECT * FROM users"):
    print(user)

# Row DELETE (데이터 삭제) 1
conn.execute("DELETE FROM users WHERE id = ? ",(2,))

# Row DELETE (데이터 삭제) 2
conn.execute("DELETE FROM users WHERE id = :id ",{"id":5})

# Row DELETE (데이터 삭제) 3
conn.execute("DELETE FROM users WHERE id = '%s' " % (4,))

# 중간 데이터 확인 2
for user in conn.execute("SELECT * FROM users"):
    print(user)

# 테이블 전체 데이터 삭제
print("users data delete : ", conn.execute("DELETE FROM users").rowcount, "rows")

# 연결 종료(해제)
conn.close()


'''
https://online.fastcampus.co.kr/courses/510383/lectures/10074685
'''
