# 겉보기에는 똑같은 동전 n개가 있다. 이 중에서 한 개는 싸고 가벼운 재료로 만들어진 '가짜 동전'일 때, 좌 우 무게를 비교할 수 있는 양팔 저울을 이용해 가짜 동전 찾아내기
# 입력 : 전체 동전 위치의 시작과 끝
# 출력 : 가짜 동전의 위치 번호

# 양팔 저울
# a ~ b 동전 그룹 / c ~ d 동전 그룹
# a~b에 가짜 동전이 있다면 -1, c~d에 가짜 동전이 있다면 1, 둘 다 없으면 0 return


def weight(a, b, c, d):
    # 임의의 fake 동전 위치
    fake = 29
    if a <= fake and fake <= b:
        return -1
    if c <= fake and fake <= d:
        return 1
    return 0


def find_fakecoin(left, right):
    half = right - left

    # 100개의 동전이 있다고 가정할 때 0~49는 g1, 50~99은 g2
    g1_left = left
    g1_right = left + half - 1
    g2_left = left + half
    g2_right = g2_left + half - 1

    result = weight(g1_left, g1_right, g2_left, g2_right)

    if result == -1:  # g1에 가짜 동전이 있을 때
        return find_fakecoin(g1_left, g1_right)
    elif result == 1:  # g2에 가짜 동전이 있을 때
        return find_fakecoin(g2_left, g2_right)
    else:  # 두 그룹 안에 가짜 동전이 없음
        return right  # 두 그릅으로 나누지 않고 남은 나머지 한 개의 동전이 가짜


if __name__ == "__main__":
    n = 100
    print(find_fakecoin(0, n - 1))
