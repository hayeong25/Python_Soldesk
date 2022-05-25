# input() : java의 Scanner와 동일

# message = input("이름을 입력하세요 : ")
# print(message)

# num1 = int(input("num1 : "))
# num2 = int(input("num2 : "))
# print(num1 + num2) # 연산이 아닌 연결 => 입력값은 str type

# === 실습 ===
# 년 / 월 / 일 입력받은 후 10년 후 날짜 출력하기
input = input("년/월/일을 입력하세요 : ")
input = input.split("/")
year = int(input[0]) + 10
month = int(input[1])
day = int(input[2])
print("10년 후는 %d년 %02d월 %02d일입니다." % (year, month, day))