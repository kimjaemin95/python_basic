'''
반복문
for, while
'''

# while
val_1 = 1
while val_1 < 11:
    print("val_1 :", val_1)
    val_1 += 1

# for
for i in range(10):
    print(i)

for x in range(1,11):
    print(x)

# 1~100까지의 합
print(sum(range(1,101)))
print(sum(range(1,101,2)))

num = 1
sum_list = list()
while num <= 100:
    sum_list.append(num)
    num += 1
print(sum(sum_list))


# 시퀀스(순서가 있는)자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전 반복
# iterable : range, reversed, enumerate, filter, map, zip

name_list = ["kim", "park", "chil", "lee", "Nee", "Jae"]
for name in name_list:
    print(name)

text_1 = "abcdefghijk"
for alp in text_1:
    print(alp)

data_dict = {
    "name":"kimjaemin",
    "age":26,
    "height":177,
    "weight":70,
    "dream":100,
    "location":4885
}
for data in data_dict:
    print(data) # key만 출력

for key in data_dict.keys():
    print(key) # key만 출력

for value in data_dict.values():
    print(value)

for key, value in data_dict.items():
    print(key, value)

print("\n\n")

# 대문자 소문자 구분하기
text = "AbcdEjiJEIN"
for i in text:
    if i == i.upper():
        print(i)
    else:
        print(i.upper())
print()

# break
data_list = [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0]
for x in data_list:
    if x==1:
        print("1을 찾았습니다. for문을 종료하겠습니다.")
        break

# continue
data_list_2 = [1,2,5,3,4,65,3,5,76,8,3,5,7,3,5,1,2,3,4,5,7,9,0,4,3,45,6,7,8,5,3,45,6,2,3,4,2,3,4,5,1,2,3,4,6,3,4,2,2,2,2]
for i in data_list_2 :
    if i == 2:
        print("2를 찾았습니다. 2가 더 있는지 찾아보겠습니다.")
        continue
    else:
        print("이것은 2가 아닙니다.")

# for - else 구문
for a in range(10):
    print(a)
else:
    print("for문이 끝나고 a가 모두 출력 되었습니다.")





