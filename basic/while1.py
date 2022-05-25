# while : tab으로 같은 블럭임을 표시해야 함

# 1 ~ 10 출력하기
from re import I


i = 1 # 초기화
while i < 11: # 조건
    print(i, end=" ")
    i = i + 1 #증감

print()

# 1 ~ 100 짝수만 출력하기
i = 1
while i < 101:
    if i % 2 == 0:
        print(i, end=" ")
    i = i + 1

# 1 ~ 100 홀수만 출력하기
i = 1
while i < 101:
    if i % 2 != 0:
        print(i, end=" ")
    i = i + 1;

# 1 ~ 100 합계 구하기
sum, i = 0, 1
while i < 101:
    sum += i
    i += 1
print(sum)

# sum()
# range(시작숫자, 끝나는숫자, 증감)
# print(sum(range(1, 101)))

i, j = 1, 1
while i < 3:
    while j < 10:
        print("%d x %d = %d" % (i, j, i*j))
        j += 1
    j = 1
    i += 1
    print()