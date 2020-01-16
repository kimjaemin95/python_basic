'''
조건문
'''

print(type(True))
print(type(False))


# 예1
if True:
    print("True")

# 관계연산자
# >, >=, <, <=, ==, !=
a = 10
b = 0
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print()

# 참/ 거짓 종류
# 참 : "내용", [내용], (내용), {내용}, 1
# 거짓 : "", [], {}, (), 0

data = "1"
if data:
    print(">>>>True")
else:
    print(">>>>Flase")


# 논리연산자
# and or not
a = 100
b = 60
c = 15

print('and : ', a > b and a < b)
print('or : ', a > b or a < b)
print(not False)
print(not True)
print()

# 산술, 관계, 논리 연산자
# 산술 > 관계 > 논리 순서로 적용 됨
print(5 + 10 > 0 and not 7 + 3 == 10)

# 다중 조건문
# 등급 정하기
score = 94
if score > 90:
    print("A등급입니다.")
elif score > 80:
    print("B등급입니다.")
elif score > 70:
    print("C등급입니다.")
elif score > 60:
    print("꽝")

# 중첩 조건문
age = 24
height = 160

if age > 20 :
    if height > 150:
        print("놀이기구 이용 가능합니다.")
    else:
        print("놀이기구 이용 불가능합니다.")
else :
    print("입장 불가능합니다. ")









