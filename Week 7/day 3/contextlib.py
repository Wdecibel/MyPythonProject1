# __Author__: Han
# __Date__: 2019/2/20

# url: www.cnblogs.com/yuanchenqi/articles/5733873.html

# contextlib模块的作用是提供更易用的上下文管理器，它是通过Generator实现的。
# contextlib中的contextmanager作为装饰器来提供一种针对函数级别的上下文管理机制，常用框架如下：
from contextlib import contextmanager

# @contextmanager
# def make_context():
#     print('enter')
#     try:                        # yield前面的语句可看作代码块执行前操作，yield之后的操作可以看作在__exit__函数中的操作。
#         yield 'ok'              # 为了保证异常安全（能处理异常）as后的变量的值是由yield返回
#     except RuntimeError as err:
#         print('error', err)
#     finally:
#         print('exit')
#
#
# with make_context() as value:
#     print(value)

@contextmanager
def loudLock():
    print('Locking')
    lock.acquire()
    yield
    print('Releasing')
    lock.release()

with loudLock():
    print('Lock is locked: %s' % lock.locked())
    print('Doing something that needs locking')






