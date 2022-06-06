friend_info = {
    "Summer": ["John", "Justin", "Mike"],
    "John": ["Summer", "Justin"],
    "Justin": ["John", "Summer", "Mike", "May"],
    "Mike": ["Summer", "Justin"],
    "May": ["Justin", "Kim"],
    "Kim": ["May"],
    "Tom": ["Jerry"],
    "Jerry": ["Tom"],
}


def print_all_friends(g, name):
    # 앞으로 처리해야 할 사람들을 큐(리스트)에 저장
    queue = []

    # 큐에 추가한 사람들 기록(set)
    end = set()

    # name을 queue, end에 추가
    queue.append((name, 0))  # queue = [("Summer", 0), ("Justin", 1)]
    end.add(name)

    # 반복문 : 큐에 사람이 있을 때까지 큐에서 한 사람씩 꺼내 꺼낸 이름 출력하고, 꺼낸 이름을 키 값으로 해서 아직 큐에 추가된 적 없는 사람을 큐에 추가하고 집합에도 추가
    while queue:
        person, d = queue.pop(0)
        print(person, d)

        for p in g[person]:
            if p not in end:
                queue.append((p, d + 1))
                end.add(p)


if __name__ == "__main__":
    print_all_friends(friend_info, "Summer")
    print_all_friends(friend_info, "Jerry")
