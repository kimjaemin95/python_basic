'''
문자열, 문자열 연산
'''


#  문자열 길이 측정
str1 = "My name is Jaemin Kim"
str2 = "Handsome"
print(len(str1), len(str2))


# escape
escape_str1 = "나는 \"잘생겼다고\" 말했습니다."
print(escape_str1)
escape_str2 = "Tab\tTab\tTab"
print(escape_str2)


# Raw String
raw_str1 = r'C:\Programs\Test\Bin'
raw_str2 = r'\\a\\a'
print(raw_str1)
print(raw_str2)


# 멀티라인
val_multi = \
'''
이렇게
띄어서
써도 괜찮습니다.
그래도 에러가 없습니다.
'''
print(val_multi)


# 문자열 연산
print('-'*100)
for i in range(1,15):
    print('*'*i)


# 문자열 포함 여부 확인
val_text = 'abcdefg'
print('a' in val_text)
print('g' not in val_text)


# 형변환
val_str_int = '123'
print(val_str_int + 'string')   # 문자열 + 문자열
print(int(val_str_int) + 123 )  # 정수 + 정수


# replace 함수
replace_txt = 'This is test replace text'
print(replace_txt.replace("replace", "REPLACE"))


# split 함수
split_txt = 'This is test split text'
print(split_txt.split(" "))


# 문자열 슬라이싱
slicing_txt = 'abcdefghijklmnop'
print(slicing_txt[3:9])
print(slicing_txt[0:1])
print(slicing_txt[:9])
print(slicing_txt[-1])
print(slicing_txt[::2]) # 2번째거는 건너 뛰면서
print(slicing_txt[::-1])






















