#Lambda

import random

def process(no_lists, f):
    for no in no_lists:
        print(f(no))
def squares(n):
    """
    제곱 함수
    :param n: integer
    :return: integer
    """
    return n * n

numbers = [random.randint(1, 100) for i in range(5)]
print(numbers)
process(numbers, lambda x: x * x)


# import random
#
# def process(no_lists, f):
#     for no in no_lists:
#         print(f(no))
# def squares(n):
#     """
#     제곱 함수
#     :param n: integer
#     :return: integer
#     """
#     return n * n
#
# numbers = [random.randint(1, 100) for i in range(5)]
# print(numbers)
# process(numbers, squares)

