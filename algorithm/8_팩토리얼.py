# 팩토리얼


def fact(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    print("3! =", fact(3))
    print("5! =", fact(5))
    print("10! =", fact(10))
