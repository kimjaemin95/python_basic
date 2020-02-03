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

# ValueError : 참조 값이 없을 때 발생
'''
x = [ 1, 5, 7]
x.remove(10)
x.index(10) 
'''

# FileNotFoundError
'''
f = open('text.txt', 'r')  설정한 경로가 잘못 되었을 때
'''

# TypeError
'''
x = [1,2]
y = (1,2)
z = 'test'
print(x + y)
print(z + x)
'''

# 항상 예외가 발생하지 않을 것으로 가정하고 먼저 코딩을 합니다.
# 그 후 런타임 예외 발생 시 예외 처리 코딩을 권장합니다.(EAFP 코딩 스타일일

# 예외 처리 기본
# try : 에러가 발생할 가능성이 있는 코드 실행
# except : 에러명 1
# except : 에러명 2
# else : 에러가 발생하지 않았을 경우 실행
# finally : 항상 실행

# 예제1

name = ['kim', 'lee', 'park']

try :
    z = 'kim' # 'cho' 예외 발생
    x = name.index(z)
    print('{} Found it in name {}'.format(z, x+1))
except ValueError:
    print('Not found it! - Occurred ValueError')
else :
    print('ok else!')



# 예제2

name = ['kim', 'lee', 'park']

try :
    z = 'jina'
    x = name.index(z)
    print('{} Found it in name {}'.format(z, x+1))
except Exception as e:
    print(e)
    print('Not found it! - Occurred Error')
else :
    print('ok else!')
finally:
    '''
    외부 접속을 했을 경우 무조건적으로 close를 해야하므로 finally 사용하는 경우가 있다
    '''
    print('finally!!!')
    print()

# 예제3
# 예외 처리는 하지 않지만, 무조건 수행 되는 코딩 패턴

try :
    print("try")
finally :
    print("Ok finally!!!!!")


# 예제4
try :
    z = 'kim' # 'cho' 예외 발생
    x = name.index(z)
    print('{} Found it in name {}'.format(z, x+1))
except ValueError:
    print('Not found it! - Occurred ValueError')
except IndexError:
    print('Not found it! - Occurred IndexError')
except Exception:
    print('Not found it! - Occurred Exception')
else :
    print('ok else!')
finally:
    print('finally ok!!')


# 예제5
# 예외 발생 : raise
# raise 키워드로 예외 직접 발생

try :
    a = 'Kim'
    if a == 'Kim':
        print('Ok 허가!')
    else:
        raise ValueError
except ValueError:
    print('ValueError 발생')
except Exception as e:
    print(e)
else:
    print('OK!@!!')










