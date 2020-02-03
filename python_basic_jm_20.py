'''
Excel, CSV 읽기, 쓰기

CSV : MIME = text/csv
'''
import csv

# 예제1
with open('./resource/sample1.csv', 'r') as f :
    reader = csv.reader(f)

    #next() -> 1행 스킵
    next(reader)

    # 확인
    print(reader)
    print(type(reader))
    print(dir(reader))
    print()

    for i in reader:
        print(i)
print()


# 예제2
with open('./resource/sample2.csv', 'r') as f :
    reader = csv.reader(f, delimiter="|")  # 구분 문자 입력

    #next() -> 1행 스킵
    # next(reader)

    # 확인
    print(reader)
    print(type(reader))
    print(dir(reader))
    print()

    for i in reader:
        print(i)
    print()


# 예제3
with open('./resource/sample1.csv', 'r') as f :
    reader = csv.DictReader(f)

    # for c in reader:
    #     print(c)

    for c in reader:
        for key, value in c.items():
            print(key, value)
        print('-'*20)


# 예제4
w = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]]
with open('./resource/sample3.csv', 'w') as f:
    wt = csv.writer(f)

    for v in w:
        wt.writerow(v)

'''

https://online.fastcampus.co.kr/courses/510383/lectures/9729969

'''





