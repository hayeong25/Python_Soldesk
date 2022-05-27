# 사용자가 정의한 모듈 실습

import prints

prints.prt1()
prints.prt2()

import mod1

prints(mod1.sum(15, 25))
prints(mod1.safe_sum(15, "25"))

from prints import prt1

prt1()

import calc  # from calc import FourCal

num1, num2 = 10, 5
# four = FourCal(num1, num2) => Error : FourCal() is not defined
four = calc.FourCal(num1, num2)
print("{} + {} = {}".format(num1, num2, four.add()))
print("{} - {} = {}".format(num1, num2, four.sub()))
print("{} * {} = {}".format(num1, num2, four.mul()))
print("{} / {} = {}".format(num1, num2, four.div()))
