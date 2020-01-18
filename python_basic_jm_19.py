'''
예외처리
'''

# 예외 종류
# 문법적으로 에러가 없지만, 코드 실행(런타임)프로세스에서 발생하는 예외 처리도 중요
# linter : 코드 스타일, 문법 체크

# 에러 종류 예

# SyntaxError : 잘못 된 문법
'''
for i in range(1,30)
    print(i)
'''

# NameError : 참조 변수 없음
'''
a = 10
b = 2
print(c)
'''

# ZeroDivisionError : 0나누기 에러
'''
print(10/0)
'''

# IndexError : 인덱스 범위 오버
'''
x = [10, 20, 30]
print(x[5])
'''

# KeyError
'''
dict_test = {'name':123, 'age':123, 'height':177}
print(dict_test['adress'])

print(dict_test.get['adress']) -> None반환
'''

# AttributeError : 모듈 , 클래스에 있는 잘못 된 속성 사용시에 발생
'''
import time
print(time.testtime_month())
'''
















