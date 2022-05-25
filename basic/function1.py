# 함수 - 반복적으로 수행되는 부분을 함수로 작성. 단독 실행 가능
# def 함수명():
#   수행할 문장1
#   수행할 문장2


from ast import arg
from re import A


def hello():
    return "hello!!!"


print(hello())


def add(a, b):
    return a + b


result = add(3, 4)
print(result)

# 기본 파라미터
def print_n_times(value, n=2):  # n 값이 없으면 default는 2
    for i in range(n):
        print(value)


print_n_times("안녕하세요")
print_n_times("안녕하세요", 5)

# 초기화 시키고 싶은 변수는 뒤에 선언
def say_myself(name, old, man=True):
    print("이름은 %s입니다." % name)
    print("나이는 %d입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")


say_myself("김모씨", 26)
say_myself("양모씨", 28, False)


def sum_and_mul(a, b):
    return a + b, a * b  # 자바와 달리 파이썬은 tuple 형태로 return 2개 가능


print(sum_and_mul(4, 5))  # (9, 20)

add, mul = sum_and_mul(7, 6)
print(add, " ", mul)


def func_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return y1, y2, y3


print(func_mul(100))
y1, y2, y3 = func_mul(200)
print(y1, " ", y2, " ", y3)

# *args : 가변 파라미터(매개변수 개수가 정확하지 않을 때 사용)
# def add_many(*args):
#     print(type(args))  # tuple
#     print(args)
# add_many({"desert": "macaroon", "wine": "merlot"})
# add_many("35", "24", "15", "36")
# add_many([35, 24, 18, 17])
# add_many(1, 2, 3, 4, 5, 6)

# def add_many(*args):
#     result = 0
#     for i in args:
#         result += i
#     return result
# print("result =", add_many())
# print("result =", add_many(15, 63, 45, 356, 36, 9, 3))
# print("result =", add_many(27, 35, 56))
# print("result =", add_many(39, 48, 17, 16, 15))

# **kwargs : keyword args => 가변 파라미터를 dictionary 형태로 다룸 (default는 tuple)
# def args_func1(**kwargs):
#     print("kwargs :", kwargs)
#     for k in kwargs.keys():
#         print(k)
#     for k, v in kwargs.items():
#         print(k, v)
# args_func1(name="Kim")
# args_func1(name="Kim", name2="Park", active="Test")
# args_func1(name="Kim", age=10, title="Title")
# args_func1(name="Kim", age=25, addr="Seoul")

# def example_mul(arg1, arg2=5, *args, **kwargs):
#     print(arg1, arg2, args, kwargs)
# example_mul(10, 20)
# example_mul(10)
# example_mul(10, 20, "Park", "Kim", 10, 20)
# example_mul(10, 20, "Choi", age=25, name="Kim")

# a = 1
# def var_test(a):
#     a += 1 # a = 2
# a = var_test(a) # 2
# print(a) # 1 => 블록 범위 안에 있어야 a 값이 유효

# def var_test():
#     global a # global 변수로 지정하면 블록 밖에서도 사용 가능
#     a += 1
# var_test()
# print(a)

# === 실습 ===
# 2개의 매개변수와 연산자를 입력받아서 사칙연산을 수행하는 함수 four_rules 작성
def four_rules(n, m, op):
    if op == "+":
        print("%d + %d = %d" % (n, m, (n + m)))
    elif op == "-":
        print("%d - %d = %d" % (n, m, (n - m)))
    elif op == "*":
        print("%d x %d = %d" % (n, m, (n * m)))
    elif op == "/":
        print("%d ÷ %d = %d" % (n, m, (n / m)))


n, m, op = int(input("숫자, 숫자, 연산자를 입력하세요 : "))
four_rules(n, m, op)

# [[1, 2, 3], [4, 5, 6], [7, 8, 9]] 형태의 리스트를 받아 1차원 리스트 [1, 2, 3, 4, 5, 6, 7, 8, 9]로 반환
def flatten(data):
    output = []
    for item in data:
        if type(item) == list:
            output += flatten(item)
        else:
            output.append(item)
    return output


list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(flatten(list1))

# 로또 생성기
import random


def get_number():
    return random.randrange(1, 46)


# lotto 리스트에 6개 숫자가 다 채워질 때까지 get_number() 호출
lotto = []
while len(lotto) >= 6:
    i = get_number()
    if lotto.count(i) >= 1:
        pass
    else:
        lotto.append(i)
print("로또 번호 :", lotto)
