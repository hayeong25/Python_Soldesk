# print() - 화면 출력

print("hello python!!") # 문자열은 큰따옴표, 작은따옴표 모두 가능
print('hello python!!')
print(100)
print("100")
print("25.3")
print(25)

# type() - 변수 타입
print(type(100)) # <class 'int'>
print(type("100")) # <class 'str'>
print(type(25.5)) # <class 'float'>
print(type(True)) # <class 'bool'>

# sep=' '이 default 값 => 여러 개 출력 시 띄어쓰기 한 후 출력됨
print('T', 'E', 'S', 'T') # T E S T
print('T', 'E', 'S', 'T', sep='') # TEST
print('2022', '05', '19', sep='-') # 2022-05-19
print('niceman', 'naver.com', sep='@') # niceman@naver.com

# end - 줄바꿈을 하지 않고 이전 문자열과 다음 문자열 연결해서 출력
print("파이썬은 ", end=' ')
print("쉬운 언어입니다.")