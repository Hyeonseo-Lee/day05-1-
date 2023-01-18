#function


def inha():
    """
    숫자 출력
    :return:
    """
    print(60)


def call_func(f):
    """
    매개변수로 함수를 넘겨 받아 실행
    :param f: 매개변수가 함수
    :return:
    """
    f() #넘겨 받은 함수 실행

def subtract(n1, n2):
    print(n1 -n2)


def run_func(f, arg1, arg2):
    f(arg1, arg2)

run_func(subtract, 99, 88)


a = (5, 7, -1)
print(sum(a))


call_func(inha)
