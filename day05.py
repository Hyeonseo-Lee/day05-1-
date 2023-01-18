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

call_func(inha)
