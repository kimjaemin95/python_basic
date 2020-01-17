'''
파일 읽기, 쓰기
읽기 모드 : r
쓰기 모드(기존 파일 삭제) : w
추가 모드(파일 생성 또는 추가) : a
.. : 상대 경로
'''

# 파일 읽기
# 예제 1
f = open('./resource/review.txt', 'r')
content = f.read()
print(content)
print(dir(f))
# open 후 close로 리소스 반환
f.close()

print('\n\n')

# 예제 2
# with 으로 작성하면 자동으로 close 해줌
with open('./resource/review.txt', 'r') as f:
    content = f.read()
    print(content)
    print(list(content))

print('\n\n')

# 예제3
with open('./resource/review.txt', 'r') as f:
    for c in f:
        print(c.strip())    # strip() 양쪽 공백 제거 함수

print('\n\n')

# 예제4
with open('./resource/review.txt', 'r') as f:
    content = f.read()
    print(">>>",content)
    content = f.read()
    print(">>>",content) # 이미 read()를 해서 커서가 txt파일의 맨 끝으로 갔기 때문에 읽혀질 내용이 더 없다.

print('\n\n')

# 예제5
with open('./resource/review.txt', 'r') as f:
    line = f.readline()
    while line:
        print(line, end='>>>>')
        line = f.readline()

print('\n\n')

# 예제6
with open('./resource/review.txt', 'r') as f:
    contents = f.readlines()
    for c in contents:
        print(c, end='*****')

print('\n\n')

# 예제7
score = list()
with open('./resource/score.txt', 'r') as f:
    for line in f:
        print('>',line)
        score.append(int(line))
    print(score)

print('Average : {:6.3}'.format(sum(score)/len(score)))


# 파일 쓰기

# 예제1
with open('./resource/text1.txt','w') as f:
    f.write("Jaemin Handsome\n")

# 예제2
with open('./resource/text1.txt','a') as f:
    f.write("Jaemin Goodman\n")

# 예제3
from random import randint

with open('./resource/text2.txt', 'w') as f:
    for cnt in range(6):
        f.write(str(randint(1,50)))
        f.write('\n')

# 예제 4
# writelines : 리스트 -> 파일로 저장
with open('./resource/text3.txt', 'w') as f:
    list_ex = [ 'kim\n', 'park\n', 'boo\n', 'Lee\n', 'Jae\n']
    f.writelines(list_ex)

# 예제 5
with open('./resource/text4.txt', 'w') as f:
    print("test contents1 !!!", file=f)
    print("test contents2 !!!", file=f)




















