# if
# python은 if문 블록{} 사용 X / 들여쓰기 사용

if True:
    print("True")

a = 200
if a < 100:
    print("a는 100보다 작습니다.")
print("IF문에서 들여쓰기는 중요해!")

if 100 <= a <= 200:
    print("a는 100과 200 사이의 수입니다.")

# === 실습 === 
# 가장 큰 수 출력하기
a, b, c = 12, 6, 18
max = a
if max < b:
    max = b
if max < c:
    max = c
print("제일 큰 수는", max)

# if ~ else
if True:
    print("True")
else:
    print("False")

a = 55
if a < 100:
    print("a는 100보다 작다")
else:
    print("a는 100보다 크다")

score, grade = 90, "A"
if score >= 90 and grade == "A":
    print("합격")
else:
    print("불합격")

# === 실습 ===
# 숫자를 입력받아
number = int(input("숫자를 입력하세요 : "))
if number % 2 == 0:
    print("짝수입니다")
else:
    print("홀수입니다")

import datetime

now = datetime.datetime.now()
print("{}년 {}월 {}일 {}시 {}분, {}초".format(now.year, now.month, now.day, now.hour, now.minute,now.second))
if now.hour < 12:
    print("오전")
else:
    print("오후")

# 삼항 연산자
str = "안녕하세요" if True else "반갑습니다,"
print(str)

# 중첩 IF
a = 75
if a > 50:
    if a < 100:
        print("a는 50보다 크고 100보다 작다")
    else:
        print("a는 100보다 크다")
else:
    print("a는 50보다 작다")

# 다중 if : if ~ elif : else
num = 90
if num >= 90:
    print("등급 A", num)
elif num >= 80:
    print("등급 B", num)
elif num >= 70:
    print("등급 C", num)
elif num >= 60:
    print("등급 D", num)
elif num >= 50:
    print("등급 E", num)
else:
    print("등급 F", num)

age, height = 27, 180
if age >= 20:
    if height >= 170:
        print("A 지망 가능")
    elif height >= 160:
        print("B 지망 가능")
    else:
        print("지원 불가")
else:
    print("20세 이상 지원 가능")

# === 실습 ===
# 점수를 입력받고 학점 출력
score = int(input("점수를 입력하세요 : "))
if score > 80:
    print("A학점")
elif scroe > 60:
    print("B학점")
elif score > 40:
    print("C학점")
elif score > 20:
    print("D학점")
else:
    print("E학점")

# 숫자 2개와 연산자 입력받아 연산 후 결과 출력
num1 = int(input("숫자를 입력하세요 : "))
num2 = int(input("숫자를 입력하세요 : "))
op = input("+, -, /, *, //, %, ** 연산자를 입력하세요 : ")
if op == '+':
    print("%d + %d = %d" % (num1, num2, (num1+num2)))
elif op == '-':
    print("%d - %d = %d" % (num1, num2, (num1-num2)))
elif op == '*':
    print("%d * %d = %d" % (num1, num2, (num1*num2)))
elif op == '/':
    print("%d / %d = %f" % (num1, num2, (num1/num2)))
elif op == '%':
    print("%d % %d = %f" % (num1, num2, (num1%num2)))
elif op == '//':
    print("%d // %d = %d" % (num1, num2, (num1//num2)))
elif op == '**':
    print("%d ** %d = %d" % (num1, num2, (num1**num2)))
else:
    print("틀린 연산자입니다")
    print("틀렸어!! 틀렸다고!!!!!")