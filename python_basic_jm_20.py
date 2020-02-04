'''
Excel, CSV 읽기, 쓰기

CSV : MIME = text/csv
'''

import csv


# 예제1
with open('./resource/sample1.csv', 'r') as f :
    reader = csv.reader(f)

    next(reader)    # 한줄 스킵 # next()가 있고 없고의 차이를 for문에서 알 수 있습니다.

    print(reader)
    print(type(reader))
    print(dir(reader))
    print()

    for i in reader:
        print(i)

# 예제2
with open('./resource/sample2.csv', 'r') as f:
    reader = csv.reader(f, delimiter='|')   # '|'을 기준으로 스플릿?처리

    print(reader)
    print(type(reader))
    print(dir(reader))
    print()

    for i in reader:
        print(i)


# 예제3
with open('./resource/sample1.csv', 'r') as f:
    reader = csv.DictReader(f)  # 반복문으로 프린트했을 때 각 행마다 컬럼과 값이 딕셔너리 형태로 출력 됩니다.
    # for i in reader:
    #     print(i)

    for i in reader:
        for key, value in i.items():
            print(key, value)
            print('-'*50)


# 예제4
w = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]]
with open('./resource/sample3.csv', 'w') as f:
    wt = csv.writer(f)
    for value in w:
        wt.writerow(value)


# 예제5
w = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]]
with open('./resource/sample4.csv', 'w', newline='') as f:  # newline=''새로운 줄바꿈을 ''으로 하겠다라는 의미입니다.
    wt = csv.writer(f)
    for value in w:
        wt.writerow(value)


# 예제6   --> 결과가 예제 5과 같습니다.
with open('./resource/sample5.csv', 'w', newline='') as f:
    wt = csv.writer(f)
    wt.writerows(w)


# XSL, XLSX
# excel을 처리하는 라이브러리 : openpyxl, xlsxwriter, xlrd, xlwt, xlutils
# pandas를 주로 사용(openpyxl, xlrd)
# pip install xlrd
# pip install openpyxl
# pip install pandas

'''
https://online.fastcampus.co.kr/courses/510383/lectures/9729970
'''
















