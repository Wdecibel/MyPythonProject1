# __Author__: Han
# __Date__: 2019/1/9


class MyRange(object):
    def __init__(self, n):
        self.index = 0
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.n:
            val = self.index
            self.index += 1
            return val
        else:
            raise StopIteration


for i in MyRange(10):
    print(i)


