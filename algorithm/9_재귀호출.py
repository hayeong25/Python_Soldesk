# 재귀호출 : 함수 안에서 자기 자신을 부르는 것

# 잘못된 예제 => RecursionError : maximum recursion depth exceeded while calling a Python object
# 파이썬 재귀호출은 끝나는 지점이 반드시 있어야 함. 무한호출이면 중간에 강제로 끝냄
def hello():
    print("hello")
    hello()


def fact(n):
    # 기본 단계 - 끝나는 부분 명시
    if n == 1:
        return 1
    # 반복 단계
    else:
        return n * fact(n - 1)
