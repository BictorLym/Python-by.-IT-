# 사용자로부터 두 개의 정수를 입력받아서 둘 중에서 큰 수를 출력하는 프로그램 만들기

a = int(input("첫 번째 정수를 입력하세요 : "))
b = int(input("두 번째 정수를 입력하세요 : "))

if a>b:
    print(a)
elif a == b:
    print("a와 b가 같습니다.")
else :
    print("b가 더큽니다.", b)
