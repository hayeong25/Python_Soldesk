# 짝짓기 조합 만들기


def name_matching(list1):
    for i in range(0, len(list1) - 1):
        for j in range(i + 1, len(list1)):
            print("{} - {}".format(list1[i], list1[j]), end="\t")


if __name__ == "__main__":
    list1 = ["Tom", "Jerry", "Mike"]
    name_matching(list1)
