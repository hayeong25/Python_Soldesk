# 선택정렬 : 정렬 알고리즘 중 가장 쉬운 방법 but 효율성이 좋지는 않음

# 이중 for문 사용 -특정 위치부터 최소값의 위치를 찾은 후 정렬을 원하는 자리와 교환
def selection_sort1(list1):
    for i in range(len(list1) - 1):
        min_idx = i
        for j in range(i + 1, len(list1)):
            if list1[min_idx] > list1[j]:
                min_idx = j
        list1[i], list1[min_idx] = list1[min_idx], list1[i]

    print("오름차순 :", list1)


def selection_sort2(list1):
    for i in range(len(list1) - 1):
        max_idx = i
        for j in range(i + 1, len(list1)):
            if list1[max_idx] < list1[j]:
                max_idx = j
        list1[i], list1[max_idx] = list1[max_idx], list1[i]

    print("내림차순 :", list1)


if __name__ == "__main__":
    list1 = [35, 9, 2, 85, 17]
    selection_sort1(list1)
    selection_sort2(list1)
