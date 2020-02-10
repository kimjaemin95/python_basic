'''
업그레이드 타이핑 게임 제작
타이핑 게임 제작 및 기본 완성
'''


import random
import time


words = [] # 영어 단어 리스트 (1000개 로드)

n = 1   # 게임 시도 횟수
cor_cnt = 0 # 정답 개수

with open('./resource/word.txt', 'r') as f :
    for c in f :
        words.append(c.strip()) # 양쪽 공백 제거 후 append

# print(words)

input("Ready? Press Enter Key!") # 사용자 입력을 대기하는 함수

start = time.time()

while n <= 5:
    random.shuffle(words)
    q = random.choice(words)
    print()

    print("*Qurestion # {}".format(n))  # 문제 번호 출력

    print(q)    # 문제 출력

    x = input() # 정답 입력

    print()

    if str(q).strip() == str(x).strip():
        print("Pass!")
        cor_cnt += 1
    else:
        print("Wrong!")

    n += 1

end = time.time() # 끝난 시점 시간 측정

run_time = end - start # 총 게임 시간
run_time_datetime = format(run_time, ".3f") # 소수 셋 째 자리 출력


if cor_cnt >= 3 :
    print("합격")
else :
    print("불합격")

print("게임 시간 : ", run_time_datetime, '초', "정답 새수 : {}".format(cor_cnt))


if __name__ == '__main__':
    pass














