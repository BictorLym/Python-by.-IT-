# 파이썬 에서의 자료형(Data-type)
from math import*
# int형을 출력해봄
print(type(17))
# float형을 출력해봄
print(type(18.0))
# str 형을 출력해봄
print(type("안녕하세요"))
# 반지름이 r인 구의 부피는
PI = 3.14
r = 5
volume = 4/3 * pi * r**3
volume = 4/3 * pi * pow(r, 3)
print(volume)

# 구의 겉넓이 공식: 4*pi*r**2
square = 4 * pi * r**2
square = 4 * pi * pow(r,2)
print("구의 겉넓이: ", square)
# print(int("구의 겉넓이: ")+ (square)) # 에러남
print("구의 겉넓이: "+ str(square))   #타입이 일치가 안되어 문자열을 생성할 수 없으므로

