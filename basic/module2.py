# 모듈 사용 방법
# 1. import 모듈명
# form 모듈명 import 특정 함수 => 바로 불러와서 사용할 수 있어 편리

from math import sin, cos, floor, ceil

print(sin(1))
print(cos(1))
print(floor(2.5))
print(ceil(2.5))

# as : 모듈명에 별칭 붙일 때 사용
import math as m

print(m.ceil(3.14))
print(m.sin(1))
print(m.cos(1))
print(m.floor(2.4))
