# 동명이인 찾기 알고리즘
# 계산 복잡도 : O(n^2)

# 중복된 이름을 set 구조에 담기
def dup_name(list1):
    names = set()
    for i in range(0, len(list1) - 1):
        for j in range(i + 1, len(list1)):
            if list1[i] == list1[j]:
                names.add(list1[i])
    return names


if __name__ == "__main__":
    list1 = ["Tom", "Jerry", "Mike", "Tom"]
    print(dup_name(list1))
