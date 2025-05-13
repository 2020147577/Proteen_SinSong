# 함수 실습

def functionA():
    global x
    x = 0

x = 2
# functionA()
print(x)


# 실습 1: def factorial
def factorial(n):
    """
    n을 받아서 n!를 출력하는 함수
    :param n: 팩토리얼 인자
    :return: 팩토리얼 값
    """
    result = 1
    # for ... in range(...):
    #     ...
    return result


# print(factorial(4))


# 실습 2: def calculator
def calculator(x1, x2, action):
    """
    더하기, 빼기, 곱하기만 수행하는 계산기
    :param x1: 첫번째 숫자
    :param x2: 두번째 숫자
    :param action: add, sub, mul 세개 중 하나를 받는다
    :return: 결과값을 출력
    """
    # if action == "add":
    #     temp = ...
    #     return temp
    # elif action == ...:
    #     ...
    # elif action == ...:
    #     ...
    return 0


x1 = int(input("첫번째 숫자: "))
x2 = int(input("두번째 숫자: "))
action = input("add/sub/mul: ")
print(calculator(x1, x2, action))
