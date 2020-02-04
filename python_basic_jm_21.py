'''
파이썬 데이터베이스 연동(SQlite)
테이블 생성 및 삽입
'''


import sqlite3
import datetime


# 삽입 날짜 생성
now = datetime.datetime.now()
print('now : ',now)

nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print('nowDatetime : ',nowDatetime ,end='\n\n')

# sqlite3
print('sqlite3 version : ', sqlite3.version)
print('sqlite3 db engin version : ', sqlite3.sqlite_version)

# DB생성 & auto commit(commit은 저장 완료와 같은 의미), Rollback(되돌리기)
conn = sqlite3.connect('D:/Python/python_basic/resource/database.db', isolation_level=None)

# Curosr
cursor = conn.cursor()
print('cursor type : ',type(cursor), end='\n\n')

# 테이블 생성(Data Type : TEXT, NUMERIC, INTEGER, REAL, BLOB ...)
'''
CREATE TABLE IF NOT EXISTS users
users테이블을 생성하는데 없으면 생성하고 있으면 있는걸 사용하겠다는 뜻입니다.
권장 방법 입니다.
'''
cursor.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, e_mail text, phone text, website text, regdate text)")

# 데이터 삽입
cursor.execute("INSERT INTO users VALUES(1, 'KIMJAEMIN', 'todaybow@naver.com', '010-3309-7000', 'www.tigerai.net.cn', ?)", (nowDatetime,))
cursor.execute("INSERT INTO users(id, username, e_mail, phone, website, regdate) VALUES(?,?,?,?,?,?)", (2, 'ChoiHeeyeon', 'top2road@naver.com','010-9xxx-xxxx', 'www.naver.com', nowDatetime))

# Many 삽입(튜플, 리스트)
userList = (
    (3, 'Lee', 'duam@naver.com','010-9xxx-xxxx', 'www.naver.com', nowDatetime),
    (4, 'Park', 'hanmail@naver.com','010-9xxx-xxxx', 'www.daum.com', nowDatetime),
    (5, 'Joo', 'cake@naver.com','010-9xxx-xxxx', 'www.hanmail.com', nowDatetime),
)

cursor.executemany("INSERT INTO users(id, username, e_mail, phone, website, regdate) VALUES (?,?,?,?,?,?)", userList)

# 테이블 데이터 삭제
# conn.execute("DELETE FROM users")
# print("users db deleted : ", conn.execute("DELETE FROM users").rowcount)


# 커밋(Commit) : isolation_level = None 일경우 auto commit
# 커밋(Commit) : isolation_level = None 이 아닐 경우 conn.commit() 명령으로 종료해야합니다.

# 롤백
# conn.rollback()

# 접속 종료
conn.close()






