'''
리스트, 튜플 사용법

리스트 : 순서 o, 중복o, 수정o, 삭제o
'''

list_1 = []
list_2 = list()
list_3 = ['a','b','c','d','e']
list_4 = [10,100,'kim','jun']
list_5 = [10,100,[1,2,3,4], [5,6,7,8,9]]


# 리스트 인덱싱
print(list_3[3])
print(list_4[-1])
print(list_5[2])
print()


# 리스트 슬라이싱
print(list_5[1:3])
print(list_3[2:-2])
print()

# 리스트 연산
print(list_3 + list_4)
print(list_3 * 3)
print(list_5 * 4)
print(list_3 + ['test', 'item'])
print()

# 리스트 요소 삭제, 수정
list_6 = [1,2,3,4,5,6,7,8,9]
list_6[0] = 10
print(list_6)
print()

list_7 = [1,2,3,4,5,6,7,8,9]
list_7[3:6] = [100, 120, [123,1234,66234]]
print(list_7)

list_8 = [1,2,3,4,5]
del list_8[3]   # 리스트 요소 인덱싱해서 삭제
print(list_8)
print()

list_9 = [1,2,3,4,5]
list_9.remove(3)    # 리스트 요소 직접 선택해서 삭제
print(list_9)
print()

# 리스트 함수
x = [1,2,3,4,5]
x.append('append item')
print(x)
x.reverse()
print(x)

y = [1,2,3,4,5]
y.insert(2,'2번 인덱스에 추가하세요')
print(y)

y.pop() # 리스트의 맨 마지막 요소를 없애는 함수 (last in first out)
print(y)
print()

z = [1,2,3,4,5]
z.append(['a','b'])

k = [1,2,3,4,5]
k.extend(['a','b'])
print(z)
print(k)    # extend와 append의 차이입니다.














