# 리스트 안에 특정한 요소가 있는지 검색

# 순차 탐색 : 특정 요소 위치 return
# 복잡도 : O(n)
def seq_search1(list1, key):
    for i in range(len(list1)):
        if key == list1[i]:
            return i


# 찾는 숫자가 여러 개 들어있다면 모든 위치를 리스트로 return
def seq_search2(list1, key):
    result = []
    for i in range(len(list1)):
        if key == list1[i]:
            result.append(i)
    return result


if __name__ == "__main__":
    list1 = [17, 92, 18, 33, 58, 7, 33, 42]
    print("18 위치 :", seq_search1(list1, 18))
    print("33 위치 :", seq_search1(list1, 33))
    print("80 위치 :", seq_search1(list1, 80))
    print("33 모든 위치 :", seq_search2(list1, 33))
