'''
파이썬 기본 인코딩
'''
import sys


# 파이썬 기본 인코딩
print(sys.stdin.encoding)
print(sys.stdout.encoding)


# 출력문
print('My name is JaeMin Kim')


# 변수 선언
jmkim = 'handsome'


# 변수 선언(한글 선언)
김재민 = '잘생김'
print(김재민)  # 한글 변수 선언은 권장하지 않습니다.


# 조건문
if jmkim == 'handsome':
    print('클럽 통과하세요')
else:
    print("클럽 빠꾸입니다.")


# 반복문
for i in range(1, 10):
    for j in range(1,10):
        print('%d * %d = ' % (i,j), i*j)


# 함수 선언
def test_fucntion():
    print("This is test function")

# 함수 사용
test_fucntion()


# 클래스
class Cookie:
    pass

# 객체 생성
cookie = Cookie()
print(id(cookie))
print(dir(cookie))



