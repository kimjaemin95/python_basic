'''
함수 및 람다

함수 정의 방법
def 함수이름(파라미터):
    함수 내용
'''

# 예제1
def test_function():
    print(">>>테스트 함수가 실행 되었습니다.")

# 함수 실행 방법
test_function()


# 예제 2
def test_2_function(text):
    print(text)

# 매개변수 입력한 함수 실행하기
test_2_function('>>>이것이 매개 변수입니다.')

# 예제 3
def test_3_function(value):
    string_val = ">>>입력된 단어는 \'{}\' 입니다.".format(value)
    return string_val

test = test_3_function("딸기")
print(test)

# 예제 4
# *args 튜플로 출력 됨
def args_function(*args):
    # 가변 매개변수
    print(args)

args_function('a','b','c')
args_function(1,2,3)
args_function(1,'a',[1,2,3])
args_function(1,2,3,4,5,6,7)


# **kwargs  딕셔너리로 출력 됨
def kwargs_function(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key, value)

kwargs_function(name="kimjaemin",
                age=26,
                height=177)

print()

# 혼합
def complex_function(arg1, arg2, *args, **kwargs):
    print(arg1, arg2, args, kwargs)

complex_function(1,2)
complex_function(1,2, 'park', 'kim')
complex_function(1,2, 'park', 'kim', name='kim')
print()

# 예제 5
# 중첩함수(클로저)
def nested_function(num):
    def _in_function(num):
        print(num+1000)
    print('>>>',num)
    _in_function(num)
nested_function(123)

# 예제 6
# 힌트
def hint_function(x : int) -> list:
    return [x, x+1, x+2]

print(hint_function(1))








