# 스택 : LIFO
# 큐 : FIFO

# 리스트
# 회문 : 순서대로 읽어도 거꾸로 읽어도 내용이 같은 낱말이나 문장 ex) 기러기, 일요일, ...

# 주어진 문장이 회문인지 아닌지 찾기
def palindrome1(s):
    qu = []  # queue
    st = []  # stack

    # 받은 문자를 큐와 스택에 담기 (알파벳인 경우만. 소문자로 변경해 담기)
    for x in s:
        if x.isalpha():
            qu.append(x.lower())
            st.append(x.lower())

    # 큐와 스택에 들어있는 문자를 꺼내면서 비교
    # 큐에 문자가 남아있는 동안 반복
    while qu:
        # 큐와 스택에서 꺼낸 문자가 다르면 return false
        if qu.pop(0) != st.pop():
            return False
    return True


# 문장의 앞뒤를 차례로 비교
def palindrome2(s):
    # 시작 위치 지정
    start = 0

    # 종료 위치 지정
    end = len(s) - 1

    while start < end:
        # start 위치에 있는 문자가 알파벳 문자가 아니면 start + 1
        if not s[start].isalpha():
            start += 1

        # end 위치에 있는 문자가 알파벳 문자가 아니면 end - 1
        elif not s[end].isalpha():
            end -= 1

        # start와 end 위치에 있는 문자를 소문자로 변경한 후 비교해서 같지 않으면 False
        elif s[start].lower() != s[end].lower():
            return False

        # 위 세 가지 경우가 아니라면 start + 1, end - 1
        else:
            start += 1
            end -= 1
    return True


if __name__ == "__main__":
    print(palindrome1("Wow"))
    print(palindrome1("Madam, I'm Adam."))
    print(palindrome1("Madam, I am Adam."))
    print(palindrome2("Wow"))
    print(palindrome2("Madam, I'm Adam."))
    print(palindrome2("Madam, I am Adam."))
