# for - for 변수 in 범위

print(range(5))
print(list(range(5)))
print(list(range(1, 5)))
print(list(range(0, 10, 2)))
print(list(range(50, 1, -2)))

# 0 ~ 9 출력
for i in range(10):
    print(i, end=" ")
for i in range(1, 11):
    print(i, end=" ")

# 1 ~ 100 출력
for i in range(1, 101):
    print(i, end=" ")

# 1 ~ 100 사이의 홀수 출력
for i in range(1, 101, 2):
    print(i, end=" ")

# 1 ~ 100 합계 구하기
sum = 0
for i in range(1, 101):
    sum += i
print(sum)

# === 실습 ===
# 숫자 입력받고 1부터 입력받은 숫자까지의 합계 구하기
# number = int(input("숫자를 입력하세요 : "))
# sum = 0
# for i in range(1, number+1):
#     sum += i
# print("1부터 %d까지의 합은 %d입니다" % (number, sum))
# print("1 ~ {}까지의 합 : {}".format(number, sum(range(1 , number+1))))

# 문자열 출력
word = "DREAMS"
for s in word:
    print(s)

# 이중 for문
for i in range(3):
    for j in range(3):
        print(j, end=" ")
    print()

# 구구단 2 ~ 9단
for i in range(2, 10):
    for j in range(1, 10):
        print("%d x %d = %d" % (i, j, i*j), end="\t")
    print()

# break, continue
i = 1
while i <= 10:
    if i == 5:
        break
    print(i, end=" ")
    i += 1

i = 1
while i <= 10:
    i += 1
    if i % 2 == 1:
        continue
    print(i, end=" ")

# === 실습 ===
# 1 ~ 10 중 5 제외하고 출력
for i in range(1, 11):
    if i == 5:
        continue
    print(i, end=" ")