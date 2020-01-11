# python basic jm 01
'''
print의 이해
'''

# 기본출력
print('Hellow python!')
print("Hellow python!")
print("""Hellow python!""")
print('''Hellow python!''')
print()


# Separator 옵션 사용
print('T','E','S','T')
print('T','E','S','T', sep='')
print()
print('jmkim','naver.com')
print('jmkim','naver.com',sep='@')


# end 옵션 사용
print('hi, my name')
print('is Jaemin Kim. What')
print('your name?')
print()
print('hi, my name',end=' ')
print('is Jaemin Kim. What',end=' ')
print('your name?',end=' ')


# format사용 [], {}, ()
print('{} and {}'.format('You', 'Me'))
print('{0} and {1} and {0}'.format('You', 'Me')) # 숫자 인덱싱
print('{a} and {b} and {c}'.format(a='Kim', b='Lee', c='Jung'))


# %s(문자), %d(정수), %f(실수)
print('%s is handsome and kindman' % ('Jaemin'))
print('My height is %dcm' % (177))
print('My weight is %fkg' % (68.3))

# %3d: 정수 3번째자리까지만 출력, %3.2f는 정수는 3번째짜리까지만 소수자리는 2번째 자리까지만 출력
print('integer: %3d, float: %3.2f' % (12345, 12345.1234))
print('integer:{0: 3d}, float:{1: 3.2f}'.format(12345, 12345.1234))
print('integer:{a: 3d}, float:{b: 3.2f}'.format(a=12345, b=12345.1234))


"""
참고 : Escape 코드

\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\r : 캐리지 리턴
\f : 폼 피드
\a : 벨 소리
\b : 백 스페이스
\000 : 널 문자
"""





















