'''
집합
집합 : Set() --> 순서x ,중복x
'''

a = set()
b = set([1,2,3,4])
c = set([1,4,5,5,5,5,6])

print(type(a))
print(c) # 중복 허용이 되지 않음

s1 = set([1,2,3,4,5,6,7,8,9,10])
s2 = set([1,3,5,7,9])
# 교집합
print(s1.intersection(s2))
print(s1 & s2)
print()

# 합집합
print(s1.union(s2))
print(s1 | s2)
print()

# 차집합
print(s1.difference(s2))
print(s1 - s2)
print('공집합',s2 - s1)

s3 = set([1,2,3,4,5,6])
# 추가
s3.add("추가 된 데이터")
print(s3)
print()

# 제거
s3.remove(1)
print(s3)


'''
2020년 01월 15일 수요일
https://online.fastcampus.co.kr/courses/510383/lectures/9729949
할 차례
'''






