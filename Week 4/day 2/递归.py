#__author__: Han
#__date__: 2019/1/4

# def fat(n):
#     ret = 1
#     for i in range(1, n+1):
#         ret = ret * i
#     return ret
#
# print(fat(5))

# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n-1)
#
# print(fact(5))


def f(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    elif n < 1:
        return None
    else:
        return f(n-2) + f(n-1)
print(f(5))