# 동명이인 찾기

# 중복된 이름을 set 구조에 담기
def dup_name(list1):
    name_dict = {}

    # 반복문 - 이름이 등장한 횟수를 딕셔너리로 만듦
    for name in list1:
        if name in name_dict:
            name_dict[name] += 1
        else:
            name_dict[name] = 1
    print(name_dict)

    result = set()
    for name in name_dict:
        if name_dict[name] >= 2:
            result.add(name)


if __name__ == "__main__":
    list1 = ["Tom", "Jerry", "Mike", "Tom"]
    print(dup_name(list1))
