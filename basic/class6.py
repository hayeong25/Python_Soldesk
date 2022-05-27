# class FourCal 작성
# 숫자 2개, +, -, *, / 메소드 작성 (연산 결과 return)


class FourCal:
    def __init__(self, num1, num2) -> None:
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2

    def mul(self):
        return self.num1 * self.num2

    def div(self):
        return self.num1 / self.num2


num1, num2 = 10, 5
calc = FourCal(num1, num2)
print("{} + {} = {}".format(num1, num2, calc.add()))
print("{} - {} = {}".format(num1, num2, calc.sub()))
print("{} * {} = {}".format(num1, num2, calc.mul()))
print("{} / {} = {}".format(num1, num2, calc.div()))

# Audio 클래스
class Audio:
    power = False
    volume = 1

    def __init__(self, power, volume) -> None:
        self.power = power
        self.volume = volume

    def switch(self, on_off):
        if on_off == "on":
            self.power = True
        else:
            self.power = False

    def set_volume(self, volume):
        self.volume = volume

    def tune(self):
        if self.power == True:
            print("La La La ...")
        else:
            print("전원을 켜주세요")
