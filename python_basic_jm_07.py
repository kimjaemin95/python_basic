'''
튜플 사용법

튜플 : 순서o, 중복o, 수정x, 삭제x
'''


# 튜플 선언
tuple_1 = ()
tuple_2 = (1,)
tuple_3 = (1,2,3,4)
tuple_4 = (1,2,3,(4,5,6),(7,8,9))

print(tuple_2)
print()

# 튜플 슬라이싱
print(tuple_3[:3])
print(tuple_4[4])
print()

# 튜플 연산
print(tuple_4 + tuple_2)
print(tuple_3 * 5)
print()

# 튜플 함수
tuple_5 = (5,2,1,3,4,5,5,5)
print(tuple_5)
print(3 in tuple_5)
print(tuple_5.count(5))






















