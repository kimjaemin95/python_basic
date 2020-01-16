'''
클래스
클래스, 인스턴스 차이 중요
네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
클래스 변수 : 직접 사용 가능, 객체 보다 먼저 생성
인스턴스 변수 : 객체마다 별도로 존재, 인스턴스 생성 후 사용
'''
class UserInfo:
    # 속성, 메소드로 구성 되어있음
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def user_info_p(self):
        print("Name : ", self.name)
        print("age : ", self.age)
        print("height : ", self.height)
        print("weight : ", self.weight)


user_1 = UserInfo('Kim',23,177, 55)
user_1.user_info_p()
print(user_1.__dict__)
print('-'*70)
user_2 = UserInfo('Park',23,180, 65)
user_2.user_info_p()
print(user_2.__dict__)


print(id(user_1))
print(id(user_2))
print(id(user_1)==id(user_2))
print('\n\n')

# 예제 2
# 클래스 변수
class WareHouse:
    stock_num = 0
    def __init__(self, name):
        self.name = name
        WareHouse.stock_num += 1
    def __del__(self):
        WareHouse.stock_num -= 1

user1 = WareHouse("Kim")
user2 = WareHouse("Lee")
user3 = WareHouse("Park")


print(WareHouse.__dict__["stock_num"])  # 클래스 변수
print(user1.stock_num)
del user1
print(user2.stock_num)


'''
여기서 부터 듣기
https://online.fastcampus.co.kr/courses/510383/lectures/9729961
'''




