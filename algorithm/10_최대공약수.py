# 최대공약수 : 두 개 이상의 정수의 공약수 중에서 가장 큰 값

from unicodedata import name


def gcd(a, b):
    result = 0
    for i in range(1, min(a, b) + 1):
        if (a % i == 0) & (b % i == 0):
            result = i
    return result


if __name__ == "__main__":
    print(gcd(1, 5))
    print(gcd(3, 6))
    print(gcd(60, 24))
    print(gcd(81, 27))
