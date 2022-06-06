# 퀵 정렬 : 전체 정렬 하지 않고, 리스트에서 기준값을 정해 기준값을 기준으로 왼쪽집합, 오른쪽집합으로 분할하여 정렬
# 왼쪽집합에는 기준값보다 작은 요소들을 이동시키고, 큰 값은 오른쪽집합으로 이동시킴


def quick_sort(list1):
    # 리스트 크기 구하기
    size = len(list1)

    # 종료조건
    if size <= 1:
        return list1

    # 기준값 정하기 - 마지막 요소
    pivot = list1[-1]
    # 기준값보다 작은 요소 담기
    g1 = []

    # 기준값보다 큰 요소 담기
    g2 = []

    for i in range(0, size - 1):  # 마지막 값은 기준값이기 때문에 제외
        if list1[i] < pivot:
            g1.append(list1[i])
        else:
            g2.append(list1[i])
    return quick_sort(g1) + [pivot] + quick_sort(g2)


if __name__ == "__main__":
    list1 = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
    print(quick_sort(list1))
