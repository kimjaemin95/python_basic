'''
람다식
람다식 : 메모리 절약, 가독성 향상, 코드 간결
함수는 객체 생성 -> 리소스(메모리) 할당
람다는 즉시 실행(heap초기화 -> 메모리 초기화
'''

# 일반적인 함수
def mul_10(num : int) -> int:
    return num * 10

print(mul_10(10))

# 람다 함수
lambda_mul_10 = lambda num : num * 10
print(lambda_mul_10(10))











