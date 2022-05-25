# 주차장 프로그램 ( ord() 함수 이용 )
parking_lot = []
top, car_name = 0, "A"

while True:
    number = int(input("[1] 자동차 넣기 | [2] 자동차 빼기 | [3] 종료 : "))
    if number == 1:
        if top >= 5:
            print("주차장이 꽉 찼습니다.")
        else:
            print(car_name, "자동차 주차 완료")
            parking_lot.append(car_name)
            print("주차장 상태 ==> ", parking_lot)
            car_name = chr(ord(car_name) + 1)
            top += 1
    elif number == 2:
        if top < 0:
            print("출차할 자동차가 없습니다.")
        else:
            print(parking_lot[-1], "자동차 출차")
            parking_lot.pop()
            top -= 1
            print("주차장 상태 ==> ", parking_lot)
    elif number == 3:
        print("프로그램을 종료합니다.")
        break
    else:
        print("번호를 다시 입력하세요.")
