# 사용자에게 참석자의 수를 입력받고, 해당하는 인원의 수에 따라서
# 치킨은 인원당 1마리, 맥주는 인원당 2병, 케잌은 인원 4개를 출력하는
# 프로그램을 작성하시오

# input()함수는 사용자로부터 입력을 받는 용도인데 문자열형태로 저장된다.
# 문자열을 숫자로 바꾸기 위해서 int()함수를 사용하였다
number = int(input("참석자의 수를 입력하세요: "))
print(type(number))

chickens = number
beer = number*2
cakes = number * 4
print("치킨의 수: ", chickens)
print("맥주의 수: ", beer)
print("케잌의 수: ", cakes)