# 클래스 상속


class Parent:
    def __init__(self) -> None:
        self.value = "Test"
        print("Parent class의 __init__ 호출")

    def test(self):
        print("Parent class의 test() 호출")


class Child(Parent):
    def __init__(self) -> None:
        Parent.__init__(self)  # 부모 객체가 생성될 수 있도록 반드시 명시해야 함
        print("Child class의 __init__ 호출")


child = Child()
child.test()
print(child.value)

# Car
class Car:
    speed = 0

    def up_speed(self, value):
        self.speed += value

    def down_speed(self, value):
        self.speed -= value


class Sedan(Car):
    seatNum = 0

    def getSeatNum(self):
        return self.seatNum


class Truck(Car):
    capacity = 0

    def getCapacity(self):
        return self.capacity


sedan, truck = Sedan(), Truck()
sedan.up_speed(100)
truck.up_speed(70)
sedan.seatNum = 5
truck.capacity = 50
print("세단 속도는 {}km/h, 좌석 수는 {}개입니다".format(sedan.speed, sedan.getSeatNum()))
print("트럭 속도는 {}km/h, 총 중량은 {}톤입니다".format(truck.speed, truck.getCapacity()))


# Audio
class AudioVisual:
    def __init__(self, power, volume) -> None:
        self.power = power
        self.volume = volume

    def switch(self, on_off):
        self.power = on_off

    def set_volume(self, volume):
        self.volume = volume


class Audio(AudioVisual):
    def __init__(self, power, volume):
        super().__init__(power, volume)

    def tune(self):
        message = "La La La ..." if self.power else "전원을 켜주세요"
        print(message)


class TV(AudioVisual):
    def __init__(self, power, volume, size):
        super().__init__(power, volume)
        self.size = size

    def watch(self):
        message = "Have Fun !!" if self.power else "전원을 켜주세요"
        print(message)


tv = TV(False, 12, 55)
tv.switch(True)
tv.watch()

audio = Audio(True, 15)
audio.set_volume(9)
audio.tune()
