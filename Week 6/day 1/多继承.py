# __Author__: Han
# __Date__: 2019/1/18

# 多继承：
# 左侧优先，深度>广度；共同父类最后执行
# 永远从object实例开始找


class GrandFather1:
    def smoke(self):
        pass


class Father1(GrandFather1):
    def drink(self):
        print('Father1')
        print(self)
        pass


class Father2:
    def smoke(self):
        pass

    def drink(self):
        print('Father2')
        print(self)
        pass

    def perm(self):
        pass


class Son(Father2, Father1):
    def baojian(self):
        pass


s = Son()
s.baojian()
s.smoke()



















