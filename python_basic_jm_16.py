'''
클래스 상속, 다중 상속
'''


# 예제 1
# 상속 기본
# 슈퍼클래스 (부모클래스) 및 서브클래스(자식클래스) -> 자식은 모든 속성, 메소드를 사용 가능하다.

# 클래스 : 라면 / 속성 : 종류, 회사, 맛, 면 종류, 라면 이름 등... -> 부모클래스

class Car():
    '''Parent Class'''
    def __init__(self, car_type, color):
        self.car_type = car_type
        self.color = color

    def show(self):
        return 'Car Class "Show Method!"'


class BmwCar(Car):
    '''Sub Class'''
    def __init__(self, car_name, car_type, color):
        super().__init__(car_type, color)
        self.car_name = car_name

    def show_model(self) -> None:
        return "Your Car Name : %s" % self.car_name


class BenzCar(Car):
    '''Sub Class'''
    def __init__(self, car_name, car_type, color):
        super().__init__(car_type, color)
        self.car_name = car_name

    def show_model(self) -> None:
        return "Your Car Name : %s" % self.car_name

    # 오버라이딩 된 함수
    def show(self):
        print(super().show())
        return 'Car Info : %s %s %s ' % (self.car_name, self.car_type, self.color)



# 일반 사용
model1 = BmwCar('520d', 'sedan', 'blue')
print(model1.car_name)
print(model1.car_type)
print(model1.color)
print(model1.show())
print(model1.show_model())
print(model1.__dict__)
print()

# Method Overriding(오버라이딩)
model2 = BenzCar('e-class 320', 'suv', 'black')
print(model2.show())

print()

# Parent Method Call
model3 = BenzCar('S-class 350', 'sedan', 'gray')
print(model3.show())

# Inheritance Info (상속 정보 반환)
# class '__main__.BmwCar' <<<< class '__main__.Car' <<<< class 'object'
print(BmwCar.mro())

# 예제 2
# 다중 상속

class X(object):
    pass

class Y():
    pass

class Z():
    pass

class A(X, Y):
    pass

class B(Y, Z):
    pass

class M(B, A, Z):
    pass

print(M.mro())
print(A.mro())

















