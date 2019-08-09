# __Author__: Han
# __Date__: 2019/2/21


def f():
    print('ok1')
    count = yield 5
    print(count)
    print('ok2')
    yield 67


# print(f())      # <generator object f at 0x000001D8E8ECD678>

gen = f()
# ret = next(gen)     # 也可以用send进行第一次传值，但只能传None
# print(ret)
gen.send(None)
x = gen.send(10)
print(x)








