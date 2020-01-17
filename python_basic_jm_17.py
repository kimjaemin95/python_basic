'''
모듈, 패키지
jm_pkg 디렉토리 안에 있는 fibonacci 파일을 불러와서 라이브러리로 사용하기

상대 경로
.. : 부모 디렉토리(하나 상위 디렉토리)
. : 현재 디렉토리
'''

# 사용1(클래스)
from jm_pkg.fibonacci import Fibonacci

Fibonacci.fib(300)
print("ex2 : ", Fibonacci.fib2(400))
print("ex3 : ", Fibonacci().title)

# 사용2(클래스)
# 전체 가져오기
from jm_pkg.fibonacci import *
Fibonacci.fib(800)

# 사용3(클래스) 엘리아스(Alias)
from jm_pkg.fibonacci import  Fibonacci as fb
print(">>>>")
fb.fib(1000)

# 사용4(함수)
import jm_pkg.calculator as cal

print("ex4 : ", cal.add(100, 200))
print("ex5 : ", cal.mul(100, 200))
print("ex6 : ", cal.min(100, 200))
print("ex7 : ", cal.div(100, 200))

# 사용5(함수)
from jm_pkg.calculator import mul
print("ex8 : ", mul(6,10))

# 사용6(함수)
import jm_pkg.prints as p

p.prt1()
p.prt2()

# 빌트인
import builtins
print(dir(builtins))





