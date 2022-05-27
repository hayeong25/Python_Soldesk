# Exception

# Compile Error
# 1. 문법 에러
print('Test)

# 2. NameError : 정의하지 않고 호출했을 경우
a, b = 10, 15
print(c) 

# Runtime Error
# 3. ZeroDivisionError : 0으로 나눌 때
print(10 / 0)

# IndexError : 배열 인덱스 범위 초과
x = [10, 20, 30]
print(x[3])

# KeyError : dictionary에서 존재하지 않는 key값 불러올 때
dict = {"name":"kim", "age":26, "city":"seoul"}
print(dict["address"])

# ValueError : list 안에 없는 인덱스를 불러올 때
x.index(40)

# FileNotFoundError : 파일이 존재하지 않을 때
f = open("data/111.txt", "r")

# TypeError : 서로 타입이 다른데 연결할 경우
x = [1, 2]
y = (1, 2)
print(x + y)

# 예외 처리
# 1. try ~ except : 오류 종류와 상관없이 오류 발생 시 except 블록 수행
# 2. try ~ except 에러명 : 해당 오류 발생 시 except 블록 수행
# 2. try ~ except Exception : 어떤 오류가 나는지 모를 때
# 3. try ~ except ~ else
# 4. try ~ except ~ finally
name = ["Kim", "Park", "Choi"]
try:
    z = "let"
    x = name.index(z)
    print("{} Found it! in name {}.".format(z, x+1))
except ValueError:
    print("Not Found")

try:
    z = "let"
    x = name.index(z)
    print("{} Found it! in name {}.".format(z, x+1))
except Exception:
    print("Not Found")


number = int(input("정수 입력 : "))
print("원의 반지름 :", number)
print("원의 둘레 :", 2 * 3.14 * number)
print("원의 넓이 :", 3.14 * number * number)

try:
    pass
except: # 예외 발생한 경우
    pass
else: # 예외가 발생하지 않은 경우에 실행 (except 바로 뒤에 위치해야 함)
    pass
finally: # 예외 발생 여부 상관없이 무조건 실행
    pass

try:
    f = open("data/info.txt", "r")
finally:
    f.close()