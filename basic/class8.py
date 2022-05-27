# 오버라이딩 : 부모 클래스의 메소드 재정의


class Parent:
    def func1(self):
        print("Parent function1()")

    def func2(self):
        print("Parent function2()")


class Child(Parent):
    def func1(self):
        print("Child function1()")

    def func3(self):
        print("Child function2()")


parent, child = Parent(), Child()
parent.func1()
child.func1()
parent.func2()
child.func2()
child.func3()


# Car
class Car:
    speed = 0

    def up_speed(self, value):
        self.speed += value
        print("(Parent)현재 속도 : {}".format(self.speed))

    def down_speed(self, value):
        self.speed -= value


class Sedan(Car):
    seatNum = 0

    def up_speed(self, value):
        self.speed += value
        # 현재 속도가 150 초과일 경우 현재 속도를 150으로 변경
        if self.speed > 150:
            self.speed = 150

    def getSeatNum(self):
        return self.seatNum


class Truck(Car):
    capacity = 0

    def getCapacity(self):
        return self.capacity


sedan, truck = Sedan(), Truck()
sedan.up_speed(200)
truck.up_speed(80)
sedan.seatNum = 5
truck.capacity = 50
print("세단 속도는 {}km/h, 좌석 수는 {}개입니다".format(sedan.speed, sedan.getSeatNum()))
print("트럭 속도는 {}km/h, 총 중량은 {}톤입니다".format(truck.speed, truck.getCapacity()))
