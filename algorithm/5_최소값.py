# 숫자 n개를 리스트로 입력 받은 후, 최소값 구하기

# 숫자 입력받아 list1에 추가
def num_input(list1):
    while True:
        num = input("숫자를 입력하세요 (q 입력시 종료) : ")
        if num == "q":
            break
        else:
            list1.append(int(num))
    return list1


# 최소값 구하기
def min(list1):
    min = 0
    for l in list1:
        if min > l:
            min = l
    return min


if __name__ == "__main__":
    list1 = list()  # 비어있는 리스트 생성
    num_input(list1)
    print(list1)
    print("최솟값 :", min(list1))
