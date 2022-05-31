# 리스트 안에서 가장 큰 숫자 찾기


from operator import indexOf
from traceback import print_tb

# 복잡도 : 0(n)
def find_max1(list1):
    max = 0
    for l in list1:
        if max < l:
            max = l
    return max


# 가장 큰 값의 위치 번호 return
def find_max2(list1):
    idx = 0
    for i in range(1, len(list1)):
        if list1[idx] < list1[i]:
            idx = i
    return idx


if __name__ == "__main__":
    list1 = [17, 92, 18, 33, 58, 7, 33, 42]
    print("가장 큰 숫자 :", find_max1(list1))

if __name__ == "__main__":
    list1 = [17, 92, 18, 33, 58, 7, 33, 42]
    print("가장 큰 숫자 위치 :", find_max2(list1))
