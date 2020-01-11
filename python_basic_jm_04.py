'''
데이터 타입
참고 : 수치연산 함수 참고 주소

int : 정수
float : 실수
complex : 복소수
bool : 불린
str : 문자열(시퀀스)
list : 리스트(시퀀스)
tuple : 튜플(시퀀스)
set : 집합
dict : 사전

'''

val_str1 = "Kimjaemin"
val_bool = True
val_str2 = "Trueman"
val_float = 10.3
val_int = 92
val_dict ={
    "name" : "kim",
    "age" : "26"
}
val_list = [1,2,3,4,5]
val_tuple = (6,7,8)
val_set = {1,2,3,4,5}

print(type(val_str1))
print(type(val_bool))
print(type(val_str2))
print(type(val_float))
print(type(val_int))
print(type(val_dict))
print(type(val_list))
print(type(val_tuple))
print(type(val_set))


int_1 = 12
int_2 = 56
int_3 = 49
int_4 = 29

big_int_1 = 777777777777777777777777777777777
big_int_2 = 999999999999999999999999999999999

float_1 = 1.123
float_2 = 3.4812
float_3 = .453
float_4 = 5.

print(int_1 * int_3) # 곱하기
print(big_int_1 * big_int_2) # 곱하기
print(int_1**2) # 제곱
print(float_1 * float_3)
print(float_1 * int_3, type(float_1 * int_3)) # 실수와 정수 곱셈
print()

# 데이터 형 변환
a = 5.
b = 4
print(a+b, type(a+b))
print(int(a+b), type(int(a+b)))
print(complex(a+b), type(complex(a+b)))
print(int(True))
print(int(False))

# 단항 연산자
x = 100
x += 100
print(x)

y = 100
y *= 100
print(y)

# 절대값
print(abs(-4))


# 가장 가까운 정수
import math
print(math.ceil(5.1))   # 5.1보다 크면서 가장 작은 정수
print(math.floor(12.349))   # 12.349보다 작으면서 가장 큰 정수













