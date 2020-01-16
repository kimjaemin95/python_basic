'''
조건문, 반복문
코딩 테스트 문제
'''

# 1. 아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하세요.
q1 = fruit = {"봄": "딸기", "여름": "토마토", "가을": "사과"}
print(fruit["가을"])
for key in fruit.keys():
    if key =="가을":
        print(fruit[key])
        break

# 2. 아래 딕셔너리에서 '사과'가 포함되었는지 확인하세요.
q2 = fruit = {"봄": "딸기", "여름": "토마토", "가을": "사과"}
for val in fruit.values():
    if val == "사과":
        print("사과가 있습니다.")
        break

# 3. 다음 점수 구간에 맞게 학점을 출력하세요.
# 81 ~ 100 : A학점
# 61 ~ 80 :  B학점
# 41 ~ 60 :  C학점
# 21 ~ 40 :  D학점
#  0 ~ 20 :  E학점
score = 40
grade = ""

if score >= 81 :
    grade = "A"
elif score <= 80 and score >= 61:
    grade = "B"
elif score <= 60 and score >= 41:
    grade = "C"
elif score <= 40 and score >= 21:
    grade = "D"
else :
    grade = "E"

print(grade)


# 4. 다음 세 개의 숫자 중 가장 큰수를 출력하세요.(if문 사용) : 12, 6, 18
print(max([12,6,18]))


# 5. 다음 주민등록 번호에서 7자리 숫자를 사용해서 남자, 여자를 판별하세요. (1,3 : 남자, 2,4 : 여자)
s = '891022-2473837'
gender_data = s.split("-")[1]
gender = int(gender_data[0])
if gender in [1, 3]:
    print("남자입니다.")
elif gender in [2,4]:
    print("여자입니다.")

# 6 ~ 10 반복문 사용(while 또는 for)
# 6. 다음 리스트 중에서 '정' 글자를 제외하고 출력하세요.
q3 = ["갑", "을", "병", "정"]
for i in q3:
    if i == "정":
        continue
    else:
        print(i)

# 7. 1부터 100까지 자연수 중 '홀수'만 한 라인으로 출력 하세요.
for i in range(1,100,2):
    print(i,end=(","))

# 8. 아래 리스트 항목 중에서 5글자 이상의 단어만 출력하세요.
q4 = ["nice", "study", "python", "anaconda", "!"]
for text in q4:
    if len(text) >= 5:
        print(text)

# 9. 아래 리스트 항목 중에서 소문자만 출력하세요.
q5 = ["A", "b", "c", "D", "e", "F", "G", "h"]
for alp in q5:
    if alp == alp.lower():
        print(alp, end=(","))

# 10. 아래 리스트 항목 중에서 소문자는 대문자로 대문자는 소문자로 출력하세요.
q6 = ["A", "b", "c", "D", "e", "F", "G", "h"]
for q in q6:
    if q == q.upper():
        print(q.lower())
    else:
        print(q.upper())











