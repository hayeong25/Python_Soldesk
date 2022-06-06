# 학생 번호와 이름이 리스트로 주어졌을 때 학생 번호를 입력하면 해당 학생 이름을 순차탐색으로 찾아 돌려주는 함수 작성
# 찾는 학생이 없다면 물음표 return


def search_name(stu_no, stu_name, num):
    for i in range(len(stu_no)):
        if stu_no[i] == num:
            return stu_name[i]
    return "?"


if __name__ == "__main__":
    stu_no = [39, 14, 67, 105]
    stu_name = ["Justin", "John", "Mike", "Summer"]
    print(search_name(stu_no, stu_name, 39))
    print(search_name(stu_no, stu_name, 67))
    print(search_name(stu_no, stu_name, 190))
