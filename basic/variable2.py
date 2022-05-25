# 변수 : 자바스크립트와 같이 타입 없음. 할당한 후에 타입이 생김
# str, int, float, bool

# 문자형 = "", ''
str1 = "Life is too short, You need Python"
str2 = 'Life is too short, You need Python'
str3 = """
    Life is too short, You need Python
"""
str4 = '''
    Life is too short, You need Python
'''
print(str1)
print(str2)
print(str3)
print(str4)

# +
head = "Python"
tail = " is fun"
print(head + tail)

# *
a = "python"
print(a * 2)

print("*" * 20)
print("My Program")
print("*" * 20)

# 문자열 인덱싱 - 왼쪽부터 0. 오른쪽은 -1
str1 = "Life is too short"
print("str1[3]", str1[3]) # e
print("str1[-3]", str1[-3]) # o

# 마지막 범위 숫자는 포함 X [0:4] => 0부터 3까지
print("str1[0:4]", str1[0:4]) # Life
print("str1[4:8]", str1[4:8]) #  is
print("str1[9:]", str1[9:]) # oo short
print("str1[:17]", str1[:17]) # Life is too short
print("str1[:-4]", str1[:-4]) # Life is too s

# === 실습 ===
str2 = "20220520Sunny"
# date 변수에 날짜만 담고 weather 변수에 날씨만 담기
date = str2[:8]
weather = str2[8:]
# date 변수에 있는 값을 2022-05-20으로 변경하고 2022-05-20 Sunny 출력
print(date[:4], date[4:6],  date[6:], sep="-", end=" ")
print(weather)

# len()
print("len() : 문자열 길이", len(str1))

# count()
print("count() : 문자열에 포함된 특정 문자의 수", str1.count('t'))
print("count() : 문자열에 포함된 특정 문자의 수 %d" % str1.count('t'))
print("count() : 문자열에 포함된 특정 문자의 수 {}".format(str1.count('t')))

# find('찾을문자', 시작위치) - 없을 경우 -1 반환
print("find() : 특정 문자가 시작되는 첫 위치 반환", str1.find('i'))
print("find() : 특정 문자가 시작되는 첫 위치 반환", str1.find('k'))
print("find() : 특정 문자가 시작되는 첫 위치 반환", str1.find('i', 4))

# index() - 찾는 문자가 없으면 에러
print("index() : 특정 문자가 시작되는 첫 위치 반환", str1.index('i'))
# print("index() : 특정 문자가 시작되는 첫 위치 반환", str1.index('k')) # ValueError : substring not found

# startswith(), endswith() - 대소문자 구분
print(str1.startswith("L")) # True
print(str1.startswith("l")) # False
print(str1.endswith("T")) # False
print(str1.endswith("t")) # True

# join() : 문자열 삽입
a = ","
print(a.join("abcde")) # a, b, c, d, e

# upper() / lower() : 대소문자 변경
a = "abcde"
print("upper() : 소문자를 대문자로 변경", a.upper())
a = "ABCDE"
print("lower() : 대문자를 소문자로 변경", a.lower())

# swapcase() : 대소문자를 상호 변환
a = "Python is Easy"
print("swapcase() : 대소문자 상호 변환", a.swapcase())

# title() : 첫 글자만 대문자로
print("python Is Easy.".title())

# ==
print("abc" == "ABC") # False

# strip(), lstrip(), rstrip() : 공백 제거
a = "   hi   "
print(a.lstrip()) # left 공백 제거
print(a.strip())
print(a.rstrip()) # right 공백 제거

# replace() :문자열 대체
print(str1.replace("Life", "Your leg"))

# split() : 문자열 나누기 - [] list 구조로 return
print(str1.split()) # ['Life', 'is', 'too', 'short']

a = "a:b:c:d"
print(a.split(":"))

# splitlines() : 줄바꿈을 기준으로 문자열 나누기
a = "하나\n둘\n셋"
print(a.splitlines()) # ['하나', '둘', '셋']

# 문자열 구성 파악
print("1234".isdigit())
print("abcd".isalpha())
print("abc123".isalnum())
print("abcd".islower())
print("ABCD".isupper())

# === 실습 ===
# http://naver.com에서 프로토콜 부분 & .com 제외하고 나머지 중 처음 세 자리 + 글자 개수 + 글자 내 e 문자 개수 + ! 출력해 비밀번호 만들기
url = "http://naver.com"
url = url.replace("http://", "")
url = url[:url.find('.')]
e_cnt = url.count('e')
password = url[:3] + str(len(url)) + str(e_cnt) + "!"
print(password) # 문자 + 숫자 연결 불가 => str(숫자)로 문자 변환