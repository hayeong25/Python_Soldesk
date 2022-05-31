# 1 ~ 10까지의 합 : 55
# 1 ~ 100까지의 합 : 5050


def sum_a(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum


# 공식 : n(n+1)/2
def sum_b(n):
    return n * (n + 1) // 2


# 재귀호출
def rec_sum(n):
    if n == 1:
        return 1
    else:
        return n + rec_sum(n)


if __name__ == "__main__":
    print("1 ~ 10까지의 합 :", sum_a(10))
    print("1 ~ 100까지의 합 :", sum_a(100))
    print("1 ~ 100까지의 합 :", sum_b(100))
    print("1 ~ 100까지의 합 :", rec_sum(100))
