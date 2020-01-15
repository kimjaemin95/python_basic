'''
딕셔너리와 집합

딕셔너리 : 순서x, 중복x, 수정o, 삭제o
Key, Value
'''


# 딕셔너리 선언
dict_a = {
    'name':'kim',
    'age':24,
    'height':170
}
dict_b = {
    0:'zero',
    1:"one",
    2:"two"
}
dict_c = {
    "array":[1,2,3,4,5]
}

# 딕셔너리 추가
print(dict_a)
print(dict_b)
print(dict_c)
print()

# 딕셔너리 추가
dict_a["add_data"] = "추가 된 데이터입니다."

# 추가 된 데이터 확인
print(dict_a)

# keys, values, items
'''
dict = { key : values} <--- 이 한 쌍을 item이라 한다
'''
# keys
print(dict_a.keys())
list_a_keys = list(dict_a.keys())
print(list_a_keys)

# values
print(dict_a.values())
list_a_values = list(dict_a.values())
print(list_a_values)

# items
print(dict_a.items())
list_a_items = list(dict_a.items())
print(list_a_items)

# items for문
for key, value in list_a_items:
    print(key, value)

















