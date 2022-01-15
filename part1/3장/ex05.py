# 문자열의 연결
# +opeartor는 문자열 사이에 들어가면 문자열을 연결해주는 역할을 한다.
first_name = "Eun Hyuk"
last_name = "Shin"
name = last_name + first_name
print(name)

# 파이썬에서는 모든 데이터에는 데이터 타입이 존재한다. 아래 소스코드에서 확인을 하면
# "Person"은 문자열이고, 100은 int타입이다. 하여 타입의 일치가 되지 않아 서로 연결
# 을 하는데 에러가 발생을 한다.
#temp = "Person" + 100   #에러남
#print(temp)

# 해결하기 위해서는 숫자 100을 str()을 이용하여 문자열로 변환시켜 타입을 서로 일치시켜야
# + 연산자가 문자열 연결해주는데 문제가 없다.
temp = "Person" + str(100)
print(temp)

temp = "Person" + str(100.188)
print(temp)

# 문자열을 숫자로 변환
# 실수일떄는 float()를 사용하면 된다.
price = float("123456")
print(type(price))
print(price)

# 문자열의 반복
# 문자열에서 * 연산자를 사용하면 그만큼 반복이 된다.
arrow = "->"*10
print(arrow)

arrow = "->"
print(arrow*10)

# %s(형식 지정자)
# %s는 문자열이나 숫자값을 변수에 대입해서 자주 변경이 있을 경우 이런 형식을 지정하여
# 상황에 맞게끔 출력을 하도록 하면 될것이다.
# %s(형식지정자)에 정수를 대입
price = 1000
print("가격: %s" %price)
# %s(형식지정자)에 문자열을 대입
time = "13:49"
print("가격: %s" % time)
# %s를 2개 이상을 사용하고자 할 때는
temp = "현재 시간은 %s시 %s분 %s초입니다."
print(temp%(10,38,12))

# 문자열 맨 앞에 f를 붙이고, 출력할 변수, 값을 중괄호 안에 넣습니다.
s = 'coffee'
n = 5
result1 = f'저는 {s}를 좋아합니다. 하루 {n}잔 마셔요.'
print(result1)


