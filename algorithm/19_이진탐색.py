# 이진탐색 : 자료가 정렬된 상태여야 함

from turtle import right


def binary_search1(list1, num):
    # 시작 위치 지정
    start = 0

    # 종료 위치 지정
    end = len(list1) - 1

    # 반복문 - 시작 위치가 종료 위치보다 작거나 같을 때까지
    while start <= end:
        # 중간 위치 지정
        mid = (start + end) // 2

        # 찾고자 하는 숫자가 중간 위치의 숫자보다 작으면 start = 중간위치 + 1
        if num < list1[mid]:
            start = mid + 1

        # 찾고자 하는 숫자가 중간 위치의 숫자보다 크면 start = 중간위치 - 1
        elif num > list1[mid]:
            start = mid - 1

        # 둘 다 아닌 경우 중간 위치 return
        else:
            return mid


# 재귀호출 이진탐색
# 1. 중간 위치 지정
# 2. 찾는 값과 중간 위치 값이 같다면 중간 위치 값 return
# 3. 찾는 값이 중간 위치 값보다 크면 중간 위치의 오른쪽을 대상으로 이진 탐색 함수 재귀호출
# 4. 찾는 값이 중간 위치 값보다 작으면 중간 위치의 왼쪽을 대상으로 이진 탐색 함수 재귀호출
def binary_search2(list1, num, start, end):
    # 종료 조건 : 리스트가 빈 상태라면 탐색 종료
    if len(list1) <= 0:
        return

    # 중간 위치 지정
    mid = (start + end) // 2

    if num < list1[mid]:
        return binary_search2(list1, num, start, mid - 1)
    elif num > list1[mid]:
        return binary_search2(list1, num, mid + 1, end)
    else:
        return mid


if __name__ == "__main__":
    list1 = [1, 4, 9, 16, 25, 36, 49, 64, 81]
    print("36의 위치 :", binary_search1(list1, 36))
    print("49의 위치 :", binary_search2(list1, 49, 0, len(list1) - 1))
