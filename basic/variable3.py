# type() : 변수 타입 확인

a = 3.5
print(type(a)) # <class 'float'>

b = True
print(type(b)) # <class 'bool'>

c = 123
print(type(c)) # <class 'int'>

d = "123"
print(type(d)) # <class 'str'>

# 형변환 : str(), int(), float(), bool()
print(str(True), type(str(True)))
print(str(1), type(str(1)))
print(str(98.6), type(str(98.6)))

print(int(False), type(int(False)))
print(int(1), type(int(1)))
# print(int("98.6"), type(int("98.6"))) # ValueError : invalid literal for in() with base 10 : '98.6'

print(float(True), type(float(True)))
print(float("1"), type(float("1")))
print(float(98), type(float(98)))

print(bool(True), type(bool(True)))
print(bool("False"), type(bool("False"))) # True
print(bool(0), type(bool(0))) # False => 0만 False
print(bool(98), type(bool(98)))