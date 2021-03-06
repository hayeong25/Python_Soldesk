# 병합정렬


def merge_sort(list1):
    # 종료조건
    if len(list1) <= 1:
        return list1

    # 분해작업
    mid = len(list1) // 2  # 중간 값 구하기
    g1 = list1[:mid]  # 재귀호출로 첫 번째 그룹 g1 = [6, 8, 3, 9, 10] => g1[6, 8] & g2[3, 9, 10]
    g2 = list1[mid:]

    merge_sort(g1)
    merge_sort(g2)

    # 병합
    i1, i2, ia = 0, 0, 0

    while i1 < len(g1) and i2 < len(g2):
        if g1[i1] > g2[i2]:
            list1[ia] = g1[i1]
            i1 += 1
            ia += 1
        else:
            list1[ia] = g2[i2]
            i2 += 1
            ia += 1

    # 남아 있는 자료 결과에 추가
    while i1 < len(g1):
        list1[ia] = g1[i1]
        i1 += 1
        ia += 1
    while i2 < len(g2):
        list1[ia] = g2[i2]
        i2 += 1
        ia += 1
    return list


if __name__ == "__main__":
    list1 = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
    print(merge_sort(list1))
