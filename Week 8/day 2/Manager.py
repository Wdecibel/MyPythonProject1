# __Author__: Han
# __Date__: 2019/2/20

# Manager是为了共享数据
from multiprocessing import Process, Manager


def f(d, l, n):
    d[n] = '1'
    d['2'] = 2
    d[0.25] = None
    l.append(n)
    print('sub:', id(d))

    # print(l)


if __name__ == '__main__':
    with Manager() as manager:
        d = manager.dict()

        l = manager.list(range(5))
        p_list = []
        print('main:', id(d))

        for i in range(10):
            p = Process(target=f, args=(d, l, i))
            p.start()
            p_list.append(p)

        for res in p_list:
            res.join()

        print(d)
        print(l)











