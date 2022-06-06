# 병합정렬 : 분해, 병합


def merge_sort1(list1):
    # 종료조건
    if len(list1) <= 1:
        return list1

    # 분해작업
    mid = len(list1) // 2  # 중간 값 구하기
    g1 = merge_sort1(list1[:mid])
    g2 = merge_sort1(list1[mid:])

    # 병합
    result = []
    while g1 and g2:  # 두 그룹에 자료가 남아 있으면
        if g1[0] < g2[0]:
            result.append(g1.pop(0))
        else:
            result.append(g2.pop(0))

    # 자료 비교 후 남아있는 요소 추가
    while g1:
        result.append(g1.pop(0))
    while g2:
        result.append(g2.pop(0))

    return result


if __name__ == "__main__":
    list1 = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
    print(merge_sort1(list1))
