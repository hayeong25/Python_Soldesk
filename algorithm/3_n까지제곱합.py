# 복잡도 + 0(n)
# 1 ~ n까지 연속한 숫자의 제곱합 구하기
def double_a(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i * i
    return sum


# 공식 : n(n+1)(2n+1)/6
# 복잡도 : 0(1)
def double_b(n):
    return n * (n + 1) * (2 * n + 1) // 6


if __name__ == "__main__":
    print("1에서 10까지 제곱합 :", double_a(10))
    print("1에서 10까지 제곱합 :", double_b(10))
