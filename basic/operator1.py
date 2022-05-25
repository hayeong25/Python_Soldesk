# 연산자

# 산술 연산자 : +, -, *, /(실수), //(정수), %, **
a, b = 5, 3
print(a+b, a-b, a*b, a/b, a//b, a%b, a**b)

s1, s2, s3 = "100", "100.123", "9999999"
print(s1 + s2 + s3)
print(float(s1) + float(s2) + float(s3))
print(int(s1) + 1)

# 복합 대입 연산자 : +=, -=, *=, /=, //=, %=, **=
a = 10
a += 5
print("a", a)
a -= 5
print("a", a)
a *= 5
print("a", a)
a /= 5
print("a", a)
a //= 5
print("a", a)
a %= 5
print("a", a)
a **= 5
print("a", a)

# === 실습 ===
# 777,777원이 5만원권, 1만원권, 5천원권, 1천원권으로 몇 장인지 출력
money = 777777
m50000 = money / 50000
money %= 50000
m10000 = money / 10000
money %= 10000
m5000 = money / 5000
money %= 5000
m1000 = money / 1000
money %= 1000
print("50,000원 : %d장" % m50000)
print("10,000원 : %d장" % m10000)
print("5,000원 : %d장" % m5000)
print("1,000원 : %d장" % m1000)
print("나머지 돈 : %d" % money)

# 관계 연산자 : ==, !=, >, <, >=, <=
a, b = 10, 0
print(a==b, a!=b, a>b, a<b, a>=b, a<=b)

# 논리 연산자 : and, or, not
print(100 > 60 and 60 > 15)
print(100 > 60 or 60 < 15)
print(not 60 < 15)
print(not False)
print(not True)
# print(!Ture)

# 비트 연산자
print(10 & 7)
print(10 | 7)
print((100 > 60) & (60 > 15))