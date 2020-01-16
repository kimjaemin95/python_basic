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



