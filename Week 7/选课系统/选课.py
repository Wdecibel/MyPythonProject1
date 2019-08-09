# __Author__: Han
# __Date__: 2019/2/14
import pickle
import os


class School:

    def __init__(self, name):
        self.name = name

    def save(self):
        pickle.dump(open('123.txt', 'wb'), self)

    def __str__(self):
        return self.name

    @staticmethod
    def get_all():
        obj_list = []
        for item in os.getcwd():
            obj = pickle.load(item)
            obj_list.append(obj)
        return obj_list


s1 = School('上海')
s1.save()
# home/alex/1

s2 = School('北京')
s2.save()
# home/alex/2

school_obj_list = School.get_all()
for obj in school_obj_list:
    # print('学校名称：%s' % obj.name)
    print(obj)










