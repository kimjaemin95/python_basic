'''
파이썬 데이터베이스 연동 (SQlite)
테이블 조회
'''


import sqlite3

# DB파일 조회(없으면 새로 생성)
conn = sqlite3.connect('D:/Python/python_basic/resource/database.db')

# 커서 바인딩
cursor = conn.cursor()

# 데이터 조회
cursor.execute("SELECT * FROM users")

# 커서 위치가 변경
# 1개 로우 선택
# print('One-> \n', cursor.fetchone())

# 지정 로우 선택
# print('Three-> \n', cursor.fetchmany(size=3))

# 나머지 전체 로우 선택
# print('All-> \n', cursor.fetchall())

# 커서위치 초과 되어 데이터가 없음
# print('All-> \n', cursor.fetchall(), end='\n\n')

# 순회1
# rows = cursor.fetchall()
# for row in rows:
#     print('retrieve1 > ', row)

# 순회2
for row in cursor.fetchall():
    print('retrieve2 > ', row)

print()


# 순회3
for row in cursor.execute("SELECT * FROM users ORDER BY id desc"):
    print('retrieve3 > ', row)

print()

# WHERE Retrieve1
param1 = (3,)
cursor.execute("SELECT * FROM users WHERE id=?", param1)
print('param1 : ', cursor.fetchall())










